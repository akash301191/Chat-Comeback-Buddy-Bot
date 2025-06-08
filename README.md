# Chat Comeback Buddy Bot

**Chat Comeback Buddy Bot** is a fun and dynamic Streamlit application that takes in real chat snippets and generates clever, humor-filled comeback messages—paired with expressive GIFs. Powered by [Agno](https://github.com/agno-agi/agno), OpenAI's GPT-4o, and Giphy, this bot helps you respond with charm, wit, and personality in every conversation.

## Folder Structure

```
Chat-Comeback-Buddy-Bot/
├── chat-comeback-buddy-bot.py
├── README.md
└── requirements.txt
```

* **chat-comeback-buddy-bot.py**: The main Streamlit application.
* **requirements.txt**: Required Python packages.
* **README.md**: This documentation file.

## Features

* **Chat Snippet Input**
  Paste any message or mini-conversation to spark a clever reply.

* **Tone & Intensity Selector**
  Customize the style of the comeback—whether witty, sarcastic, savage, or silly.

* **AI-Powered Comeback Generation**
  A GPT-4o-powered agent analyzes your conversation and crafts an appropriate comeback line.

* **GIF Selection via Giphy**
  The bot performs a focused GIF search using the comeback's tone and delivers a perfect visual punchline.

* **Markdown Output**
  Your entire chat (with the generated comeback and embedded GIF) is formatted in clean Markdown.

* **Download Option**
  Save the final conversation as a `.md` file for sharing or reuse.

* **Minimalist UI with Streamlit**
  The app is built with a responsive and distraction-free Streamlit interface.

## Prerequisites

* Python 3.11 or higher
* An OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))
* A Giphy API key ([Get one here](https://developers.giphy.com/dashboard/))

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/akash301191/Chat-Comeback-Buddy-Bot.git
   cd Chat-Comeback-Buddy-Bot
   ```

2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the app**:

   ```bash
   streamlit run chat-comeback-buddy-bot.py
   ```

2. **In your browser**:

   * Paste a chat or conversation snippet.
   * Choose your preferred **comeback style** and **intensity level**.
   * Click **🎯 Generate Comeback**.
   * View your updated chat with an AI-crafted response and a matching GIF.

3. **Download Option**
   Use the **📥 Download Comeback Response** button to save the full chat in Markdown format.

## Code Overview

* **`render_chat_inputs()`**: Captures chat input, tone preference, and intensity settings.
* **`render_sidebar()`**: Collects and stores OpenAI and Giphy API keys.
* **`generate_chat_response()`**:

  * Uses a GPT-4o-powered agent to generate a clever comeback.
  * Searches Giphy using a concise, expressive query.
  * Formats the full output in Markdown, including the GIF.
* **`main()`**: Orchestrates the app layout, input capture, and final output display.

## Contributions

Contributions are welcome! If you have ideas for improvement, bug fixes, or new features, feel free to fork the repo and open a pull request. Make sure your changes are clean, tested, and aligned with the app’s purpose.
