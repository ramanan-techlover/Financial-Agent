import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dataclasses import dataclass

@dataclass
class Message:
    actor: str
    payload: str

USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"

# API KEY
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]  # Correctly retrieve the API key from Streamlit secrets
Groq.api_key = GROQ_API_KEY  # Set the API key for Groq

# Initialize session state for conversation history
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?")]

# Initialize agents
web_agent = Agent(
    name="Web Agent",
    role="Provide information by searching the web and always include sources with direct links.",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Describe your role clearly when asked.",
        "Always include sources with direct links to the pages."
    ],
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Assist with financial data like stock prices, company info, and analysis, providing detailed tables and exact answers.",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=[
        "Describe your role clearly when asked.",
        "Use tables to display data and analysis.",
        "Provide exact answers to user queries."
    ],
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=[
        "Always include sources with direct links.",
        "Use tables to display data and analysis.",
        "Provide detailed answers to user queries.",
        "Describe your roles clearly when asked."
    ],
    markdown=True,
)

# Streamlit UI
st.set_page_config(page_title="Finance Agent", layout="centered")
st.title("Finance Agent - ChatBot")

# Display existing messages
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)

# Capture user input
prompt: str = st.chat_input("Enter a prompt here")

if prompt:
    # Append user message to session state
    st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
    st.chat_message(USER).write(prompt)  # Display user message immediately

    with st.spinner("Processing..."):
        try:
            # Get response from the agent team
            assistant_response = agent_team.run(prompt, stream=False)

            # Check if the response has a `.content` attribute or is a string
            if hasattr(assistant_response, "content"):
                response_content = assistant_response.content
            elif isinstance(assistant_response, str):
                response_content = assistant_response
            else:
                response_content = "I couldn't process your request. Please try again."

            # Append assistant response to the conversation history
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response_content))
            st.chat_message(ASSISTANT).write(response_content)  # Display bot response immediately

        except Exception as e:
            # Handle exceptions with a fallback message
            st.error(f"An error occurred: {str(e)}")
            fallback_response = (
                "I'm here to help! I can search the web or provide financial insights. Let me know what you need."
            )
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=fallback_response))
            st.chat_message(ASSISTANT).write(fallback_response)  # Display fallback response immediately
