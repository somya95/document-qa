from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Load document into memory
def load_document(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# Ask Question from LLM and return its output
def ask_question(question, text, conversation_history):
    prompt = f"""
            Here is content for your reference: 
            {text}

            Previous conversation:
            {conversation_history}

            Based on the above content, answer the following question: 
            {question}

            If the answer is not in the content provided, say so clearly.
            """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    return response.text

print('Reading the document.\n')
doc = load_document('sample.txt')
print(f"Loaded {len(doc)} characters")
print("Enter 'exit' to quit conversational loop. \n")

# Initializing Conversation History
conversation_history = []

while True:
    user_query = input('Question: ')
    if user_query.lower() == 'exit':
        print('\nEnding Session. Goodbye!\n')
        break
    elif user_query.strip() == '':
        print("Question cannot be blank. Please retry.")
    else:
        try:
            answer = ask_question(doc, user_query, conversation_history)
            print(f'\nAnswer: {answer}\n')

            # Append to conversation history
            conversation_history.append(
                {
                    'question': user_query,
                    'answer': answer
                }
            )
        except Exception as e:
            print(f'\nSomething went wrong: {e}. Please try again.\n')