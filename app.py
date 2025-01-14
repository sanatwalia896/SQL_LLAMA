import streamlit as st
from pathlib import Path
from langchain.agents.agent_types import AgentType
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

load_dotenv()

# groq api key  added in the environment
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Setting the Streamlit page title
st.set_page_config(page_title="SQLllama", page_icon="🦙")
st.title("llama3 🦙 : Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Radio button
radio_opt = ["Use SQLite 3 Database - StudentDb", "Connect to your SQL Database"]

selected_opt = st.sidebar.radio(
    label="Choose the DB you want to chat with", options=radio_opt
)

if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("MySQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database")
    connect_btn = st.sidebar.button("Connect to MySQL")
else:
    db_uri = LOCALDB
    connect_btn = None

# LLM model
llm = ChatGroq(model="llama-3.1-8b-instant")


@st.cache_resource(ttl=7200)
def configure_db(
    db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None
):
    if db_uri == LOCALDB:
        db_filepath = Path(
            "/Users/sanatwalia/Desktop/Assignments_applications/SQL_CHATBOT/StudentDb.db"
        ).absolute()
        print(db_filepath)
        creator = lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(
            create_engine(
                f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
            )
        )


if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
    st.success("Successfully connected to the MySQL database!")
else:
    db = configure_db(db_uri)
    st.success("Connected to the SQLite database!")

# Further implementation with `toolkit` and SQL agent.

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

if "messages" not in st.session_state or st.sidebar.button("Clear Message history"):
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you? "}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})

    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})

        st.write(response)
