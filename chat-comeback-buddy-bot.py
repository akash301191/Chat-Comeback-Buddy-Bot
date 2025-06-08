import streamlit as st
from textwrap import dedent
import re

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.giphy import GiphyTools

def render_sidebar():
    st.sidebar.title("🔐 API Configuration")
    st.sidebar.markdown("---")

    # OpenAI API Key input
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        st.sidebar.success("✅ OpenAI API key updated!")

    # GiphyAPI Key input
    giphy_api_key = st.sidebar.text_input(
        "Giphy API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://developers.giphy.com/dashboard/)."
    )
    if giphy_api_key:
        st.session_state.giphy_api_key = giphy_api_key
        st.sidebar.success("✅ Giphy API key updated!")

    st.sidebar.markdown("---")

def render_chat_inputs():
    st.markdown("---")

    st.subheader("💬 Paste a Chat Snippet")
    chat_text = st.text_area(
        "Paste a message or short conversation you'd like a GIF comeback for.",
        height=200,
        placeholder="e.g., 'Yeah sure, like that plan ever works 😏'"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎭 Comeback Style")
        tone = st.selectbox(
            "What kind of comeback are you aiming for?",
            [
                "Witty and playful",
                "Sarcastic and dry",
                "Savage and bold",
                "Friendly and light",
                "Random and silly"
            ]
        )

    with col2:
        st.subheader("📢 Intensity Level")
        intensity = st.selectbox(
            "How strong should the response be?",
            [
                "Low-key and subtle",
                "Balanced and clever",
                "High-impact and punchy"
            ]
        )

    return {
        "chat_text": chat_text,
        "tone": tone,
        "intensity": intensity
    }

def generate_chat_response(user_inputs: dict) -> str:
    # Prepare the prompt
    chat_snippet = user_inputs["chat_text"]
    tone = user_inputs["tone"]
    intensity = user_inputs["intensity"]

    chat_comeback_agent = Agent(
        name="Chat Comeback Agent",
        model=OpenAIChat(id="gpt-4o", api_key=st.session_state.openai_api_key),
        tools=[GiphyTools(api_key=st.session_state.giphy_api_key)],
        description=dedent("""
            You are a witty conversation assistant. Your job is to interpret a given chat snippet,
            understand the intended tone and intensity, craft a clever comeback message,
            and return the most fitting GIF to go with it.
        """),
        instructions=[
            "Read the user's chat message and comeback preferences (tone and intensity).",
            "Write a short, funny, and clever text-only comeback response.",
            "Summarize the comeback into a **GIF search query no longer than 8–10 words**.",
            "The query must be **brief, expressive, and under 10 words**.",
            "Do **not** include the full chat in the search query — use only the core idea or emotion.",
            "Use the `search_gifs` tool to find the most relevant GIF using this query.",
            "Format the entire output in Markdown as follows:",
            "- Convert the original chat into clean, readable Markdown (e.g., `**Alice**: Hello`, one line per message).",
            "- Append the comeback as a new line in **exactly the same style** as the original chat format (same speaker style and spacing).",
            "- Add a blank line after the comeback.",
            "- Include the GIF in Markdown format on a new line: `![gif](URL)`.",
            "Output only the final Markdown-formatted conversation. Do not include any commentary, reasoning, or explanation."
        ],
        show_tool_calls=True,
        tool_call_limit=3
    )


    comeback_prompt = f"""
    Chat snippet:
    {chat_snippet}

    Comeback tone: {tone}
    Intensity: {intensity}

    Generate a witty comeback based on these inputs.
    """

    updated_chat = chat_comeback_agent.run(comeback_prompt).content

    return updated_chat

def main() -> None:
    # Page config
    st.set_page_config(page_title="Chat Comeback Buddy Bot", page_icon="💬", layout="wide")

    # Custom styling
    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header and intro
    st.markdown("<h1 style='font-size: 2.5rem;'>💬 Chat Comeback Buddy Bot</h1>", unsafe_allow_html=True)
    st.markdown(
        "Welcome to Chat Comeback Buddy Bot — a fun and dynamic Streamlit app that analyzes your chat snippets and delivers clever, humor-filled GIF replies, making it easy to add wit, charm, and personality to every conversation.",
        unsafe_allow_html=True
    )

    render_sidebar()
    user_chat_inputs = render_chat_inputs()

    st.markdown("---")

    if st.button("🎯 Generate Comeback"):
        if not hasattr(st.session_state, "openai_api_key"):
            st.error("Please provide your OpenAI API key in the sidebar.")
        elif not hasattr(st.session_state, "giphy_api_key"):
            st.error("Please provide your Giphy API key in the sidebar.")
        elif not user_chat_inputs["chat_text"].strip():
            st.error("Please paste a chat snippet to respond to.")
        else:
            with st.spinner("Generating a snappy comeback..."):
                updated_chat = generate_chat_response(user_chat_inputs)

                st.session_state.updated_chat = updated_chat

    # Display the response
    if "updated_chat" in st.session_state:
        st.markdown("## 💬 Updated Chat")
        st.markdown(st.session_state.updated_chat, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Comeback Response",
            data=st.session_state.updated_chat,
            file_name="chat_comeback.md",
            mime="text/markdown"
        )

# Run the app
if __name__ == "__main__":
    main()
