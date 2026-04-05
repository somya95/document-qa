from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def load_document(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def ask_question(question, text):
    prompt = f"""
            Here is content for your reference: {text}
            Based on the above content, answer the following question: {question}
            If the answer is not in the content provided, say so clearly.
            """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    return response.text

doc = load_document('sample.txt')
print(f"Loaded {len(doc)} characters")

user_query = input('Question: ')
answer = ask_question(doc, user_query)
print(f'Answer: {answer}')