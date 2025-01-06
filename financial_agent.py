import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# API KEY
GROQ_API_KEY = "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"
Groq.api_key = GROQ_API_KEY

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
st.set_page_config(page_title="Chatbot Interface", layout="centered")
st.title("Chatbot Interface")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message here:"):
    # Append user input to the conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Processing..."):
        try:
            # Get response from the agent team
            assistant_response = agent_team.run(user_input, stream=False)

            # Check if the response has a `.content` attribute or is a string
            if hasattr(assistant_response, "content"):
                response_content = assistant_response.content
            elif isinstance(assistant_response, str):
                response_content = assistant_response
            else:
                response_content = "I couldn't process your request. Please try again."

            # Append assistant response to the conversation history
            st.session_state.messages.append({"role": "assistant", "content": response_content})

            # Display the assistant's response
            with st.chat_message("assistant"):
                st.markdown(response_content)

        except Exception as e:
            # Handle exceptions with a fallback message
            st.error(f"An error occurred: {str(e)}")
            fallback_response = (
                "I'm here to help! I can search the web or provide financial insights. Let me know what you need."
            )
            st.session_state.messages.append({"role": "assistant", "content": fallback_response})
            with st.chat_message("assistant"):
                st.markdown(fallback_response)
