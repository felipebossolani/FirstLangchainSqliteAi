import os
import getpass
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# Configurando as chaves de API
os.environ["OPENAI_API_KEY"] = getpass.getpass("Digite sua OpenAI API Key: ")

# Conectando ao banco de dados SQLite
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Configurando o modelo de linguagem (LLM)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Criando o agente SQL
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

# Executando uma consulta com o agente
response = agent_executor.invoke("Qual o artista possui mais albuns?")
print(response)

response = agent_executor.invoke("Quantos albuns começcam com a letra 'T'?")
print(response)

response = agent_executor.invoke("Qual o total de músicas do Led Zeppelin?")
print(response)
