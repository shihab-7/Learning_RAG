from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from deep_translator import GoogleTranslator

class UniversityLLM:

    def __init__(self):
        
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0.2,
            num_ctx=8192
        )
        self.translator=GoogleTranslator(source='en', target='bn')
    
    def _invoke(self, system_prompt, user_prompt):
        response = self.llm.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ]
        )
        return response.content.strip()
    
    

    # qwen2.5:3b er bangla reasoning onek kharap
    # just llm diye shajano answer tai abar bangla te translate kora maybe best lagbe
    

    def generate_answer(self, question, context):

        system_prompt = """
                You are DIU AI Assistant.

                You are given two trusted sources of information.

                Source 1: PERSONAL INFORMATION
                Source 2: UNIVERSITY INFORMATION

                Treat BOTH sources as equally valid.

                

                Rules:
                - If the answer is in PERSONAL INFORMATION, answer from there.
                - If the answer is in UNIVERSITY INFORMATION, answer from there.
                - If neither contains the answer, reply exactly:

                "I couldn't find that information."

                - Use whichever information is relevant.
                - If both are required, combine them.
                - Never invent information.
                - The contexts are always correct.
                - Use ONLY the contexts.
                - Never hallucinate.
                - Never use outside knowledge.
                - Answer ONLY the user's question.
                - Ignore unrelated context.
                - Answer in English.
                - If the answer contains rules, eligibility criteria or percentages, include every item.
                - Prefer bullet points.
                
                Instructions:
                1. Determine whether the question needs personal information, university information, or both.
                2. If both are needed, first extract the relevant personal facts, then compare them with the university rules.
                3. Explain your reasoning before giving the conclusion.
                4. Never ignore PERSONAL INFORMATION if it is available.
                5. Never ignore UNIVERSITY INFORMATION if it contains applicable rules.
                """

        user_prompt = f"""
                You are given university documents.

                Context
                -----------------

                {context}

                User Question
                -----------------

                {question}

                Answer the question using ONLY the context.
                """

        return self._invoke(system_prompt, user_prompt)
        
    def translate_to_bangla(self, english_answer):
        try:
            return self.translator.translate(english_answer)
        except Exception as e:
            print(f"Translation error: {e}")
            return english_answer
        
    #akhon direct invoke use na kore ask use kore custom behaviour implement kora jabe
    def ask(self, question,context):

        answer=self.generate_answer(question,context)
        print(f"English Answer: {answer}")

        if answer.strip() == "I couldn't find that information in the university documents.":
            return "দুঃখিত, এই তথ্যটি বিশ্ববিদ্যালয়ের নথিতে পাওয়া যায়নি।"
        
        return self.translate_to_bangla(answer)