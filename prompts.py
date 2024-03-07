from langchain.prompts import PromptTemplate


template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""

CONDENSE_QUESTION_PROMPT=PromptTemplate.from_template(template)


prompt_template = """You are a helpful AI assistant. Use the following pieces of context to answer the question at the end.

{context}

Question: {question}
Helpful answer in markdown format:"""

QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
