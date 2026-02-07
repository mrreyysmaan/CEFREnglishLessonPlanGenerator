import streamlit as st
import google.generativeai as genai

# ==========================================
# 📂 PART 1: THE SYLLABUS VAULT (PASTE YOUR DATA HERE)
# ==========================================
# This is where you paste your SOW. 
# FORMAT: "Year": { "Unit": { "Skill": [ "Learning Standards" ] } }

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
        "Unit 1: Friends": {
            "Listening": ["1.1.1 Recognise and reproduce target language sounds & 1.2.1 Understand meaning"],
            "Speaking": ["2.1.1 Give very basic personal information & 2.1.5 Name or describe objects"]
        },
        "Unit 2: At School": {
            "Reading": ["3.1.1 Identify and recognise the shapes of the letters & 3.1.2 Recognise and sound out"],
            "Writing": ["4.1.2 copy letters and familiar high frequency words"]
        }
    }
    # You can copy-paste more years here following the same curly bracket pattern
}

# ==========================================
# 🤖 PART 2: THE AI INSTRUCTIONS (THE BRAIN)
# ==========================================

SYSTEM_PROMPT = """
ACT AS: A Guru Cemerlang (Expert Malaysian English Teacher).
TASK: Create a highly detailed, student-centered CEFR Lesson Plan.

STRICT CONSTRAINTS:
1. **3 STAGES:** Structure into Pre-Lesson, Lesson Delivery, and Post-Lesson.
2. **DETAILED NUMBERED STEPS:** Do NOT write summaries. Write "1. Pupils do X... 2. Teacher says Y...".
3. **STUDENT-CENTERED:** Focus on what pupils DO (e.g., "Pupils pair up...", "Pupils interview...").
4. **NO TEXTBOOKS:** Create original activities using the Learning Standards provided.
5. **OBJECTIVES:** SMART objectives must relate specifically to the UNIT topic.

FORMATTING OUTPUT (Markdown):

## 🎯 Learning Objectives
(Provide 2 tiers: Main & Complementary based on the LS)

## 🧩 Pre-Lesson (Induction)
(Numbered steps for a warm-up game/activity)

## 🚀 Lesson Delivery (The Core)
(Numbered steps 1-10. This must be the longest section. Include specific examples of sentences/dialogue pupils will practice.)

### 🛠️ Differentiation Strategy
* **For Advanced (Cemerlang):** (Specific challenge based on the activity above)
* **For Remedial (Pemulihan):** (Specific support/scaffolding based on the activity above)

## 📝 Post-Lesson (Closure)
(Numbered steps for reflection/exit ticket)

## 📊 PBD Assessment Guide
* **Observation Focus:** (What exactly to watch for during the main activity)
"""

# ==========================================
# 🖥️ PART 3: THE WEB APP INTERFACE
# ==========================================

st.set_page_config(page_title="MY CEFR Planner", page_icon="🇲🇾", layout="wide")

# Custom CSS to make it look like the preview
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

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("🇲🇾 Lesson Details")
    
    # 1. API Key (Auto-detects from secrets or asks user)
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        api_key = st.text_input("Gemini API Key", type="password")

    # 2. Year Selection
    year_options = list(SYLLABUS_DB.keys())
    selected_year = st.selectbox("1. Class Level", year_options)

    # 3. Unit Selection (Updates based on Year)
    unit_options = list(SYLLABUS_DB[selected_year].keys())
    selected_unit = st.selectbox("2. Topic / Unit", unit_options)

    # 4. Skill Selection (Updates based on Unit)
    skill_options = list(SYLLABUS_DB[selected_year][selected_unit].keys())
    selected_skill = st.selectbox("3. Focus Skill", skill_options)

    # 5. LS Selection (Updates based on Skill)
    ls_options = SYLLABUS_DB[selected_year][selected_unit][selected_skill]
    selected_ls = st.selectbox("4. Learning Standards", ls_options)

    # 6. Remarks
    notes = st.text_area("Teacher's Remarks", placeholder="e.g., Focus on simple SVO sentences.")
    
    generate_btn = st.button("✨ Generate Lesson Plan")

# --- MAIN PAGE DISPLAY ---
st.title(f"{selected_unit}")
st.caption(f"Class: {selected_year} | Skill: {selected_skill} | Standard: {selected_ls}")
st.divider()

if generate_btn:
    if not api_key:
        st.error("Please enter your API Key to proceed.")
    else:
        # Connect to Gemini
        genai.configure(api_key=api_key)
        
        # The Prompt that combines your Rules + User Selection
        full_prompt = f"""
        {SYSTEM_PROMPT}
        
        **LESSON CONTEXT:**
        - **Class:** {selected_year}
        - **Unit/Topic:** {selected_unit}
        - **Focus Skill:** {selected_skill}
        - **Learning Standards:** {selected_ls}
        - **Teacher Notes:** {notes}
        
        GENERATE THE FULL LESSON PLAN NOW.
        """
        
        with st.spinner("🤖 Consulting the syllabus... Creating detailed steps..."):
            try:
                # Try the newest, fastest model first
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.success("Generated with Gemini Flash! (Fastest)")
                
            except Exception as e:
                # If 'Flash' is not found (404), switch to 'Pro' automatically
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.success("Generated with Gemini Pro! (Reliable Backup)")
                except Exception as e2:
                    st.error(f"Error: {e2}")
                    st.info("Check your API key. If you just created it, wait 5 minutes.")
