from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.runnables import RunnablePassthrough

system_prompt_initial = """Du bist Englischlehrer. Du fässt dich kurz
"""

# Get the prompt to use - you can modify this!
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
        (
            "human",
            """Eingereichter Lösungsvorschlag des Studenten: {student_sentence_english}
            Richtige Lösung wäre gewesen: {examiner_sentence_english} 
            
            Fehler des Studenten: {mistakes_made}
            
            Auf welche Signale oder Hinweise in dem Satz hätte der Student achten müssen damit der Fehler nicht passiert wäre?
            Fasse dich sehr kurz als wäre es ein hinweis an einen anderen Lehrer auf einer Lehrerkonferenz. 
            Du hast so wenig Zeit wie bei einem Elevator Pitch.
            Liste die spezifischen grammatikalischen Konzepte auf, die der Student im Zusammenhang 
        mit dem Present Perfect Continuous nicht verstanden hat, und nutze dabei die Fachterminologie der Sprachwissenschaft.
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

empfehler_agent = prompt | llm


def getEmpfehlerAgent():
    return empfehler_agent
