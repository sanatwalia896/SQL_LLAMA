# SQLLlama: Chat with Your Database

SQLLlama is a Streamlit-based chatbot application that enables users to interact with SQL databases seamlessly using natural language queries. The app supports SQLite and MySQL databases and leverages the power of large language models (LLMs) to understand and respond to user queries.

---

## Features

- **Interactive Chat Interface**: Query your database using a simple chat-based UI.
- **Database Options**:
  - Connect to a local SQLite database.
  - Connect to a remote MySQL database
- **Streamlined Connectivity**: Easy setup for database connections with built-in error handling.
- **LLM-Powered Responses**: Utilizes the ChatGroq model for intelligent query handling.
- **Session Management**: Maintains chat history during a session with options to clear history.

---

## Installation

### Prerequisites

- Python 3.8 or above
- pip

### Required Libraries

Install the required Python libraries using the following command:

```bash
pip install streamlit langchain sqlalchemy sqlite3 dotenv mysql-connector-python
```

---

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Environment Variables**:
   Create a `.env` file in the project root directory and add your Groq API key:

   ```env
   GROQ_API_KEY=<your-groq-api-key>
   ```

3. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

---

## Usage

### Step 1: Select Database Type

- Choose between:
  1. `Use SQLite 3 Database - StudentDb`
  2. `Connect to your SQL Database`

### Step 2: Configure Database

- For SQLite:
  - The app automatically connects to the `StudentDb.db` file located at a predefined path.
- For MySQL:
  - Provide the host, username, password, and database name in the sidebar inputs.
  - Click the **Connect to MySQL** button.

### Step 3: Query the Database

- Use the chat interface to type your queries (e.g., "Show all students who scored above 90").
- View the response in the chat window.

---

## Project Structure

```
SQLLlama/
├── app.py              # Main application file
├── .env                # Environment variables (excluded in version control)
├── requirements.txt    # List of dependencies
└── StudentDb.db        # Sample SQLite database
```

---

## Acknowledgments

This application is built using the following technologies:

- [Streamlit](https://streamlit.io/): For creating interactive web apps.
- [LangChain](https://docs.langchain.com/): For building LLM-powered applications.
- [SQLAlchemy](https://www.sqlalchemy.org/): For database connection and ORM.
- [ChatGroq](https://groq.com/): For natural language understanding and query processing.

This project is inspired and influenced greatly by project learning from Krish Naik in his tutorials.

---

## Troubleshooting

1. **Connection Issues**:

   - Ensure correct MySQL credentials are provided.
   - Check the availability of the database server.

2. **Environment Variable Issues**:

   - Verify the `.env` file is properly configured and loaded.

3. **Missing Dependencies**:

   - Run `pip install -r requirements.txt` to ensure all dependencies are installed.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For further assistance or inquiries, please contact:

**[SANAT WALIA ]**\
Email: [[codersanat896@gmail.com](mailto:your-email@example.com)]
