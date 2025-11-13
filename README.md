# ✨ VibeCraft - AI Personality Designer

VibeCraft is a **Streamlit web application** that generates **personalized personality profiles, visual aesthetics, and moodboards** from user-described vibes using **Google Gemini API** and **Pollinations AI**.

---

## **🌟 Features**

- Generate detailed personality profiles:
  - Core traits, quirks, mindset
  - Tone of communication (voice, energy, feel)
  - Poetic summary line capturing personality essence
- Visual aesthetics:
  - Color palette visualization
  - AI-generated moodboard image
  - AI avatar portrait
- Interactive examples and text input
- Modern **dark neon/glowing UI** for better user experience

---

## **🛠️ Technical Stack**

- **Frontend**: Streamlit (dark theme + custom CSS for glowing effects)
- **Backend AI**:
  - [Google Gemini API](https://aistudio.google.com/) for personality generation
  - [Pollinations AI](https://pollinations.ai/) for free moodboard/visual generation
- **Python Libraries**:
  - `streamlit`, `google-generativeai`, `matplotlib`, `Pillow`, `requests`

---

## **⚡ Installation**

1. Clone the repository:
 ```bash
git clone https://github.com/<your-username>/VibeCraft.git
cd VibeCraft
```
2.Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```
4.Set your Gemini API Key:
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Windows CMD
set GEMINI_API_KEY=your-api-key-here

# Mac/Linux
export GEMINI_API_KEY="your-api-key-here"
```
5.Run the app:

```bash
streamlit run vibecraft_streamlit.py
```
## 🧩 How it works

1. **Input Vibe**  
   Type a description (or select an example) in the text area.

2. **Generate Personality**  
   Click the button to send the description to **Google Gemini**.

3. **Receive Profile**  
   AI generates JSON containing:  
   - Archetype  
   - Traits  
   - Tone  
   - Strengths  
   - Motivations  
   - Color Palette  
   - Moodboard prompt  
   - Avatar style & voice tone

4. **Generate Images**  
   Pollinations AI renders the moodboard and avatar images.

5. **Display**  
   Streamlit shows:  
   - Personality details  
   - Color palette as visual swatches  
   - Moodboard and avatar images
  
     ## 🎨 Customization

- **Dark Theme with Neon/Glow Accents**  
  Provides a modern, visually striking interface for users.  

- **Color Palette Visualization**  
  Personality color palettes are rendered as visual swatches using **Matplotlib**.  

- **Glowing VibeCraft Logo**  
  The app features a central glowing logo for a unique branding experience.  

- **Background Gradients**  
  Background gradients can be easily adjusted via custom CSS for a dynamic look.
  
## 💡 Future Improvements

- Replace Pollinations with higher-fidelity image generation  
- Add voice tone playback  
- Add dynamic background animations  
- Save profiles as PDF/PNG  
- Multi-language support  

---

### 👤 Author

**Sriya Meenakshi Chalamalasetty**  
Made this project for Nerds Vibeathon 2025
GitHub: [https://github.com/SriyaMeenakshi](https://github.com/SriyaMeenakshi)  
