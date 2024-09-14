import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.memory import ConversationSummaryBufferMemory

# Load environment variables
load_dotenv()

# Function to initialize session state
def init_state():
    st.session_state.messages = []
    st.session_state.history = []
    st.session_state.session_id = "unique_session_id"
    st.session_state.token_count = 0

# Function to select and initialize the LLM model
def select_llm_model(model_name, temperature):
    model_mapping = {
        "Gemma-7b-IT": "gemma-7b-it",
        "Llama3–70b-8192": "llama3-70b-8192",
        "Llama3–8b-8192": "llama3-8b-8192",
        "Mixtral-8x7b-32768": "mixtral-8x7b-32768"
    }
    selected_model = model_mapping.get(model_name)
    groq_api = st.secrets["grok"]["GROQ_API_KEY"]
    if not groq_api:
        raise ValueError("GROQ_API_KEY secret is not set.")
    llm = ChatGroq(temperature=temperature, model=selected_model, api_key=groq_api)
    return llm

# Function to convert Excel file to DataFrame
def convert_excel_to_df(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"Error reading the file: {str(e)}")
        return None

prompt = '''You are a demand forecasting expert. You have access to an Excel file named "SAPReport.xlsx," which contains historical sales data, product information, and demand trends. For each user query, you must analyze the relevant data and provide accurate demand forecasts.
Key points for your analysis:
1. Use the historical data from "SAPReport.xlsx" to identify patterns and trends.
2. Generate demand forecasts based on the provided input query.
3. Include any relevant assumptions and insights based on the data.
'''

# Function to create a pandas dataframe agent
def create_pandas_agent(llm, df):
    try:
        agent_executor = create_pandas_dataframe_agent(
            llm,
            df,
            agent_type="tool-calling",
            verbose=True,
            prefix=prompt, 
            include_df_in_prompt=True
        )
        return agent_executor
    except Exception as e:
        st.error(f"Error creating pandas agent: {str(e)}")
        return None

# Function to query the agent and extract output
def query_data(agent, query):
    try:
        if agent is None:
            raise ValueError("Agent is not initialized properly.")
        
        response = agent.invoke(query)
        
        output_value = response.get('output', 'No output found')
        graph_code = response.get('graph_code', '').strip()
        token_usage = response.get('response_metadata', {}).get("token_usage", {}).get("total_tokens", 0)
        
        st.session_state.token_count += token_usage
        
        return output_value, graph_code
    except AttributeError as e:
        st.error(f"AttributeError: {str(e)}")
    except ValueError as e:
        st.error(f"ValueError: {str(e)}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Set up the Streamlit page
st.set_page_config(page_title="Demand Forecast Chatbot", page_icon="📊", layout="wide")
st.title("Demand Forecast Chatbot")

# Initialize session state if not already present
if 'messages' not in st.session_state:
    init_state()

# Directly specify the file path
file_path = "SAPReport.xlsx" 

if file_path:
    with st.spinner("Loading data..."):
        df = convert_excel_to_df(file_path)
        if df is not None:
            data_file_name = os.path.basename(file_path)

            # Sidebar for model selection
            with st.sidebar:
                st.subheader("Select LLM Model")
                selected_model = st.radio(
                    "Choose a model:",
                    ("Gemma-7b-IT", "Llama3–70b-8192", "Llama3–8b-8192", "Mixtral-8x7b-32768"),
                    index=1  # Default to Llama3-70b-8192
                )
                
                temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.1)

                st.markdown(f"**Data File:** {data_file_name}")

            st.sidebar.markdown("""
                **Note:**
                - This chatbot is fed with SAP's data from 2015 and 2016.
                - It may make mistakes in its forecasts.
            """)

            if selected_model:
                llm = select_llm_model(selected_model, temperature)
                memory = ConversationSummaryBufferMemory(llm=llm, memory_key="chat_history", return_messages=True)
                agent = create_pandas_agent(llm, df)

                # Display existing messages
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"], unsafe_allow_html=True)

                # Handle user input and agent response
                if prompt := st.chat_input("Type your message here..."):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.chat_message("user"):
                        st.write(prompt)

                    with st.chat_message("assistant"):
                        placeholder = st.empty()
                        placeholder.markdown("...")

                        try:
                            output_value, graph_code = query_data(agent, prompt)
                            placeholder.markdown(output_value, unsafe_allow_html=True)
                            st.session_state.messages.append({"role": "assistant", "content": output_value})

                            if graph_code:
                                exec(graph_code)
                                st.pyplot(plt.gcf())
                            
                        except KeyError as e:
                            st.error(f"KeyError: {str(e)}")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

# Display chat history if any
if st.session_state.history:
    for chat in st.session_state.history:
        st.write(f"**You:** {chat['query']}")
        st.write(f"**Agent:** {chat['response']}")
