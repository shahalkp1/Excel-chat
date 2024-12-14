# Excel-Chat

**Excel-Chat** provides a free and intuitive way to interact with your data using natural language. 

## Features
- Upload `.csv` or `.xlsx` files.
- Ask questions about your data and get answers instantly.
- View the corresponding Python code for full transparency.
- Powered by **PandasAI** and **Bamboo LLM**, making data analysis simple and efficient.


<img width="1231" alt="image" src="https://github.com/user-attachments/assets/e2c31e70-7949-4478-b73a-ba0745e5c983" />

## Setup Instructions

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.9 or later
- Streamlit installed (for running the app)
- API key for Bamboo LLM (if required)

### Installation
1. **Clone the Repository**

2. **Create a Virtual Environment**
      python3 -m venv venv
      source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. **Install Dependencies**
     pip install -r requirements.txt

4. **Set API Key**
     Add your Bamboo LLM API key to a .streamlit/secrets.toml
     You can get your free API key signing up at https://pandabi.ai

5. Run the Application
    streamlit run app.py
