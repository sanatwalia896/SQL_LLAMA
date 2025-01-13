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
# groq api key  added in the environemnt
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

## setting the streamlit page title
st.set_page_config(page_title="SQLllama", page_icon="🦙")
st.title("llama3 🦙 : Chat with SQL DB ")

## Problem with sql chat is prompt injection can happen

# INJECTION_WARNING = """
# SQL agent can be vulnerable to prompt injection . Use a DB role with
# """

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"
## radio button

radio_opt = ["Use SQllITE 3 Database - StudentDb", "Connect to your SQL DataBase"]

selected_opt = st.sidebar.radio(
    label="Choose the db which you want to chat ", options=radio_opt
)

if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide MysSQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("MySQL password", type="password")
    mysql_db = st.sidebar.text_input("MySQl database")

else:
    db_uri = LOCALDB

if not db_uri:
    st.info("Please enter the database information and uri ")

### LLM model calling
llm = ChatGroq(model="llama-3.1-8b-instant")


@st.cache_resource(ttl="2h")
def configure_db(
    db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None
):
    if db_uri == LOCALDB:
        db_filepath = (Path(__file__).parent / "StudenDb.db").absolute()
        print(db_filepath)

        creator = lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", uri=True)

        return SQLDatabase(create_engine("sqlite:///", creator=creator))

    elif db_uri == MYSQL:
        if mysql_host and mysql_user and mysql_password and mysql_db:
            st.error("Please provide all MySQl connection details.")
            st.stop()
        return SQLDatabase(
            create_engine(
                f"msql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
            )
        )


if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

## toolkit
