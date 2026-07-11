import re

class TextCleaner:

    @staticmethod
    def clean(text:str)->str:
        text = re.sub(r'\s+', ' ', text)  #replace multiple whitespace with a single space

        #remove repetitive spaces
        text = re.sub(r' +', ' ', text)
        return text.strip()  #remove leading and trailing whitespace