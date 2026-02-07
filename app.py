import streamlit as st
import google.generativeai as genai

# ==========================================
# 🔑 EMERGENCY KEY SLOT
# ==========================================
# LEAVE THIS EMPTY. Use Streamlit Secrets instead.
MANUAL_API_KEY = ""

# ==========================================
# 📂 PART 1: THE SYLLABUS VAULT
# ==========================================
SYLLABUS_DB = {
    "Year 6": {
        "Unit 1: It's An Emergency": {
            "Writing": [
                "4.2.3 Narrate factual and imagined events & 2.3.1 Narrate short stories",
                "4.2.1 Give detailed information about themselves & 4.2.2 Spell high frequency words"
            ],
            "Speaking": [
                "2.3.1 Narrate short stories, events and experiences & 3.2.2 Understand specific information",
                "2.1.1 Give detailed information about themselves & 2.1.3 Ask for and give clarification"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words & 3.2.2 Understand specific information",
                "3.3.1 Read and enjoy A2 fiction/non-fiction print and digital texts"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 1.2.1 Understand main idea",
                "1.2.5 Understand more complex supported questions"
            ]
        },
        "Unit 2: Life in the Past": {
            "Reading": ["3.2.2 Understand specific info & 3.2.4 Use dictionary"],
            "Writing": ["4.2.3 Narrate factual events & 4.3.1 Use capital letters"]
        }
    },
    "Year 1": {
        "Unit 0: Friends": {
            "Speaking": [
                "2.1.4 Greet, say goodbye, and express thanks & 2.3.1 Introduce self to an audience using fixed phrases",
                "2.1.1 Give very basic personal information using fixed phrases & 3.1.3 Blend phonemes (CVC, CCVC)",
                "2.3.1 Introduce self to an audience using fixed phrases & 4.3.1 Use capital letters appropriately in personal and place names"
            ],
            "Listening": [
                "1.2.4 Understand short basic supported classroom instructions & 4.1.2 Form letters and words in neat legible print",
                "1.2.2 Understand with support specific information & 2.1.1 Give very basic personal information using fixed phrases",
                "1.2.5 Understand short supported questions & 4.2.1 Give very basic personal information using fixed phrases"
            ],
            "Reading": [
                "3.1.1 Identify and recognise the shapes of the letters in the alphabet & 3.1.2 Recognise and sound out with support beginning, medial and final sounds in a word",
                "3.1.1 Identify and recognise the shapes of the letters & 4.1.2 Form letters and words in neat legible print",
                "3.1.1 Identify and recognise the shapes of the letters & 4.1.2 Form letters and words (i, ii, iii)",
                "3.2.2 Understand specific information and details & 1.2.3 Understand with a high degree of support very short simple narratives"
            ],
            "Writing": [
                "4.1.2 Form letters and words in neat legible print & 3.1.2 Recognise and sound out with support beginning, medial and final sounds",
                "4.1.2 Form letters and words in neat legible print & 2.1.1 Give very basic personal information using fixed phrases",
                "4.1.2 Form letters and words in neat legible print & 3.3.1 Read and enjoy simple print and digital games at word level",
                "4.2.1 Give very basic personal information using fixed phrases & 2.1.5 Name or describe objects using suitable words from word sets"
            ],
            "Language Arts": [
                "5.1.1 Demonstrate appreciation through non-verbal responses",
                "5.1.1 Demonstrate appreciation & 5.1.2 Say the words in simple texts, and sing simple songs",
                "5.1.1 Demonstrate appreciation & 2.1.5 Name or describe objects using suitable words from word sets"
            ]
        },
        "Unit 1: At School": {
            "Listening": [
                "1.2.1 Understand with support the main idea & 2.1.5 Name or describe objects using suitable words",
                "1.3.1 Predict words they will hear & 1.2.4 Understand short basic supported classroom instructions",
                "1.2.3 Understand very short simple narratives & 3.2.1 Understand the main idea of very simple phrases",
                "1.2.1 Understand with support the main idea & 1.2.2 Understand with support specific information",
                "1.2.2 Understand with support specific information & 2.1.1 Give very basic personal information",
                "1.2.2 Understand with support specific information & 1.2.5 Understand short supported questions",
                "1.2.4 Understand short basic supported classroom instructions & 2.2.2 Ask for attention or help"
            ],
            "Speaking": [
                "2.1.5 Name or describe objects & 1.2.2 Understand with support specific information",
                "2.1.4 Greet, say goodbye, and express thanks & 1.2.2 Understand with support specific information",
                "2.1.1 Give very basic personal information & 1.2.5 Understand short supported questions",
                "2.1.4 Greet, say goodbye, and express thanks & 2.2.2 Ask for attention or help",
                "2.1.2 Find out about very basic personal information & 4.2.5 Connect words and proper names using 'and'",
                "2.1.4 Greet, say goodbye, and express thanks & 1.2.4 Understand short basic supported classroom instructions"
            ],
            "Language Arts": [
                "5.2.1 Name people, things or places in illustrations & 5.3.1 Respond imaginatively through creating simple art",
                "5.2.1 Name people, things or places in illustrations & 2.1.5 Name or describe objects",
                "5.1.2 Demonstrate appreciation through non-verbal responses & 5.3.1 Respond imaginatively",
                "5.1.1 Demonstrate appreciation & 5.1.2 Say the words in simple texts",
                "5.3.1 Respond imaginatively & 1.2.4 Understand short basic supported classroom instructions",
                "5.1.1 Demonstrate appreciation & 5.3.1 Respond imaginatively"
            ],
            "Reading": [
                "3.1.3 Blend phonemes (CVC, CCVC) & 4.3.2 Spell familiar high frequency words accurately",
                "3.1.2 Recognise and sound out & 1.1.1 Recognise and reproduce target language sounds",
                "3.1.3 Blend phonemes & 3.1.4 Segment phonemes",
                "3.2.2 Understand specific information & 2.1.5 Name or describe objects",
                "3.1.2 Recognise and sound out & 4.3.2 Spell familiar high frequency words accurately"
            ],
            "Writing": [
                "4.2.2 Greet, say goodbye, and express thanks & 4.2.4 Name or describe objects using suitable words",
                "4.2.4 Name or describe objects & 1.2.4 Understand short basic supported classroom instructions",
                "4.2.2 Greet, say goodbye, and express thanks & 4.3.2 Spell familiar high frequency words accurately",
                "4.3.2 Spell familiar high frequency words accurately & 3.2.1 Understand the main idea",
                "4.3.2 Spell familiar high frequency words accurately & 3.2.2 Understand specific information",
                "4.2.4 Name or describe objects & 3.2.4 Name or describe objects"
            ]
        },
        "Unit 2: Let's Play!": {
            "Speaking": [
                "2.1.5 Name or describe objects & 1.2.1 Understand with support the main idea",
                "2.1.1 Give very basic personal information & 4.2.1 Give very basic personal information",
                "2.1.5 Understand short supported questions (Note: Text check) & 2.2.2 Ask for attention or help",
                "2.1.5 Name or describe objects & 3.2.2 Understand specific information",
                "2.1.3 Express basic likes and dislikes & 2.2.2 Ask for attention or help",
                "2.1.1 Give very basic personal information & 2.2.2 Ask for attention or help"
            ],
            "Reading": [
                "3.2.2 Understand specific information & 2.1.2 Find out about very basic personal information",
                "3.1.3 Blend phonemes & 3.1.4 Segment phonemes",
                "3.2.1 Understand main idea & 1.2.3 Understand very short simple narratives",
                "3.2.3 Use visuals on the page & 4.2.4 Name or describe objects",
                "3.1.2 Recognise and sound out & 1.1.1 Recognise and reproduce target language sounds",
                "3.1.1 Identify and recognise shapes of letters & 3.1.2 Recognise and sound out",
                "3.2.3 Use visuals on the page & 1.2.5 Understand short supported questions"
            ],
            "Language Arts": [
                "5.2.1 Name people, things or places & 1.2.3 Understand very short simple narratives",
                "5.2.1 Name people, things or places & 1.2.2 Understand specific information",
                "5.2.1 Name people, things or places & 4.3.3 Plan and write words and phrases",
                "5.2.1 Name people, things or places & 5.3.1 Respond imaginatively",
                "5.1.1 Demonstrate appreciation & 5.2.1 Name people, things or places"
            ],
            "Listening": [
                "1.2.4 Understand short basic supported instructions & 2.1.5 Name or describe objects",
                "1.2.2 Understand specific information & 1.2.5 Understand short supported questions",
                "1.3.1 Predict words & 1.2.2 Understand specific information",
                "1.2.2 Understand specific information & 3.2.2 Understand specific information",
                "1.2.2 Understand specific information & 2.1.5 Name or describe objects"
            ],
            "Writing": [
                "2.1.3 Express basic likes and dislikes & 2.3.1 Introduce self to an audience",
                "4.2.3 Express basic likes and dislikes & 2.2.2 Ask for attention or help",
                "4.3.2 Spell familiar high frequency words & 3.3.1 Read and enjoy simple print and digital games",
                "4.3.1 Use capital letters appropriately & 3.2.2 Understand specific information",
                "4.2.3 Spell familiar high frequency words accurately & 2.1.3 Express basic likes and dislikes",
                "4.3.2 Use capital letters appropriately & 4.3.3 Spell familiar high frequency words accurately",
                "4.3.2 Use capital letters appropriately & 4.2.1 Give very basic personal information"
            ]
        },
        "Unit 3: Pet Show": {
            "Listening": [
                "1.2.1 Understand with support the main idea & 2.1.5 Name or describe objects",
                "1.2.2 Understand with support specific information & 2.1.5 Name or describe objects"
            ],
            "Language Arts": ["5.3.1 Respond imaginatively & 4.2.4 Name or describe objects"],
            "Speaking": ["2.1.2 Find out personal info & 2.1.3 Express basic likes and dislikes"],
            "Reading": ["3.1.3 Blend phonemes & 3.3.1 Read and enjoy simple print and digital games"]
        }
    }
}

# ==========================================
# 🤖 PART 2: THE AI INSTRUCTIONS (MR REYY'S ASSISTANT)
# ==========================================

SYSTEM_PROMPT = """
ACT AS: Mr Reyy's Assistant (An efficient, practical Malaysian English Teacher's aide).
TONE: Professional, concise, and ready to copy-paste.

**INSTRUCTIONS FOR OUTPUT:**

1. **INTRODUCTION:**
   - Start exactly with: "Good day teacher! I'm Mr Reyy's assistant. Let's make learning {TOPIC_KEYWORD}, in the best possible way!" 
   - (Replace {TOPIC_KEYWORD} with the main topic of the unit selected).

2. **OBJECTIVES (Clean & Simple):**
   - Format exactly like this:
     "By the end of the lesson, pupils will be able to:"
     
     **1.** [Main Objective - SMART]
     
     **2.** [Complementary Objective - SMART]
   - Use **bold numbers** manually typed out (e.g., **1.**).
   - Leave an empty line between objectives.

3. **LESSON STEPS (CRITICAL FORMATTING - COPY/PASTE FRIENDLY):**
   - **NO PARAGRAPHS:** Never group steps together.
   - **NUMBERING:** Use **bold numbers** manually typed out (e.g., **1.**) followed by the step.
   - **SPACING:** You MUST leave an empty line between every step.
   - **DIFFERENTIATION/SAMPLES:** Must be on a NEW LINE with an empty line before them.
   - Restart numbering at '1.' for EACH section.
   
   **Strict Layout Template:**

   **Pre-Lesson**
   
   **1.** [Step 1 instruction]
   
   **2.** [Step 2 instruction]

   **Lesson Delivery**
   
   **1.** [Step 1 instruction]
   
   **2.** [Step 2 instruction]
   
   **3.** [Step 3 instruction]
      
      * *Sample:* "..."
   
   **4.** [Step 4 instruction]
      
      * **Advanced:** ...
      
      * **Remedial:** ...

   **Post-Lesson**
   
   **1.** [Step 1 instruction]
   
   **2.** [Step 2 instruction]

4. **NO TEXTBOOKS:** Original activities only.
"""

# ==========================================
# 🖥️ PART 3: THE WEB APP INTERFACE
# ==========================================

st.set_page_config(page_title="MY CEFR Planner", page_icon="🇲🇾", layout="wide")

st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #2563EB;
        color: white;
        height: 3em;
        border-radius: 10px;
    }
    .main .block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🇲🇾 Lesson Details")
    
    # API KEY LOGIC (PRIORITY: Manual -> Secrets -> Input Box)
    api_key = MANUAL_API_KEY
    if not api_key:
        api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        api_key = st.text_input("Gemini API Key", type="password")

    # Debug Status
    if api_key:
        st.success("API Key Loaded ✅")
    else:
        st.warning("API Key Missing ❌")

    # SELECTION LOGIC
    year_options = list(SYLLABUS_DB.keys())
    selected_year = st.selectbox("1. Class Level", year_options)

    unit_options = list(SYLLABUS_DB[selected_year].keys())
    selected_unit = st.selectbox("2. Topic / Unit", unit_options)

    skill_options = list(SYLLABUS_DB[selected_year][selected_unit].keys())
    selected_skill = st.selectbox("3. Focus Skill", skill_options)

    ls_options = SYLLABUS_DB[selected_year][selected_unit][selected_skill]
    selected_ls = st.selectbox("4. Learning Standards", ls_options)

    notes = st.text_area("Teacher's Remarks", placeholder="e.g., Focus on simple SVO sentences.")
    
    generate_btn = st.button("✨ Generate Lesson Plan")

st.title(f"{selected_unit}")
st.caption(f"Class: {selected_year} | Skill: {selected_skill} | Standard: {selected_ls}")
st.divider()

if generate_btn:
    if not api_key:
        st.error("Please enter your API Key to proceed.")
    else:
        genai.configure(api_key=api_key)
        
        full_prompt = f"""
        {SYSTEM_PROMPT}
        
        **CONTEXT:**
        - **Class:** {selected_year}
        - **Unit:** {selected_unit}
        - **Skill:** {selected_skill}
        - **Standard:** {selected_ls}
        - **Notes:** {notes}
        
        GENERATE THE LESSON PLAN NOW.
        """
        
        with st.spinner("🤖 Writing a clean, practical plan..."):
            try:
                available_model = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        available_model = m.name
                        if 'flash' in m.name or 'pro' in m.name:
                            break 
                
                if available_model:
                    model = genai.GenerativeModel(available_model)
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.success(f"Generated by Mr Reyy's Assistant ({available_model})")
                else:
                    st.error("❌ No available AI models found for this key.")
            
            except Exception as e:
                st.error("❌ Connection Failed. Check API Key.")
                st.warning(f"Error: {e}")
