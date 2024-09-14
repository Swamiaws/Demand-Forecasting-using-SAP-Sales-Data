# Demand Forecast Chatbot

## Overview

The Demand Forecast Chatbot is an advanced tool designed to provide accurate demand forecasts based on historical sales data. It leverages a sophisticated language model to analyze data from an Excel file and generate insightful predictions. This chatbot is particularly useful for businesses seeking to understand demand trends and make data-driven decisions.

## Architecture

### Components

1. **Frontend:**
   - **Streamlit:** A web application framework used to create a user-friendly interface for interacting with the chatbot. It handles user inputs, displays responses, and visualizes data.

2. **Backend:**
   - **LangChain-GROQ:** Utilized for language modeling and generating responses. It interfaces with various language models to provide accurate and context-aware answers.
   - **Pandas, OpenPyXL, and Tabulate:** Data manipulation libraries for handling Excel data. These tools are used to read, manipulate, and format data for analysis.
   - **Matplotlib:** Used for plotting and visualizing data trends and forecasts.
   - **Scikit-learn:** Provides machine learning tools and models, such as ARIMA, for forecasting.

3. **Data Processing:**
   - **Excel File:** The primary data source containing historical sales data, product information, and demand trends. The chatbot reads this file to analyze patterns and generate forecasts.

4. **Memory:**
   - **ConversationSummaryBufferMemory:** Keeps track of conversation history and context to ensure coherent interactions.

### Tools Used

- **Streamlit:** Web framework for creating interactive applications.
- **LangChain-GROQ:** Language modeling tool for generating responses.
- **Pandas, OpenPyXL, and Tabulate:** Data manipulation libraries for handling Excel data.
- **Matplotlib:** Plotting library for data visualization.
- **dotenv:** For managing environment variables.
- **Scikit-learn:** For implementing models such as ARIMA.

## Installation

1. **Setup:**
   - Ensure you have Python installed on your system.
   - Install the required Python packages using `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Environment Configuration:**
   - Create a `.env` file in the project directory and add your `GROQ_API_KEY`:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

3. **Prepare Your Data:**
   - Place your Excel file (`SAPReport.xlsx`) in the project directory. Ensure it contains historical sales data and relevant information.

## Running the Application Locally

1. Execute the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```
2. Open the URL provided in the terminal to access the web interface.

## Access the Application

To use the deployed application, click on the following link: [Run the Demand Forecast Chatbot](https://demand-forecasting-using-sap-sales-data.streamlit.app/)
