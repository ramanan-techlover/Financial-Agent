# Financial Agent

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)](https://streamlit.io/)  
[![Groq AI](https://img.shields.io/badge/Powered%20by-Groq-blue)](https://groq.com/)  

A powerful and user-friendly chatbot interface designed to provide financial insights and web-sourced information. Built using the Phi framework and integrated with cutting-edge tools like DuckDuckGo for web searches and YFinanceTools for real-time financial data analysis.

## 🌟 Features
- **Web Search**: Provides accurate and detailed information from the web, including verified sources.  
- **Financial Insights**: Fetches stock prices, company information, analyst recommendations, and more using YFinanceTools.  
- **Conversation History**: Displays a complete history of user and assistant interactions in a structured interface.  
- **Customizable Roles**: Agents with specific roles ensure focused and efficient responses to queries.  
- **Streamlit Interface**: An intuitive and responsive web app built on Streamlit for seamless user interaction.  

## 🚀 Live Demo
Check out the live app here: [Financial Agent](https://financial-agent-bot.streamlit.app)  

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ramanan-techlover/Financial-Agent.git
   cd Financial-Agent
   ```

2. **Install dependencies**:
   Create a virtual environment and install the required packages:
   ```bash
   python -m venv aienv
   aienv\Scripts\activate  # On Mac, use `source aienv/bin/activate`
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   - Add your API keys to a `.env` file in the root directory:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key
     ```
   - Store `GROQ_API_KEY` in your Streamlit secrets for deployment.

4. **Run the app**:
   ```bash
   streamlit run financial_agent.py
   ```

## 🛠️ Technology Stack
- **[Streamlit](https://streamlit.io/)**: Simplifies building beautiful web apps for machine learning and data science.  
- **[Phi Framework](https://phi-framework.org/)**: Enhances conversational AI with agent-based modular architecture.  
- **[Groq AI](https://groq.com/)**: Provides robust AI models for versatile chatbot capabilities.  
- **[DuckDuckGo API](https://duckduckgo.com/)**: For secure and anonymous web searches.  
- **[YFinanceTools](https://pypi.org/project/yfinance/)**: Powers real-time financial data analysis.  

## 📖 How It Works
1. **User Interaction**: Users input queries via a chat interface.  
2. **Agent Assignment**: The query is routed to a specific agent based on its context (e.g., web or financial queries).  
3. **Processing & Response**: The assigned agent processes the query using the integrated tools and provides a response with sources or detailed analysis.  
4. **Conversation Display**: Responses and prompts are displayed in the chat interface, with user messages on the right and bot replies on the left.  

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.  
2. Create a new branch for your feature: `git checkout -b feature-name`.  
3. Commit your changes: `git commit -m "Add a new feature"`.  
4. Push to your branch: `git push origin feature-name`.  
5. Open a pull request.  

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## 📬 Contact
If you have any questions, feel free to reach out:
- **Author**: [Ramanan](https://github.com/ramanan-techlover)  
- **Repository**: [Financial Agent](https://github.com/ramanan-techlover/Financial-Agent)  
