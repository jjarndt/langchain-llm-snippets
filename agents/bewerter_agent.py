from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.runnables import RunnablePassthrough

system_prompt_initial = """
Du bist Englischlehrer.
"""

# Get the prompt to use - you can modify this!
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),

        (
            "human",
            """
            Eingereichter Lösungsvorschlag des Studenten: {student_sentence_english}
            Richtige Lösung wäre gewesen: {examiner_sentence_english} 
            
            Fasse kurz und prägnant zusammen wo der Fehler liegt im Stile einer Randnotiz 
            des Lehrers über einen Schüler für das Klassenbuch.
        """,
        ),
    ]
)

llm = ChatOpenAI(
    model="gpt-4-0125-preview",
    # model="gpt-3.5-turbo-0125",
    streaming=True,
    temperature=0.0,
)

bewerter = prompt | llm


def getBewerterAgent():
    return bewerter
