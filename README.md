# Document Q&A Bot

A conversational AI application that lets you ask natural language questions about a document. Load a text file, ask anything about its contents — summaries, key ideas, character opinions — and get answers grounded strictly in the document. The app maintains conversation history throughout the session, so follow-up questions are understood in context. Type `exit` to end the session.

> Built as an independent project to learn LLM API integration from scratch.

---

## Why I Built This

I'm transitioning from RPA (Robotic Process Automation) to AI development — moving from rule-based automation to building intelligent, dynamic applications.

For a while I was stuck in tutorial-based learning — consuming content without shipping anything real. This project was my deliberate break from that pattern. I wanted to build something end-to-end, independently, and push it to GitHub.

The biggest thing I wanted to prove to myself was that actually building with AI APIs is not as hard or paralysing as it seems from the outside. It isn't.

---

## Tech Stack

- **Python** — core language
- **Google Gemini API** (`google-genai`) — LLM for answering questions
- **pypdf** — PDF text extraction
- **python-dotenv** — managing API keys securely via `.env`

---

## Setup Instructions

**1. Clone the repository**
```
git clone https://github.com/your-username/document-qa.git
cd document-qa
```

**2. Install dependencies**
```
uv pip install -r requirements.txt
```

**3. Get your Gemini API key**
- Go to [aistudio.google.com](https://aistudio.google.com)
- Sign in with your Google account
- Click **Get API key → Create API key**
- Copy the key

**4. Create a `.env` file in the project folder**
```
GEMINI_API_KEY=your_key_here
```

**5. Add a document**
- Place any `.txt` file in the project folder
- A sample file `sample.txt` is already included in the repo

**6. Run the app**
```
python app.py
```

---

## How to Use It

Run the app:
```
python app.py
```

Enter the path to your document when prompted, then start asking questions. Type `exit` to end the session.

**Example Session — Steve Jobs' 2005 Stanford Commencement Speech**

```
Loaded 12050 characters
Type 'exit' to quit

Question: What are the three stories Jobs talks about?

Answer: Based on the content provided, the three stories Steve Jobs talks about are:

1. Connecting the dots — his decision to drop out of Reed College and how a
calligraphy class later influenced the typography of the first Macintosh.

2. Love and loss — his firing from Apple at 30, and how that period led him to
start NeXT and Pixar and meet his wife.

3. Death — his pancreatic cancer diagnosis and how confronting mortality became
his most important tool for making life decisions.

Question: Summarise the speech in three sentences

Answer: In his 2005 Stanford commencement speech, Steve Jobs shares three personal
stories to encourage graduates to trust their intuition and pursue work they truly
love. He reflects on how unconventional choices ultimately led to his greatest creative
successes. He urges his audience to live authentically, concluding with the famous
exhortation to "stay hungry, stay foolish."

Question: exit
Ending session. Goodbye!
```

---

## Future Improvements

- **RAG pipeline** — currently the entire document is sent to the model with every query, which is slow and won't scale to large documents. The next step is chunking the document, generating embeddings, and retrieving only the relevant chunks per query
- **Multiple file format support** — extend document loading to handle PDFs and Word (`.docx`) files alongside plain text
- **LangChain refactor** — abstract the LLM integration to make the app model agnostic, allowing easy switching between Gemini, OpenAI, and Anthropic
- **Streamlit UI** — replace the command line interface with a simple web interface for better usability
- **Conversation export** — save the Q&A session to a text or PDF file at the end of each session
