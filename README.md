# Agentic-CSV-RAG-Template

## Getting Started

Follow these steps to get the application up and running:

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Surajrs812/Agentic-CSV-RAG-Template.git
cd Agentic-CSV-RAG-Template.git
```

### 2. Add Groq API Key

Create a `.env` file in the root directory of the project and add your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Install Dependencies

Make sure you have all necessary dependencies installed. Run the following command:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

To start the application, use the following command:

```bash
streamlit run app.py
```

### 5. Using the Application

1. **Select LLM Model**: Choose your preferred LLM model from the sidebar.
2. **Ask Questions**: Type your queries in the input box, and the model will analyze your data and provide responses. If the response requires a graph, it will be generated and displayed automatically.
3. **View History**: Previous queries and responses are stored in the session history for your reference.

## Example Queries

Here are some example queries you can try:

- "Compare the sales data for the first and second quarters."
- "What is the average price of products in the dataset?"
- "Generate a bar chart showing the distribution of product categories."

## Troubleshooting

- Ensure that the correct Groq API key is added in the `.env` file.
- Make sure all dependencies are installed correctly.
- If the application crashes, check the terminal for error messages and ensure that your data files are correctly formatted.