```python
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS - SOFT LAVENDER THEME
# ============================================================
custom_css = """
<style>
/* Overall app background */
.stApp {
    background-color: #F5F2FB;
}

/* Main title styling */
.main-title {
    text-align: center;
    color: #4B3B6B;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}

/* Subtitle styling */
.sub-title {
    text-align: center;
    color: #7A6B99;
    font-size: 1.3rem;
    font-weight: 400;
    margin-bottom: 1.5rem;
}

/* Description box */
.description-box {
    background-color: #EDE7F6;
    border-radius: 14px;
    padding: 1.3rem 1.8rem;
    color: #4B3B6B;
    font-size: 1.05rem;
    line-height: 1.6rem;
    border: 1px solid #D8CCF0;
    margin-bottom: 2rem;
}

/* Section headers */
.section-header {
    color: #4B3B6B;
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 2.2rem;
    margin-bottom: 1rem;
    border-left: 5px solid #B8A4E3;
    padding-left: 0.7rem;
}

/* Agent card styling */
.agent-card {
    background-color: #FFFFFF;
    border: 1px solid #E0D4F7;
    border-radius: 16px;
    padding: 1.5rem 1.2rem;
    text-align: center;
    box-shadow: 0 3px 10px rgba(150, 120, 200, 0.12);
    height: 220px;
    transition: transform 0.2s ease-in-out;
}

.agent-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(150, 120, 200, 0.22);
}

.agent-icon {
    font-size: 2.3rem;
    margin-bottom: 0.5rem;
}

.agent-title {
    color: #4B3B6B;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

.agent-desc {
    color: #6B5B8A;
    font-size: 0.92rem;
    line-height: 1.3rem;
}

/* Feature card styling */
.feature-card {
    background-color: #F3EEFC;
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
    border: 1px solid #DCCBF5;
    height: 130px;
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 0.4rem;
}

.feature-text {
    color: #4B3B6B;
    font-weight: 600;
    font-size: 1rem;
}

/* Footer styling */
.footer-text {
    text-align: center;
    color: #9A8CB5;
    font-size: 0.85rem;
    margin-top: 3rem;
    padding-bottom: 1rem;
}

/* Custom button styling */
div.stButton > button {
    background-color: #B8A4E3;
    color: white;
    font-weight: 700;
    font-size: 1.05rem;
    border-radius: 10px;
    padding: 0.6rem 1.5rem;
    border: none;
    width: 100%;
    transition: background-color 0.2s ease-in-out;
}

div.stButton > button:hover {
    background-color: #9C82D4;
    color: white;
}

/* Text input styling */
div.stTextInput > div > div > input {
    border-radius: 10px;
    border: 1px solid #D8CCF0;
    padding: 0.6rem;
}
</style>
"""

# Inject the custom CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)

# ============================================================
# HEADER SECTION - TITLE & SUBTITLE
# ============================================================
st.markdown('<div class="main-title">📚 StudyMate AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your AI-powered study companion</div>', unsafe_allow_html=True)

# ============================================================
# PROJECT DESCRIPTION SECTION
# ============================================================
st.markdown(
    """
    <div class="description-box">
    StudyMate AI is a <b>multi-agent educational assistant</b> built to help students learn more
    efficiently. Instead of relying on a single AI model, StudyMate AI uses a team of specialized
    agents that work together — one agent explains concepts in simple terms, another generates
    quizzes to test your understanding, and another builds a personalized study plan tailored to
    your goals. Simply enter a topic below, and let the agents handle the rest!
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TOPIC INPUT & GENERATE BUTTON SECTION
# ============================================================
# Use columns to center the input and button for a clean layout
input_col1, input_col2, input_col3 = st.columns([1, 3, 1])

with input_col2:
    # Text input for the topic the student wants to learn
    topic = st.text_input("Enter a topic you want to learn", placeholder="e.g. Newton's Laws of Motion")

    # Button to trigger the (future) multi-agent pipeline
    generate_clicked = st.button("🚀 Generate Learning Package")

    # Simple placeholder feedback when the button is clicked
    if generate_clicked:
        if topic.strip() == "":
            st.warning("Please enter a topic before generating your learning package.")
        else:
            st.success(f"Great! Your AI agents are preparing a learning package for: **{topic}**")

# ============================================================
# "MEET YOUR AI AGENTS" SECTION
# ============================================================
st.markdown('<div class="section-header">🤖 Meet Your AI Agents</div>', unsafe_allow_html=True)

# Create four columns, one for each agent card
agent_col1, agent_col2, agent_col3, agent_col4 = st.columns(4)

# Coordinator Agent Card
with agent_col1:
    st.markdown(
        """
        <div class="agent-card">
            <div class="agent-icon">🎯</div>
            <div class="agent-title">Coordinator Agent</div>
            <div class="agent-desc">Routes user requests to the appropriate agent.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Explainer Agent Card
with agent_col2:
    st.markdown(
        """
        <div class="agent-card">
            <div class="agent-icon">📖</div>
            <div class="agent-title">Explainer Agent</div>
            <div class="agent-desc">Provides beginner-friendly explanations and examples.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Quiz Agent Card
with agent_col3:
    st.markdown(
        """
        <div class="agent-card">
            <div class="agent-icon">📝</div>
            <div class="agent-title">Quiz Agent</div>
            <div class="agent-desc">Generates quizzes and practice questions.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Study Planner Agent Card
with agent_col4:
    st.markdown(
        """
        <div class="agent-card">
            <div class="agent-icon">📅</div>
            <div class="agent-title">Study Planner Agent</div>
            <div class="agent-desc">Creates personalized learning roadmaps and study schedules.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# "FEATURES" SECTION
# ============================================================
st.markdown('<div class="section-header">✨ Features</div>', unsafe_allow_html=True)

# Create four columns, one for each feature highlight
feature_col1, feature_col2, feature_col3, feature_col4 = st.columns(4)

with feature_col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-text">Concept Explanations</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-text">Quiz Generation</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🗓️</div>
            <div class="feature-text">Personalized Study Plans</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🕸️</div>
            <div class="feature-text">Multi-Agent Architecture</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FOOTER SECTION
# ============================================================
st.markdown(
    '<div class="footer-text">Built with ❤️ using Streamlit | StudyMate AI — Kaggle Capstone Project</div>',
    unsafe_allow_html=True
)
```
