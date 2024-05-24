from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.runnables import RunnablePassthrough

system_prompt_initial = """Du bist Englischlehrer. Bitte fasse den Fehler in der Zeitform zusammen, der in folgendem Satz gemacht wurde: {mistakes_made}. Verwende dabei eine knappe und prägnante Formulierung, die den spezifischen Fehler und den Kontext der Verwendung hervorhebt.
"""

# Get the prompt to use - you can modify this!
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),

        (
            "human",
            """{mistakes_made}
        """,
        ),
    ]
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    # model="gpt-3.5-turbo-0125",
    streaming=True,
    temperature=0.0,
)

shortener = prompt | llm


def getShortenerAgent():
    return shortener

#%%
