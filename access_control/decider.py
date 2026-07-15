from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama


class AccessControlDecider:

    def __init__(self):

        self.llm =ChatOllama(
            model="qwen2.5:3b",
            temperature=0
        )

    def decide_access(self, query):

        system_prompt = """
                You are an intent classification engine.

                Your job is to classify the user's query into EXACTLY one category.

                Categories:

                PERSONAL
                - Questions about a user's own information.
                - Examples:
                    - My CGPA
                    - My attendance
                    - My tuition status
                    - My scholarship status
                    - My advisor
                    - My office room
                    - My office hours
                    
                UNIVERSITY
                - Questions about university knowledge.
                - Examples:
                    - Admission policy
                    - Library rules
                    - Scholarship policy
                    - Academic calendar
                    - Code of conduct
                    - Examination regulations

                MIXED
                - Questions requiring BOTH personal information AND university knowledge.
                - Examples:
                    - What is my CGPA and what scholarship can I apply for?
                    - My attendance and examination policy.
                    - My advisor and office regulations.

                Rules:
                - Return ONLY one word.
                - Do NOT explain.
                - Do NOT use punctuation.

                Possible outputs:

                PERSONAL
                UNIVERSITY
                MIXED 
        """

        response = self.llm.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
        )

        return response.content.strip().upper()