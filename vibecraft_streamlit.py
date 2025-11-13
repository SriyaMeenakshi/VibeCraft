import streamlit as st
import google.generativeai as genai
import requests

# ------------------- SETUP -------------------
st.set_page_config(page_title=" VIBECRAFT ", page_icon="✨", layout="centered")

# ---------- Session State Initialization ----------
if "current_vibe" not in st.session_state:
    st.session_state.current_vibe = ""
if "profile" not in st.session_state:
    st.session_state.profile = ""
if "image_url" not in st.session_state:
    st.session_state.image_url = ""

# ---------- Gemini Setup ----------
import os
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("⚠️ API Key Required: Please set your GEMINI_API_KEY environment variable to use this app.")
    st.stop()

genai.configure(api_key=API_KEY)

# ---------- Custom CSS ----------
st.markdown("""
<style>
/* 🌌 Modern Neon Dark Theme */

html, body, [class*="css"] {
    background: #0d0f1a;
    color: #e0e0e0;
    font-family: 'Poppins', sans-serif;
}

/* ✨ Title */
.main-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(90deg, #8b5cf6, #ec4899, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 15px rgba(139, 92, 246, 0.6), 0 0 25px rgba(236, 72, 153, 0.5);
    margin-top: 1rem;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #9ca3af;
    margin-bottom: 2rem;
}

/* Text Area */
textarea {
    background-color: rgba(30, 30, 50, 0.95) !important;
    color: #f0f0f0 !important;
    border: 1px solid #8b5cf6 !important;
    border-radius: 0.8rem !important;
    box-shadow: 0 0 10px rgba(139, 92, 246, 0.3);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #8b5cf6, #ec4899);
    color: white;
    border: none;
    border-radius: 1rem;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(236, 72, 153, 0.6);
    background: linear-gradient(135deg, #06b6d4, #ec4899);
}

/* Cards */
.stCard, [class*="stCard"] {
    background: rgba(20, 20, 40, 0.7) !important;
    border-radius: 1rem !important;
    padding: 1.5rem !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Headings */
h2, h3, h4 {
    color: #ec4899 !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 0.9rem;
    margin-top: 3rem;
}

/* Dividers */
hr {
    border: 1px solid rgba(139, 92, 246, 0.3);
}
</style>
""", unsafe_allow_html=True)



# ------------------- FUNCTIONS -------------------

def generate_personality(vibe_text):
    """Generate a personality profile using Gemini"""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""You are a personality designer AI. Generate a creative personality and aesthetic style 
        for the following description: '{vibe_text}'.
        Format response with:
        1. Personality Profile
        2. Aesthetic Style
        3. Recommended Tone of Communication
        4. Poetic Line."""
        response = model.generate_content(prompt)
        st.session_state.profile = response.text
    except Exception as e:
        st.error(f"❌ Gemini API Error: {e}")

def generate_image(vibe_text):
    """Generate an aesthetic image using Pollinations AI"""
    try:
        prompt = vibe_text.replace(" ", "%20")
        img_url = f"https://image.pollinations.ai/prompt/{prompt}?width=512&height=512"
        st.session_state.image_url = img_url
    except Exception as e:
        st.error(f"❌ Image generation failed: {e}")

# ------------------- FRONTEND -------------------

st.title("✨ VIBECRAFT ✨")
st.markdown("_Design a personality. Visualize a vibe._")

# Vibe Options
preset_vibes = [
    "Soft-spoken artist who loves chaos",
    "Curious student with innovative mind",
    "Bold leader with quiet strength",
    "Dreamer lost in the digital age",
    "Analytical thinker with poetic soul"
]

# Dropdown
selected_vibe = st.selectbox("🎭 Choose a vibe preset (or type your own):", [""] + preset_vibes)

# Textbox
vibe_input = st.text_area("💡 Describe a vibe or personality:", 
    value=st.session_state.current_vibe if not selected_vibe else selected_vibe,
    placeholder="Type something like 'Mysterious coder who speaks in metaphors'...")

# Update current vibe
st.session_state.current_vibe = vibe_input.strip()

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🎨 Generate Personality", key="gen_persona"):
        if st.session_state.current_vibe:
            generate_personality(st.session_state.current_vibe)
        else:
            st.warning("Please enter or select a vibe first!")

with col2:
    if st.button("🖼 Generate Image", key="gen_image"):
        if st.session_state.current_vibe:
            generate_image(st.session_state.current_vibe)
        else:
            st.warning("Please enter or select a vibe first!")

# Display Results
if st.session_state.profile:
    st.markdown("## 🧠 Personality Profile")
    st.markdown(st.session_state.profile)

if st.session_state.image_url:
    st.markdown("## 🎨 Vibe Visualization")
    st.image(st.session_state.image_url, use_container_width=True)

st.markdown("---")
st.markdown("🚀 _Powered by Gemini × Pollinations AI_")

