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
    "Year 1": {
        "Unit 0: Friends (World of Self, Family and Friends)": {
            "Speaking": [
                "2.1.4 Greet, say goodbye, and express thanks & 2.3.1 Introduce self to an audience",
                "2.1.1 Give very basic personal information & 3.1.3 Blend phonemes (CVC, CCVC)",
                "2.3.1 Introduce self to an audience & 4.3.1 Use capital letters in names"
            ],
            "Listening": [
                "1.2.4 Understand short basic supported classroom instructions & 4.1.2 Form letters and words",
                "1.2.2 Understand with support specific information & 2.1.1 Give very basic personal information",
                "1.2.5 Understand short supported questions & 4.2.1 Give very basic personal information"
            ],
            "Reading": [
                "3.1.1 Identify and recognise shapes of letters & 3.1.2 Recognise and sound out sounds",
                "3.1.1 Identify and recognise shapes of letters & 4.1.2 Form letters and words",
                "3.2.2 Understand specific information & 1.2.3 Understand very short simple narratives"
            ],
            "Writing": [
                "4.1.2 Form letters and words & 3.1.2 Recognise and sound out sounds",
                "4.1.2 Form letters and words & 2.1.1 Give very basic personal information",
                "4.1.2 Form letters and words & 3.3.1 Read and enjoy simple games at word level",
                "4.2.1 Give very basic personal information & 2.1.5 Name or describe objects"
            ],
            "Language Arts": [
                "5.1.1 Demonstrate appreciation (chants/raps) & 5.1.2 Say words in simple texts",
                "5.1.1 Demonstrate appreciation (chants/raps) & 2.1.5 Name or describe objects"
            ]
        },
        "Unit 1: At School (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.1 Understand main idea & 2.1.5 Name or describe objects",
                "1.3.1 Predict words & 1.2.4 Understand instructions",
                "1.2.3 Understand narratives & 3.2.1 Understand main idea",
                "1.2.1 Understand main idea & 1.2.2 Understand specific information",
                "1.2.2 Understand specific information & 2.1.1 Give personal info",
                "1.2.2 Understand specific information & 1.2.5 Understand questions",
                "1.2.4 Understand instructions & 2.2.2 Ask for attention or help"
            ],
            "Speaking": [
                "2.1.5 Name or describe objects & 1.2.2 Understand specific information",
                "2.1.4 Greet/Thanks & 1.2.2 Understand specific information",
                "2.1.1 Give personal info & 1.2.5 Understand questions",
                "2.1.4 Greet/Thanks & 2.2.2 Ask for attention or help",
                "2.1.2 Find out personal info & 4.2.5 Connect words with 'and'",
                "2.1.4 Greet/Thanks & 1.2.4 Understand instructions"
            ],
            "Language Arts": [
                "5.2.1 Name items in illustrations & 5.3.1 Respond imaginatively (art/craft)",
                "5.2.1 Name items in illustrations & 2.1.5 Name or describe objects",
                "5.1.2 Say words in simple texts & 5.3.1 Respond imaginatively",
                "5.1.1 Demonstrate appreciation & 5.1.2 Say words in simple texts",
                "5.3.1 Respond imaginatively & 1.2.4 Understand instructions",
                "5.1.1 Demonstrate appreciation & 5.3.1 Respond imaginatively"
            ],
            "Reading": [
                "3.1.3 Blend phonemes & 4.3.2 Spell high frequency words",
                "3.1.2 Sound out sounds & 1.1.1 Recognise phonemes",
                "3.1.3 Blend phonemes & 3.1.4 Segment phonemes",
                "3.2.2 Understand specific info & 2.1.5 Name or describe objects",
                "3.1.2 Sound out sounds & 4.3.2 Spell high frequency words"
            ],
            "Writing": [
                "4.2.2 Greet/Thanks & 4.2.4 Name or describe objects",
                "4.2.4 Name or describe objects & 1.2.4 Understand instructions",
                "4.2.2 Greet/Thanks & 4.3.2 Spell high frequency words",
                "4.3.2 Spell high frequency words & 3.2.1 Understand main idea",
                "4.3.2 Spell high frequency words & 3.2.2 Understand specific info",
                "4.2.4 Name or describe objects & 3.2.4 Name or describe objects"
            ]
        },
        "Unit 2: Let's Play! (World of Stories)": {
            "Speaking": [
                "2.1.5 Name or describe objects & 1.2.1 Understand main idea",
                "2.1.1 Give personal info & 4.2.1 Give personal info",
                "2.1.5 Understand questions & 2.2.2 Ask for attention or help",
                "2.1.5 Name or describe objects & 3.2.2 Understand specific info",
                "2.1.3 Express likes/dislikes & 2.2.2 Ask for attention or help",
                "2.1.1 Give personal info & 2.2.2 Ask for attention or help"
            ],
            "Reading": [
                "3.2.2 Understand specific info & 2.1.2 Find out personal info",
                "3.1.3 Blend phonemes & 3.1.4 Segment phonemes",
                "3.2.1 Understand main idea & 1.2.3 Understand narratives",
                "3.2.3 Use visuals & 4.2.4 Name or describe objects",
                "3.1.2 Sound out sounds & 1.1.1 Recognise phonemes",
                "3.1.1 Recognise letter shapes & 3.1.2 Sound out sounds",
                "3.2.3 Use visuals & 1.2.5 Understand questions"
            ],
            "Language Arts": [
                "5.2.1 Name items in illustrations & 1.2.3 Understand narratives",
                "5.2.1 Name items in illustrations & 1.2.2 Understand specific info",
                "5.2.1 Name items in illustrations & 4.3.3 Plan and write words",
                "5.2.1 Name items in illustrations & 5.3.1 Respond imaginatively",
                "5.1.1 Demonstrate appreciation & 5.2.1 Name items in illustrations"
            ],
            "Listening": [
                "1.2.4 Understand instructions & 2.1.5 Name or describe objects",
                "1.2.2 Understand specific info & 1.2.5 Understand questions",
                "1.3.1 Predict words & 1.2.2 Understand specific info",
                "1.2.2 Understand specific info & 3.2.2 Understand specific info",
                "1.2.2 Understand specific info & 2.1.5 Name or describe objects"
            ],
            "Writing": [
                "2.1.3 Express likes/dislikes & 2.3.1 Introduce self",
                "4.2.3 Express likes/dislikes & 2.2.2 Ask for attention or help",
                "4.3.2 Spell high frequency words & 3.3.1 Read simple games",
                "4.3.1 Use capital letters & 3.2.2 Understand specific info",
                "4.2.3 Spell high frequency words & 2.1.3 Express likes/dislikes",
                "4.3.2 Use capital letters & 4.3.3 Spell high frequency words",
                "4.3.2 Use capital letters & 4.2.1 Give personal info"
            ]
        },
        "Unit 3: Pet Show (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand main idea & 2.1.5 Name or describe objects",
                "1.2.2 Understand specific info & 2.1.5 Name or describe objects"
            ],
            "Language Arts": ["5.3.1 Respond imaginatively & 4.2.4 Name or describe objects"],
            "Speaking": ["2.1.2 Find out personal info & 2.1.3 Express likes/dislikes"],
            "Reading": ["3.1.3 Blend phonemes & 3.3.1 Read simple games"]
        },
        "Unit 4: Lunchtime (World of Knowledge)": {
            "Speaking": [
                "2.1.5 Name or describe objects & 1.2.1 Understand main idea",
                "2.1.5 Name or describe objects & 3.2.2 Understand specific info",
                "2.1.2 Find out personal info & 1.2.2 Understand specific info",
                "2.1.4 Greet, say goodbye & 1.2.5 Understand short supported questions",
                "2.1.3 Express likes/dislikes & 3.3.1 Read simple games",
                "2.1.2 Find out personal info & 1.2.5 Understand short supported questions",
                "2.1.1 Give personal info & 3.2.3 Use visuals",
                "2.1.5 Name or describe objects & 1.2.5 Understand short supported questions",
                "2.1.1 Give personal info & 1.2.2 Understand specific info"
            ],
            "Reading": [
                "3.2.3 Use visuals & 2.1.1 Give personal info",
                "3.2.1 Understand main idea & 3.2.2 Understand specific info",
                "3.2.2 Understand specific info & 1.1.1 Recognise phonemes",
                "3.1.3 Blend phonemes & 4.3.2 Spell high frequency words",
                "3.2.3 Use visuals & 2.1.1 Give personal info",
                "3.2.2 Understand specific info & 2.1.4 Greet, say goodbye",
                "3.2.4 Use picture dictionary & 2.1.1 Give personal info",
                "3.2.2 Understand specific info & 2.1.5 Name or describe objects",
                "3.3.1 Read simple games & 3.2.3 Use visuals"
            ],
            "Listening": [
                "1.2.2 Understand specific info & 1.2.2 Understand specific info",
                "1.2.4 Understand instructions & 2.1.5 Name or describe objects",
                "1.2.2 Understand specific info & 3.2.1 Understand main idea",
                "1.3.1 Predict words & 1.2.2 Understand specific info",
                "1.2.2 Understand specific info & 4.3.2 Spell high frequency words",
                "1.2.1 Understand main idea & 1.2.2 Understand specific info",
                "1.3.1 Predict words & 1.2.2 Understand specific info",
                "1.2.5 Understand short supported questions & 2.1.5 Name or describe objects",
                "1.2.5 Understand short supported questions & 2.1.2 Find out personal info"
            ],
            "Language Arts": [
                "5.1.1 Demonstrate appreciation & 1.2.1 Understand main idea",
                "5.2.1 Name items in illustrations & 4.3.2 Spell high frequency words",
                "5.2.1 Name items in illustrations & 1.2.3 Understand narratives",
                "5.2.1 Name items in illustrations & 2.1.4 Greet, say goodbye",
                "5.2.1 Name items in illustrations & 1.3.1 Predict words",
                "5.2.1 Name items in illustrations & 3.1.3 Blend phonemes",
                "5.2.1 Name items in illustrations & 1.2.3 Understand narratives",
                "5.3.1 Respond imaginatively & 2.3.1 Introduce self",
                "5.3.1 Respond imaginatively & 2.3.1 Introduce self"
            ],
            "Writing": [
                "4.3.2 Spell high frequency words & 4.3.3 Plan and write words",
                "4.3.3 Plan and write words & 4.3.2 Spell high frequency words",
                "4.3.2 Spell high frequency words & 3.1.3 Blend phonemes",
                "4.3.2 Spell high frequency words & 3.3.1 Read simple games",
                "4.3.3 Plan and write words & 4.2.5 Connect words with 'and'",
                "4.2.1 Give personal info & 3.2.2 Understand specific info",
                "4.2.5 Connect words with 'and' & 3.2.2 Understand specific info",
                "4.3.2 Spell high frequency words & 3.2.3 Use visuals"
            ]
        }
    },
    "Year 2": {
        "Unit 0: Introduction (World of Self, Family and Friends)": {
            "Writing": [
                "4.2.1 Ask for and give basic personal information using basic questions and statements & 2.3.1 Introduce self and others to an audience using fixed phrases"
            ]
        },
        "Unit 5: Free Time (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of simple sentences & 2.1.1 Give simple personal information using basic statements",
                "1.2.2 Understand with support specific information and details of simple sentences & 2.1.1 Give simple personal information using basic statements",
                "1.2.3 Understand with support very short simple narratives & 1.2.2 Understand with support specific information and details of simple sentences",
                "1.2.2 Understand with support specific information and details of simple sentences & 3.1.1 Identify, recognise and name the letters of the alphabet",
                "1.2.3 Understand with support very short simple narratives & 1.2.4 Understand an increased range of short basic supported classroom instructions"
            ],
            "Speaking": [
                "2.1.1 Give simple personal information using basic statements & 1.2.1 Understand with support the main idea of simple sentences",
                "2.1.1 Give simple personal information using basic statements & 1.2.2 Understand with support specific information and details of simple sentences",
                "2.1.1 Give simple personal information using basic statements & 2.1.2 Find out about personal information by asking basic questions",
                "2.1.1 Give simple personal information using basic statements & 4.2.1 Ask for and give basic personal information using basic questions and statements",
                "2.1.2 Find out about personal information by asking basic questions & 2.1.1 Give simple personal information using basic statements"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of simple sentences & 1.2.1 Understand with support the main idea of simple sentences",
                "3.1.2 Recognise and sound out with some support beginning, medial and final sounds in a word & 3.1.1 Identify, recognise and name the letters of the alphabet",
                "3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV) & 1.1.1 Recognise and reproduce with support a range of high frequency target language phonemes",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.3 i) Reread a word, phrase or sentence to understand meaning",
                "3.2.2 Understand specific information and details of simple sentences & 2.1.2 Find out about personal information by asking basic questions"
            ],
            "Language Arts": [
                "5.2.1 Name people, things, actions, or places of interest in texts & 1.2.1 Understand with support the main idea of simple sentences",
                "5.2.1 Name people, things, actions, or places of interest in texts & 2.1.3 Give a short sequence of basic instructions",
                "5.1.2 Say the words in simple texts, and sing simple songs & 3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV)",
                "5.1.2 Say the words in simple texts, and sing simple songs & 4.2.1 Ask for and give basic personal information using basic questions and statements",
                "5.1.1 Demonstrate appreciation through nonverbal responses & 1.2.1 Understand with support the main idea of simple sentences"
            ],
            "Writing": [
                "4.3.3 Plan, draft and write simple sentences & 4.2.1 Ask for and give basic personal information using basic questions and statements",
                "4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level & 1.2.2 Understand with support specific information and details of simple sentences",
                "4.3.3 Plan, draft and write simple sentences & 4.2.5 Connect words and phrases using basic coordinating conjunctions",
                "4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level & 3.2.4 Use a picture dictionary to find, list and categorise words from Year 2 topics and themes"
            ]
        },
        "Unit 6: The old house (World of Stories)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of simple sentences & 4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing",
                "1.2.2 Understand with support specific information and details of simple sentences & 2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses",
                "1.2.3 Understand with support very short simple narratives & 1.2.2 Understand with support specific information and details of simple sentences",
                "1.1.1 Recognise and reproduce with support a range of high frequency target language phonemes & 3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV)",
                "1.2.2 Understand with support specific information and details of simple sentences & 2.1.5 Describe objects using suitable words and phrases",
                "1.2.2 Understand with support specific information and details of simple sentences & 2.1.1 Give simple personal information using basic statements"
            ],
            "Speaking": [
                "2.1.3 Give a short sequence of basic instructions & 1.2.5 Understand an increased range of short supported questions",
                "2.1.5 Describe objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of simple sentences",
                "2.1.2 Find out about personal information by asking basic questions & 2.1.5 Describe objects using suitable words and phrases",
                "2.1.5 Describe objects using suitable words and phrases & 2.2.2 Ask for attention of help from a teacher of a classmate by using suitable statements and questions",
                "2.1.5 Describe objects using suitable words and phrases & 2.2.2 Ask for attention of help from a teacher of a classmate by using suitable statements and questions",
                "2.2.2 Ask for attention of help from a teacher of a classmate & 1.2.5 Understand an increased range of short supported questions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of simple sentences & 4.2.3 Write short familiar instructions",
                "3.2.3 i) Reread a word, phrase or sentence to understand meaning ii)Ignore unknown words & 1.2.1 Understand with support the main idea of simple sentences",
                "3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV) & 1.1.1 Recognise and reproduce with support a range of high frequency target language phonemes",
                "3.2.1 Understand the main idea of simple sentences & 3.1.2 Recognise and sound out with some support beginning, medial and final sounds in a word",
                "3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV) & 1.1.1 Recognise and reproduce with support a range of high frequency target language phonemes",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.4 Use a picture dictionary to find, list and categorise words from Year 2 topics and themes"
            ],
            "Writing": [
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 2.1.2 Find out about personal information by asking basic questions",
                "4.3.3 Plan, draft and write simple sentences & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "4.2.1 Ask for and give basic personal information using basic questions and statements & 4.2.5 Connect words and phrases using basic coordinating conjunctions",
                "4.2.5 Connect words and phrases using basic coordinating conjunctions & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "4.2.3 Write short familiar instructions & 4.2.4 Describe objects using suitable words and phrases"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.2.2 Ask for attention of help from a teacher of a classmate by using suitable statements and questions",
                "5.1.2 Say the words in simple texts, and sing simple songs & 1.3.1 Understand the message the teacher or classmate is communicating by using visual clues",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 1.2.1 Understand with support the main idea of simple sentences",
                "5.2.1 Name people, things, actions, or places of interest in texts & 2.1.5 Describe objects using suitable words and phrases",
                "5.1.1 Demonstrate appreciation through nonverbal responses & 1.2.3 Understand with support very simple short narratives",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.1.3 Give a short sequence of basic instructions"
            ]
        },
        "Unit 7: Get dressed! (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of simple sentences & 3.3.1 Read and enjoy simple print and digital games at sentence level",
                "1.2.5 Understand an increased range of short supported questions & 1.3.1 Understand the message the teacher or classmate is communicating by using visual clues",
                "1.3.1 Understand the message the teacher or classmate is communicating by using visual clues & 2.1.5 Describe objects using suitable words and phrases",
                "1.1.1 Recognise and reproduce with support a range of high frequency target language Phonemes & 3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV)",
                "1.3.1 Understand the message the teacher or classmate is communicating by using visual clues & 2.1.5 Describe objects using suitable words and phrases",
                "1.3.1 Understand the message the teacher or classmate is communicating by using visual clues & 2.1.5 Describe objects using suitable words and phrases",
                "1.2.3 Understand with support very short simple narratives & 1.2.4 Understand an increased range of short basic supported classroom instructions"
            ],
            "Speaking": [
                "2.1.2 Find out about personal information asking basic questions & 1.2.5 Understand an increased range of short supported questions",
                "2.1.2 Find out about personal information asking basic questions & 2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses",
                "2.1.2 Find out about personal information asking basic questions & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "2.1.3 Give a short sequence of basic instructions & 2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses",
                "2.1.2 Find out about personal information by asking basic questions & 4.2.4 Name or describe objects using suitable words from word sets",
                "2.1.5 Describe objects using suitable words and phrases & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "2.1.5 Describe objects using suitable words and phrases & 1.1.1 Recognise and reproduce with support a limited range of high frequency target language phonemes"
            ],
            "Reading": [
                "3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV) & 3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV)",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.3 i) Reread a word, phrase or sentence to understand meaning",
                "3.2.1 Understand the main idea of simple sentences & 3.2.2 Understand specific information and details of simple sentences",
                "3.1.2 Recognise and sound out with some support beginning, medial and final sounds in a word & 3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV)",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.3 i) Reread a word, phrase or sentence to understand meaning",
                "3.2.2 Understand specific information and details of simple sentences & 3.3.1 Read and enjoy simple print and digital games at sentence level",
                "3.2.4 Use a picture dictionary to find, list and categorise words from Year 2 topics and themes & 2.1.5 Describe objects using suitable words and phrases"
            ],
            "Writing": [
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 3.1.1 Identify, recognise and name the letters of the alphabet",
                "4.2.3 Write short familiar instructions & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level & 4.2.5 Connect words and phrases using basic coordinating conjunctions",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 4.3.3 Plan, draft and write simple sentences",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 2.1.5 Describe objects using suitable words and phrases",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 3.3.1 Read and enjoy simple print and digital games at sentence level"
            ],
            "Language Arts": [
                "5.2.1 Name people, things, actions, or places of interest in texts & 4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing",
                "5.1.2 Say the words in simple texts, and sing simple songs & 3.2.3 ii) ignore unknown words in order to understand a phrase or sentence",
                "5.2.1 Name people, things, actions, or places of interest in texts & 1.3.1 Understand the message the teacher or classmate is communicating by using visual clues",
                "5.2.1 Name people, things, actions, or places of interest in texts & 2.1.5 Describe objects using suitable words and phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.1.5 Describe objects using suitable words and phrases",
                "5.1.2 Say the words in simple texts, and sing simple songs & 2.1.5 Describe objects using suitable words and phrases"
            ]
        },
        "Unit 8: The robot (World of Stories)": {
            "Speaking": [
                "2.1.3 Give a short sequence of basic instructions & 1.2.2 Understand with support specific information and details of simple sentences",
                "3.1.3 Blend phonemes (CVC, CCVC, CVCV, CCV) & 3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV)",
                "2.1.2 Find out about personal information by asking basic questions & 2.1.1 Give very basic personal information using fixed phrases",
                "2.3.1 Introduce self and others to an audience using fixed phrases & 2.1.2 Find out about personal information by asking basic questions",
                "2.1.2 Find out about personal information by asking basic questions & 4.2.1 Ask for and give basic personal information using basic questions and statements",
                "2.1.4 Ask about and express ability & 1.2.5 Understand an increased range of short supported questions",
                "2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses & 2.2.2 Ask for attention or help from a teacher or classmate using one word or a fixed phrase",
                "2.1.5 Describe objects using suitable words and phrases & 4.2.4 Name or describe objects using suitable words from word sets"
            ],
            "Writing": [
                "4.2.2 Express simple ability & 3.2.1 Understand the main idea of simple sentences",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 3.3.1 Read and enjoy simple print and digital games at sentence level",
                "4.2.2 Express simple ability & 2.1.4 Ask about and express ability",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 3.1.1 Identify, recognise and name the letters of the alphabet",
                "4.2.5 Connect words and phrases using basic coordinating conjunctions & 4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level",
                "3.2.1 Understand the main idea of simple sentences & 4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.3 i) Reread a word, phrase or sentence to understand meaning",
                "4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level & 4.3.3 Plan, draft and write simple sentences",
                "4.2.4 Name or describe objects using suitable words from word sets & 1.2.1 Understand with support the main idea of simple sentences",
                "4.3.1 Use capital letters and full stops appropriately in guided writing at sentence level & 4.3.3 Plan, draft and write simple sentences"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.1.3 Give a short sequence of basic instructions",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.1.5 Describe objects using suitable words and phrases",
                "5.1.1 Demonstrate appreciation through nonverbal responses & 1.2.4 Understand an increased range of short basic supported classroom instructions",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.1.4 Ask about and express ability",
                "5.1.1 Demonstrate appreciation through nonverbal responses & 2.1.1 Give very basic personal information using fixed phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 2.2.2 Ask for attention or help from a teacher or classmate using one word or a fixed phrase",
                "5.1.1 Demonstrate appreciation through nonverbal responses & 5.1.2 Say the words in simple texts, and sing simple songs",
                "5.2.1 Name people, things, actions, or places of interest in texts & 1.2.3 Understand with support very short simple narratives"
            ],
            "Listening": [
                "1.2.2 Understand with support specific information and details of simple sentences & 2.1.5 Describe objects using suitable words and phrases",
                "1.2.2 Understand with support specific information and details of simple sentences & 2.1.4 Ask about and express ability",
                "1.2.2 Understand with support specific information and details of simple sentences & 1.2.5 Understand an increased range of short supported questions",
                "1.1.1 Recognise and reproduce with support a range of high frequency target language Phonemes & 3.1.2 Recognise and sound out with some support beginning, medial and final sounds in a word",
                "1.2.5 Understand an increased range of short supported questions & 1.3.1 Understand the message the teacher or classmate is communicating by using visual clues",
                "1.2.2 Understand with support specific information and details of simple sentences & 3.2.4 Use a picture dictionary to find, list and categorise words from Year 2 topics and themes",
                "1.2.2 Understand with support specific information and details of simple sentences & 4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing"
            ],
            "Reading": [
                "2.1.4 Ask about and express ability & 1.2.2 Understand with support specific information and details of simple sentences",
                "3.2.1 Understand the main idea of simple sentences & 1.2.2 Understand with support specific information and details of simple sentences",
                "3.1.4 Segment phonemes (CVC, CCVC, CVCV, CCV) & 3.1.2 Recognise and sound out with some support beginning, medial and final sounds in a word",
                "3.2.2 Understand specific information and details of simple sentences & 2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses",
                "3.2.2 Understand specific information and details of simple sentences & 4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing"
            ]
        },
        "Unit 9: At the beach (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of simple sentences & 1.3.1 Understand the message the teacher or classmate is communicating",
                "1.2.2 Understand with support specific information and details of simple sentences & 4.2.5 Connect words and phrases using basic coordinating conjunctions",
                "1.1.1 Recognise and reproduce with support a range of high frequency target language Phonemes & 3.1.2 Recognise and sound out with some support",
                "1.2.2 Understand with support specific information and details of simple sentences & 3.1.2 Recognise and sound out with some support",
                "1.3.1 Understand the message the teacher or classmate is communicating & 1.2.4 Understand an increased range of short basic supported classroom instructions",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.4 Use a picture dictionary to find, list and categorise words",
                "1.2.5 Understand an increased range of short supported questions & 1.2.2 Understand with support specific information and details of simple sentences"
            ],
            "Speaking": [
                "2.1.2 Find out about personal information by asking basic questions & 1.3.1 Understand the message the teacher or classmate is communicating",
                "2.1.3 Give a short sequence of basic instructions & 1.2.4 Understand an increased range of short basic supported classroom instructions",
                "2.1.1 Give very basic personal information using fixed phrases & 2.1.5 Describe objects using suitable words and phrases",
                "2.1.5 Describe objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of simple sentences",
                "2.1.5 Describe objects using suitable words and phrases & 2.2.2 Ask for attention or help from the teacher or classmate",
                "2.1.5 Describe objects using suitable words and phrases & 1.2.5 Understand an increased range of short supported questions"
            ],
            "Writing": [
                "4.3.2 Spell a narrow range of familiar high frequency words accurately in guided writing & 1.2.2 Understand with support specific information and details",
                "2.1.1 Give very basic personal information using fixed phrases & 2.2.1 Keep interaction going in short exchanges by using suitable non-verbal responses",
                "4.3.3 Plan, draft and write simple sentences & 2.1.1 Give very basic personal information using fixed phrases",
                "4.3.3 Plan, draft and write simple sentences & 4.3.1 Use capital letters and full stops appropriately in guided writing",
                "4.3.1 Use capital letters and full stops appropriately in guided writing & 4.3.2 Spell a narrow range of familiar high frequency words accurately",
                "4.3.3 Plan, draft and write simple sentences & 4.3.1 Use capital letters and full stops appropriately in guided writing",
                "4.3.1 Use capital letters and full stops appropriately in guided writing & 4.3.3 Plan, draft and write simple sentences"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of simple sentences & 2.1.1 Give very basic personal information using fixed phrases",
                "3.2.2 Understand specific information and details of simple sentences & 3.2.3 i) Reread a word, phrase or sentence to understand meaning",
                "3.2.3 i) Reread a word, phrase or sentence ii) Ignore unknown words & 3.2.1 Understand the main idea of simple sentences",
                "3.2.1 Understand the main idea of simple sentences & 3.2.3 i) Reread a word, phrase or sentence ii) Ignore unknown words",
                "3.2.2 Understand specific information and details of simple sentences & 4.3.2 Spell a narrow range of familiar high frequency words accurately",
                "3.2.3 i) Reread a word, phrase or sentence ii) Ignore unknown words & 1.2.5 Understand an increased range of short supported questions"
            ],
            "Language Arts": [
                "5.1.2 Say the words in simple texts, and sing simple songs & 3.1.2 Recognise and sound out with some support",
                "5.2.1 Name people, things, actions, or places of interest in texts & 1.2.3 Understand with support very short simple narratives",
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 1.2.2 Understand with support specific information and details",
                "5.2.1 Name people, things, actions, or places of interest in texts & 4.3.2 Spell a narrow range of familiar high frequency words accurately",
                "5.1.2 Say the words in simple texts, and sing simple songs & 5.2.1 Name people, things, actions, or places of interest in texts",
                "5.1.2 Say the words in simple texts, and sing simple songs & 2.3.1 Introduce self and others to an audience using fixed phrases"
            ]
        }
    },
    "Year 3": {
        "Unit 1: Welcome! (World of Self, Family and Friends)": {
            "Writing": [
                "1.3.1 Guess the meaning of unfamiliar words by using visual clues & 2.1.5 Describe people and objects using suitable words and phrases",
                "4.2.4 Describe people and objects using suitable words and phrases & 4.1.2 Begin to use cursive handwriting in a limited range of written work",
                "4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing & 1.2.1 Understand with support the main idea of short simple texts",
                "4.3.1 Use capital letters, full stops and question marks appropriately & 4.3.3 Plan, draft and write an increased range of simple sentences"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of short simple texts",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wide range of short supported questions",
                "2.1.2 Find out about and describe basic everyday routines & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.1 Understand the main idea of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.2 Understand specific information and details of short simple texts & 2.1.5 Describe people and objects using suitable words and phrases",
                "3.2.2 Understand specific information and details of short simple texts & 4.3.1 Use capital letters, full stops and question marks appropriately"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.3.3 Plan, draft and write an increased range of simple sentences",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 5.1.1 In addition to Year 2 text types: simple poems",
                "5.2.1 Name people, things, actions, or places of interest in texts & 2.3.1 Narrate very short basic stories and events"
            ],
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 4.3.1 Use capital letters, full stops and question marks appropriately",
                "1.2.5 Understand a wide range of short supported questions & 2.2.2 Ask for attention or help from a teacher or classmate by using suitable questions"
            ]
        },
        "Unit 2: Every day (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 1.3.1 Guess the meaning of unfamiliar words by using visual clues",
                "1.2.2 Understand with support specific information and details of short simple texts & 1.2.5 Understand a wide range of short supported questions",
                "1.2.1 Understand with support the main idea of simple sentences & 2.3.1 Introduce self and others to an audience using fixed phrases"
            ],
            "Speaking": [
                "2.1.2 Find out about and describe basic everyday routines & 4.3.2 Spell an increased range of familiar high frequency words accurately",
                "2.1.2 Find out about and describe basic everyday routines & 1.2.5 Understand a wide range of short supported questions",
                "2.1.2 Find out about and describe basic everyday routines & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of short simple texts & 3.2.2 Understand specific information and details of short simple texts",
                "3.2.4 Use a picture dictionary to find, list and categorise words & 3.2.2 Understand specific information and details of short simple texts",
                "3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals & 3.2.2 Understand specific information and details of short simple texts",
                "3.2.2 Understand specific information and details of short simple texts & 4.2.4 Describe people and objects using suitable words and phrases"
            ],
            "Writing": [
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.3.1 Use capital letters, full stops and question marks appropriately",
                "4.3.2 Spell an increased range of familiar high frequency words accurately & 2.2.2 Ask for attention or help from a teacher or classmate by using suitable questions",
                "4.3.1 Use capital letters, full stops and question marks appropriately & 4.1.2 Begin to use cursive handwriting in a limited range of written work"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 5.1.1 In addition to Year 2 text types: simple poems",
                "5.1.2 Say the words in simple texts, and sing simple songs & 1.2.3 Understand with support very short simple narratives",
                "5.2.1 Name people, things, actions, or places of interest in texts & 2.1.5 Describe people and objects using suitable words and phrases"
            ]
        },
        "Unit 3: Right now (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 1.3.1 Guess the meaning of unfamiliar words by using visual clues",
                "1.2.2 Understand with support specific information and details of short simple texts & 1.3.1 Guess the meaning of unfamiliar words by using visual clues",
                "4.2.4 Describe people and objects using suitable words and phrases & 3.2.2 Understand specific information and details of short simple texts",
                "1.2.2 Understand with support specific information and details of short simple texts & 4.3.3 Plan, draft and write simple sentences"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable words and phrases & 1.1.1 Recognise and reproduce with support a range of target language phonemes",
                "2.1.5 Describe people and objects using suitable words and phrases & 2.2.2 Ask for attention or help from a teacher or classmate",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Writing": [
                "3.2.1 Understand the main idea of short simple texts & 3.2.2 Understand specific information and details of short simple texts",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately & 3.2.2 Understand specific information and details of short simple texts",
                "4.3.3 Plan, draft and write simple sentences & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "4.2.4 Describe people and objects using suitable words and phrases & 1.1.1 Recognise and reproduce with support a range of target language phonemes"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 2.1.5 Describe people and objects using suitable words and phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 2.1.5 Describe people and objects using suitable words and phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.3.2 Spell a narrow range of familiar high frequency words accurately"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of short simple texts & 3.2.2 Understand specific information and details of short simple texts",
                "3.2.1 Understand the main idea of short simple texts & 4.3.2 Spell a narrow range of familiar high frequency words accurately"
            ]
        },
        "Unit 4: Year in, year out (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of short simple texts & 2.2.1 Keep interaction going in short exchanges",
                "1.2.2 Understand with support specific information and details of short simple sentences & 2.1.2 Find out about and describe basic everyday routines",
                "1.2.2 Understand with support specific information and details of short simple sentences & 3.2.1 Understand the main idea of short simple texts"
            ],
            "Speaking": [
                "2.1.1 Ask about and express basic opinions & 1.2.2 Understand with support specific information and details of short simple texts",
                "2.1.2 Find out about and describe basic everyday routines & 4.1.2 Begin to use cursive handwriting in a limited range of written work",
                "2.1.2 Find out about and describe basic everyday routines & 2.1.5 Describe people and objects using suitable words and phrases",
                "4.3.1 Use capital letters and full stops and question marks appropriately & 2.1.2 Find out about and describe basic everyday routines"
            ],
            "Writing": [
                "3.2.1 Understand the main idea of short simple texts & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "4.3.2 Spell a narrow range of familiar high frequency words accurately & 2.1.2 Find out about and describe basic everyday routines",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 1.2.5 Understand a wild range of short supported questions",
                "4.2.4 Describe people and objects using suitable words and phrases & 2.2.2 Ask for attention of help from a teacher or a classmate"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.3.2 Spell a narrow range of familiar high frequency words accurately",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.2.4 Describe people and objects using suitable words and phrases"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of short simple sentences & 2.2.2 Ask for attention of help from a teacher or a classmate",
                "3.2.2 Understand specific information and details of short simple sentences & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ]
        },
        "Unit 5: My new house (World of Self, Family and Friends)": {
            "Speaking": [
                "1.2.2 Understand with support specific information & 1.2.1 Understand with support the main idea",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wild range of short supported questions",
                "2.1.1 Ask about and express basic opinions & 1.2.5 Understand a wild range of short supported questions",
                "2.1.1 Ask about and express basic opinions & 1.2.5 Understand a wild range of short supported questions",
                "2.1.5 Describe people and objects using suitable words and phrases & 4.3.1 Use capital letters, full stops and question marks appropriately"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details & 4.3.2 Spell a narrow range of familiar high frequency words accurately",
                "3.2.3 Guess the meaning of unfamiliar words & 3.2.1 Understand the main idea of short simple texts",
                "3.2.2 Understand specific information and details & 3.2.1 Understand the main idea of short simple texts"
            ],
            "Writing": [
                "4.1.2 Begin to use cursive handwriting & 3.2.4 Recognise and use with support key features of a simple monolingual dictionary",
                "4.2.4 Describe people and objects using suitable words and phrases & 4.3.3 Plan, draft and write an increased range of simple sentences",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 2.3.1 Introduce self and others to an audience using fixed phrases"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple short chants or raps & 1.2.4 Understand a wide range of short basic supported classroom instructions",
                "5.1.2 Say the words in simple texts, and sing simple songs & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "5.2.1 Ask and answer simple questions about characters & 1.2.3 Understand with support short simple narratives"
            ],
            "Listening": [
                "1.2.2 Understand with support specific information & 1.2.5 Understand a wild range of short supported questions",
                "1.1.1 Recognise and reproduce with support a range of target language phonemes & 2.1.5 Describe people and objects using suitable words and phrases"
            ]
        },
        "Unit 6: Food, please! (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 2.1.1 Ask about and express basic opinions",
                "1.2.5 Understand a wide range of short supported questions & 1.2.2 Understand with support specific information and details of short simple texts",
                "1.2.2 Understand with support specific information and details of short simple texts & 1.2.5 Understand a wide range of short supported questions",
                "3.2.2 Understand specific information and details of short simple texts & 2.1.1 Ask about and express basic opinions"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of short simple texts",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic & 3.2.2 Understand specific information and details of short simple sentences",
                "3.2.1 Understand the main idea of short simple texts & 3.2.2 Understand specific information and details of short simple sentences",
                "3.2.1 Understand the main idea of short simple texts & 1.2.5 Understand a wide range of short supported questions",
                "3.2.1 Understand the main idea of short simple texts & 4.2.5 Connect sentences using basic coordinating conjunctions"
            ],
            "Writing": [
                "4.2.3 Give simple directions & 4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 3.2.2 Understand specific information and details of short simple sentences",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 2.3.1 Introduce self and others to an audience using fixed phrases"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 2.1.1 Ask about and express basic opinions",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts of interest"
            ]
        },
        "Unit 7: Out and about (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 1.3.1 Guess the meaning of unfamiliar words by using visual clues",
                "1.2.1 Understand with support the main idea of short simple texts & 4.2.4 Describe people and objects using suitable words and phrases",
                "1.2.2 Understand with support specific information and details of short simple texts & 1.2.1 Understand with support the main idea of short simple texts"
            ],
            "Speaking": [
                "2.1.3 Give a short sequence of basic directions & 1.2.4 Understand a wide range of short basic supported classroom instructions",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of short simple texts",
                "2.1.2 Find out about and describe everyday routines & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of short simple texts & 1.1.1 Recognise and reproduce with support a range of target language phonemes",
                "3.2.1 Understand the main idea of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.1 Understand the main idea of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic"
            ],
            "Writing": [
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.1.2 Begin to use cursive handwriting in a limited range of written work",
                "4.2.3 Give simple directions & 4.3.1 Use capital letters, full stops and question marks appropriately in guided writing at sentence level",
                "4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing & 1.2.2 Understand with support specific information and details of short simple texts",
                "4.2.3 Give simple directions & 3.2.2 Understand specific information and details of short simple texts"
            ],
            "Language Arts": [
                "5.1.2 Say the words in simple texts, and sing simple songs & 1.2.2 Understand with support specific information and details of short simple texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing",
                "5.2.1 Ask and answer simple questions about characters & 2.1.4 Ask about, make and respond to simple predictions"
            ]
        },
        "Unit 8: Where were you yesterday? (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 1.2.5 Understand a wide range of short supported questions",
                "1.2.2 Understand with support specific information and details of short simple texts & 2.1.1 Give a short sequence of basic directions",
                "1.2.2 Understand with support specific information and details of short simple texts & 2.1.1 Give a short sequence of basic directions"
            ],
            "Speaking": [
                "2.3.1 Introduce self and others to an audience using fixed phrases & 2.2.2 Ask for attention or help from a teacher or classmate by using suitable questions",
                "2.1.1 Give a short sequence of basic directions & 2.3.1 Introduce self and others to an audience using fixed phrases",
                "2.1.1 Give a short sequence of basic directions & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of short simple texts & 1.2.5 Understand a wide range of short supported questions",
                "3.2.2 Understand specific information and details of short simple texts & 4.2.2 Make and give reasons for simple predictions",
                "3.2.2 Understand specific information and details of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.2 Understand specific information and details of short simple texts & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Writing": [
                "4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing & 3.2.2 Understand specific information and details of short simple texts",
                "4.2.4 Describe people and objects using suitable words and phrases & 4.3.1 Use capital letters, full stops and question marks appropriately in guided writing at sentence level",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing"
            ],
            "Language Arts": [
                "5.2.1 Ask and answer simple questions about characters & 4.2.4 Describe people and objects using suitable words and phrases",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 3.2.2 Understand specific information and details of short simple texts",
                "5.2.1 Ask and answer simple questions about characters & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic"
            ]
        },
        "Unit 9: On holiday (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of short simple texts & 2.1.5 Describe people and objects using suitable words and phrases",
                "1.2.2 Understand with support specific information and details of short simple texts & 2.1.5 Describe people and objects using suitable words and phrases",
                "1.2.3 Understand with support short simple narratives & 4.3.3 Plan, draft and write an increased range of simple sentences"
            ],
            "Speaking": [
                "2.3.1 Narrate very short basic stories and events & 3.2.2 Understand specific information and details of short simple texts",
                "2.2.1 Keep interaction going in short exchanges & 4.3.3 Plan, draft and write an increased range of simple sentences",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words & 3.2.4 Recognise and use with support key features of a simple monolingual dictionary",
                "3.2.3 Guess the meaning of unfamiliar words & 3.2.4 Recognise and use with support key features of a simple monolingual dictionary",
                "3.2.2 Understand specific information and details of short simple texts & 4.2.5 Connect sentences using basic coordinating conjunctions"
            ],
            "Writing": [
                "4.3.3 Plan, draft and write an increased range of simple sentences & 3.2.2 Understand specific information and details of short simple texts",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing",
                "4.2.5 Connect sentences using basic coordinating conjunctions & 4.3.1 Use capital letters, full stops and question marks appropriately",
                "4.2.4 Describe people and objects using suitable words and phrases & 1.2.5 Understand a wide range of short supported questions"
            ],
            "Language Arts": [
                "5.1.2 Say the words in simple texts, and sing simple songs & 2.3.1 Narrate very short basic stories and events",
                "5.1.2 Say the words in simple texts, and sing simple songs & 2.1.5 Describe people and objects using suitable words and phrases",
                "5.2.1 Ask and answer simple questions about characters & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts of interest"
            ]
        },
        "Unit 10: The world around us (World of Knowledge)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of short simple texts & 1.1.1 Recognise and reproduce with support a range of target language phonemes",
                "1.2.2 Understand with support specific information and details of short simple texts & 2.1.5 Describe people and objects using suitable words and phrases",
                "1.2.5 Understand a wide range of short supported questions & 3.2.2 Understand specific information and details of short simple texts"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.2 Understand with support specific information and details of short simple texts",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.4 Understand a wide range of short basic supported classroom instructions",
                "2.1.5 Describe people and objects using suitable words and phrases & 3.2.2 Understand specific information and details of short simple texts"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.2 Understand specific information and details of short simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic",
                "3.2.3 Guess the meaning of unfamiliar words from clues provided by visuals and the topic & 1.2.4 Understand a wide range of short basic supported classroom instructions"
            ],
            "Writing": [
                "4.2.4 Describe people and objects using suitable words and phrases & 4.3.2 Spell an increased range of familiar high frequency words accurately in guided writing",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.3.1 Use capital letters, full stops and question marks appropriately in guided writing",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 4.2.4 Describe people and objects using suitable words and phrases",
                "4.3.3 Plan, draft and write an increased range of simple sentences & 3.2.2 Understand specific information and details of short simple texts"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 4.2.4 Describe people and objects using suitable words and phrases",
                "5.2.1 Ask and answer simple questions about characters & 4.3.3 Plan, draft and write an increased range of simple sentences",
                "5.2.1 Ask and answer simple questions about characters & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts of interest"
            ]
        }
    },
    "Year 4": {
        "Unit 1: Where are you from? (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of longer simple texts & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes",
                "1.2.2 Understand with support specific information and details of longer simple texts & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes",
                "1.2.3 Understand with support short simple narratives on a range of familiar topics & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.4 Understand longer supported classroom instructions",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.4 Understand longer supported classroom instructions",
                "2.1.5 Describe people and objects using suitable words and phrases & 1.2.5 Understand longer supported questions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of short simple texts & 1.2.4 Understand longer supported classroom instructions",
                "3.2.2 Understand specific information and details of short simple texts & 1.2.4 Understand longer supported classroom instructions",
                "3.2.1 Understand the main idea of simple texts of one or two paragraphs & 3.2.2 Understand specific information and details of simple texts of one or two paragraphs"
            ],
            "Writing": [
                "4.2.4 Describe people and objects using suitable words and phrases & 4.3.2 Spell most high frequency words accurately in guided writing",
                "4.2.4 Describe people and objects using suitable words and phrases & 4.3.2 Spell most high frequency words accurately in guided writing",
                "2.1.5 Describe people, and objects using suitable statements & 4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating simple action songs & 4.2.4 Describe people and objects using suitable statements"
            ]
        },
        "Unit 2: My Week (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of longer simple texts & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes",
                "1.2.5 Understand longer supported questions & 1.2.3 Understand with support short simple narratives on a range of familiar topics",
                "1.2.5 Understand longer supported questions & 1.2.2 Understand with support specific information and details of longer simple texts"
            ],
            "Speaking": [
                "2.1.1 Explain and give reasons for basic opinions & 1.2.5 Understand longer supported questions",
                "2.1.4 Give reasons for simple predictions & 4.2.1 Explain and give reasons for simple opinions",
                "2.1.5 Describe people, and objects using suitable statements & 1.2.5 Understand longer supported questions"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of simple texts of one or two paragraphs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "3.2.2 Understand specific information and details of simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by title and topic",
                "3.2.2 Understand specific information and details of simple texts & 3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary"
            ],
            "Writing": [
                "3.2.2 Understand specific information and details of simple texts & 4.2.4 Describe people and objects using suitable statements",
                "4.3.3 Produce a plan or draft of one paragraph & 4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately",
                "4.3.2 Spell most high frequency words accurately in guided writing & 1.2.5 Understand longer supported questions"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively through creating simple action songs & 1.2.5 Understand a wide range of longer supported questions",
                "5.3.1 Respond imaginatively through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ]
        },
        "Unit 3: In the Past (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 1.2.2 Understand with support specific information and details of longer simple texts",
                "1.2.5 Understand longer supported questions & 2.1.2 Find out about and describe experiences in the past",
                "1.2.5 Understand longer supported questions & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes"
            ],
            "Speaking": [
                "2.1.2 Find out about and describe experiences in the past & 3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary",
                "2.1.2 Find out about and describe experiences in the past & 2.1.3 Give a longer sequence of basic instructions or directions",
                "2.1.2 Find out about and describe experiences in the past & 2.3.1 Narrate short basic stories"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of simple texts of one or two paragraphs & 1.2.3 Understand with support short simple narratives on a range of familiar topics",
                "3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts & 2.1.4 Give reasons for simple predictions",
                "3.2.2 Understand specific information and details of simple texts & 1.2.4 Understand longer supported classroom instructions"
            ],
            "Writing": [
                "4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately & 3.2.2 Understand specific information and details of simple texts",
                "4.2.4 Describe people and objects using suitable statements & 1.2.3 Understand with support short simple narratives on a range of familiar topics",
                "4.2.5 Connect sentences into a coherent paragraph & 3.2.2 Understand specific information and details of simple texts"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively through creating simple action songs & 4.2.1 Explain and give reasons for simple opinions",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.2 Find out about and describe experiences in the past",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.4 Give reasons for simple predictions"
            ]
        },
        "Unit 4: Celebrations (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues provided by title and topic",
                "1.2.3 Understand with support short simple narratives & 1.2.2 Understand with support specific information and details of longer simple texts",
                "1.2.1 Understand with support the main idea of longer simple texts & 1.2.2 Understand with support specific information and details of longer simple texts"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand longer supported questions",
                "2.1.1 Explain and give reasons for basic opinions & 2.2.2 Check steps needed to complete short classroom tasks",
                "4.3.2 Spell most high frequency words accurately in guided writing & 2.1.4 Give reasons for simple predictions"
            ],
            "Reading": [
                "3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "3.2.1 Understand the main idea of simple texts & 3.2.2 Understand specific information and details of simple texts",
                "3.2.2 Understand specific information and details of simple texts & 4.1.2 Use cursive writing in written work"
            ],
            "Writing": [
                "4.2.4 Describe people and objects using suitable statements & 4.1.2 Use cursive writing in written work",
                "4.3.3 Produce a plan or draft of one paragraph & 4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately",
                "4.2.5 Connect sentences into a coherent paragraph & 4.2.2 Make and respond to simple offers and invitations"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 4.2.4 Describe people and objects using suitable statements"
            ]
        },
        "Unit 5: Eating right (World of Self, Family and Friends)": {
            "Listening": [
                "1.3.1 Guess the meaning of unfamiliar words & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes",
                "1.2.5 Understand longer supported questions & 1.2.2 Understand with support specific information and details of longer simple texts",
                "1.2.5 Understand longer supported questions & 2.2.1 Keep interaction going in short exchanges"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand longer supported questions",
                "2.1.1 Explain and give reasons for basic opinions & 4.2.3 Describe basic everyday routines",
                "2.1.5 Describe people, and objects using suitable statements & 2.2.2 Check steps needed to complete short classroom tasks"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details & 3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary",
                "3.2.2 Understand specific information and details & 4.3.2 Spell most high frequency words accurately in guided writing",
                "3.2.2 Understand specific information and details & 3.2.3 Guess the meaning of unfamiliar words from clues provided by title and topic"
            ],
            "Writing": [
                "4.3.2 Spell most high frequency words accurately & 4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately",
                "4.2.5 Connect sentences into a coherent paragraph & 4.2.3 Describe basic everyday routines",
                "4.1.2 Use cursive writing in written work & 4.3.2 Spell most high frequency words accurately in guided writing"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating picture stories & 2.2.2 Check steps needed to complete short classroom tasks",
                "5.3.1 Respond imaginatively through creating picture stories & 2.1.1 Explain and give reasons for basic opinions"
            ]
        },
        "Unit 6: Getting around (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.5 Understand longer supported questions & 1.2.2 Understand with support specific information and details of longer simple texts",
                "1.2.2 Understand with support specific information and details of longer simple texts & 4.2.3 Describe basic everyday routines"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 4.2.2 Make and respond to simple offers and invitations",
                "2.2.2 Check steps needed to complete short classroom tasks & 2.1.3 Give a longer sequence of basic instructions or directions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of simple texts & 2.1.5 Describe people and objects using suitable statements",
                "3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts & 2.3.1 Narrate short basic stories"
            ],
            "Writing": [
                "4.2.4 Describe people and objects using suitable statements & 4.3.3 Produce a plan or draft of one paragraph",
                "4.2.1 Explain and give reasons for simple opinions & 4.2.4 Describe people and objects using suitable statements"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively through creating simple picture stories & 4.2.2 Make and respond to simple offers and invitations",
                "5.3.1 Respond imaginatively through creating simple picture stories & 4.3.3 Produce a plan or draft of one paragraph"
            ]
        },
        "Unit 7: Helping out (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of longer simple texts & 3.2.3 Guess the meaning of unfamiliar words",
                "1.2.2 Understand with support specific information and details of longer simple texts & 2.1.5 Describe people and objects using suitable statements",
                "1.2.3 Understand with support short simple narratives & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable statements & 2.1.2 Find out about and describe experiences in the past",
                "2.1.5 Describe people and objects using suitable statements & 1.2.5 Understand longer supported questions",
                "2.1.3 Give a longer sequence of basic directions & 2.2.2 Check steps needed to complete short classroom tasks"
            ],
            "Reading": [
                "3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts & 1.2.3 Understand with support short simple narratives",
                "3.2.2 Understand specific information and details of simple texts & 3.2.1 Understand the main idea of simple texts",
                "3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary & 3.2.1 Understand the main idea of simple texts"
            ],
            "Writing": [
                "4.3.1 Use capital letters, full stops, question marks and commas appropriately & 3.2.2 Understand specific information and details of simple texts",
                "4.2.3 Describe basic everyday routines & 4.3.2 Spell most high frequency words accurately in guided writing",
                "4.3.1 Use capital letters, full stops, question marks and commas appropriately & 3.2.2 Understand specific information and details of short simple texts"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.5 Describe people and objects using suitable statements",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.4 Give reasons for simple predictions",
                "5.3.1 Respond imaginatively through creating simple picture stories & 2.1.4 Give reasons for simple predictions"
            ]
        },
        "Unit 8: Amazing animals (World of Knowledge)": {
            "Listening": [
                "1.2.5 Understand longer supported questions & 1.3.1 Guess the meaning of unfamiliar words",
                "1.3.1 Guess the meaning of unfamiliar words & 2.1.4 Give reasons for simple predictions",
                "1.1.1 Recognise and reproduce with support a wide range of target language phonemes & 3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary"
            ],
            "Speaking": [
                "2.1.5 Describe people and objects using suitable statements & 4.3.2 Spell most high frequency words accurately in guided writing",
                "2.1.5 Describe people and objects using suitable statements & 2.2.2 Check steps needed to complete short classroom tasks",
                "2.1.1 Explain and give reasons for basic opinions & 2.1.5 Describe people and objects using suitable statements"
            ],
            "Reading": [
                "3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary & 2.1.5 Describe people and objects using suitable statements",
                "3.2.2 Understand specific information and details of simple texts & 2.1.4 Give reasons for simple predictions",
                "3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts & 2.3.1 Narrate short basic stories"
            ],
            "Writing": [
                "4.2.4 Describe people and objects using suitable statements & 4.3.2 Spell most high frequency words accurately in guided writing",
                "4.2.4 Describe people and objects using suitable statements & 1.2.2 Understand with support specific information and details of longer simple texts",
                "4.2.5 Connect sentences into a coherent paragraph & 4.3.3 Produce a plan or draft of one paragraph"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.1 Explain and give reasons for basic opinions",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating simple picture stories & 4.3.2 Spell most high frequency words accurately in guided writing"
            ]
        },
        "Unit 9: Get active! (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details of longer simple texts & 1.2.1 Understand with support the main idea of longer simple texts",
                "1.2.2 Understand with support specific information and details of longer simple texts & 4.3.3 Produce a plan or draft of one paragraph",
                "1.2.1 Understand with support the main idea of longer simple texts & 2.1.1 Explain and give reasons for basic opinions"
            ],
            "Speaking": [
                "2.1.1 Explain and give reasons for basic opinions & 2.2.1 Keep interaction going in short exchanges",
                "2.1.5 Describe people and objects using suitable statements & 1.2.2 Understand with support specific information and details of longer simple texts",
                "2.1.5 Describe people and objects using suitable statements & 2.1.1 Explain and give reasons for basic opinions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of simple texts & 3.2.1 Understand the main idea of simple texts",
                "3.2.2 Understand specific information and details of simple texts & 3.2.1 Understand the main idea of simple texts",
                "3.2.2 Understand specific information and details of simple texts & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ],
            "Writing": [
                "4.2.2 Make and respond to simple offers and invitations & 4.2.5 Connect sentences into a coherent paragraph",
                "4.2.4 Describe people and objects using suitable statements & 3.2.2 Understand specific information and details of simple texts",
                "4.2.1 Explain and give reasons for simple opinions & 3.2.2 Understand specific information and details of simple texts"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 2.1.1 Explain and give reasons for basic opinions",
                "5.3.1 Respond imaginatively through creating simple picture stories & 2.3.1 Narrate short basic stories",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 4.1.2 Use cursive handwriting in written work"
            ]
        },
        "Unit 10: What’s the matter? (World of Self, Family and Friends)": {
            "Listening": [
                "1.3.1 Guess the meaning of unfamiliar words & 1.1.1 Recognise and reproduce with support a wide range of target language phonemes",
                "1.2.2 Understand with support specific information and details of longer simple texts & 2.1.1 Explain and give reasons for basic opinions"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand a wide range of longer supported questions",
                "2.2.2 Check steps needed to complete short classroom tasks & 1.2.4 Understand longer supported classroom instructions"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words & 1.2.3 Understand with support short simple narratives on a range of familiar topics",
                "3.2.2 Understand specific information and details of simple texts & 3.2.4 Recognise and use with little or no support key features of a simple monolingual dictionary",
                "3.2.2 Understand specific information and details of simple texts & 3.2.3 Guess the meaning of unfamiliar words"
            ],
            "Writing": [
                "4.2.2 Make and respond to simple offers and invitations & 4.2.1 Explain and give reasons for simple opinions",
                "4.3.3 Produce a plan or draft of one paragraph & 4.3.2 Spell most high frequency words accurately in guided writing",
                "4.3.3 Produce a plan or draft of one paragraph & 2.2.2 Check steps needed to complete short classroom tasks"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 4.3.1 Use capital letters, full stops, question marks and commas appropriately",
                "5.2.1 Say in simple words and phrases how a text makes them feel & 4.2.4 Describe people and objects using suitable statements",
                "5.3.1 Respond imaginatively through creating simple picture stories & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ]
        }
    },
    "Year 5": {
        "Starter Unit: Free time (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 3.2.1 Understand the main idea of simple texts of two paragraphs or more",
                "1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes & 3.2.1 Understand the main idea of simple texts of two paragraphs or more",
                "1.2.5 Understand a sequence of supported questions & 3.2.3 Guess the meaning of unfamiliar words from clues"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves & 4.2.1 Give detailed information about themselves",
                "2.1.1 Give detailed information about themselves & 4.2.1 Give detailed information about themselves",
                "2.1.1 Give detailed information about themselves & 4.3.2 Spell a range of high frequency words accurately"
            ],
            "Reading": [
                "3.2.1 Understand the main idea of simple texts of one or two paragraphs & 2.2.1 Keep interaction going in short exchanges",
                "3.2.2 Understand specific information and details of two paragraphs or more & 4.2.4 Describe people, places and objects using suitable statements",
                "3.3.1 Read and enjoy A2 fiction/non-fiction print and digital texts of interest & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately"
            ],
            "Writing": [
                "4.2.4 Describe people, places and objects using suitable statements & 1.2.4 Understand a sequence of supported classroom instructions",
                "4.2.4 Describe people, places and objects using suitable statements & 2.1.5 Describe people, places and objects using suitable statements",
                "4.2.1 Give detailed information about themselves & 3.2.1 Understand the main idea of simple texts of two paragraphs or more"
            ],
            "Language Arts": [
                "5.2.1 Explain in simple language why they like or dislike an event & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.3.1 Narrate short basic stories and events",
                "5.2.1 Explain in simple language why they like or dislike an event & 1.2.2 Understand with support specific information and details"
            ]
        },
        "Unit 1: Towns and cities (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 4.2.4 Describe people, places and objects using suitable statements",
                "1.2.2 Understand with support specific information and details & 4.3.2 Spell a range of high frequency words accurately",
                "1.2.5 Understand a sequence of supported questions & 4.3.2 Spell a range of high frequency words accurately"
            ],
            "Speaking": [
                "2.1.5 Describe people, places and objects using suitable statements & 4.2.1 Give detailed information about themselves",
                "2.1.2 Find out about and Describe experiences up to now & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand a sequence of supported questions"
            ],
            "Reading": [
                "3.2.4 Use with support familiar print and digital resources to check meaning & 2.1.5 Describe people, places and objects using suitable statements",
                "3.2.2 Understand specific information and details of two paragraphs or more & 4.3.2 Spell a range of high frequency words accurately",
                "3.2.4 Use with support familiar print and digital resources to check meaning & 4.2.4 Describe people, places and objects using suitable statements"
            ],
            "Writing": [
                "4.2.4 Describe people, places and objects using suitable statements & 2.2.1 Keep interaction going in short exchanges",
                "4.2.5 Connect sentences into one or two coherent paragraphs & 3.2.1 Understand the main idea of simple texts",
                "4.2.5 Connect sentences into one or two coherent paragraphs & 2.1.5 Describe people, places and objects using suitable statements"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.2.4 Describe people, places and objects using suitable statements",
                "2.2.1 Keep interaction going in short exchanges & 4.2.4 Describe people, places and objects using suitable statements",
                "5.2.1 Explain in simple language why they like or dislike an event & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "2.2.1 Keep interaction going in short exchanges & 4.3.2 Spell a range of high frequency words accurately",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.1.5 Describe people, places and objects using suitable statements"
            ]
        },
        "Unit 2: Days (World of Self, Family and Friends)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 4.3.2 Spell a range of high frequency words accurately",
                "1.2.2 Understand with support specific information and details & 2.1.4 Ask about and describe future plans",
                "1.3.1 Guess the meaning of unfamiliar words from clues & 3.2.4 Use with support familiar print and digital resources to check meaning"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "1.2.4 Understand a sequence of supported classroom instructions & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "2.1.4 Ask about and describe future plans & 4.2.2 Ask for, give and respond to simple advice"
            ],
            "Reading": [
                "3.3.1 Read and enjoy A2 fiction/non-fiction print and digital texts & 4.3.2 Spell a range of high-frequency words accurately",
                "2.1.1 Give detailed information about themselves & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 2.3.1 Narrate short basic stories and events"
            ],
            "Writing": [
                "4.2.4 Describe people, places and objects using suitable statements & 2.3.1 Narrate short basic stories and events",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 1.2.5 Understand a sequence of supported questions",
                "4.2.1 Give detailed information about themselves & 2.1.5 Describe people, places and objects using suitable statements",
                "2.2.1 Keep interaction going in short exchanges & 4.2.1 Give detailed information about themselves",
                "3.2.2 Understand specific information and details of two paragraphs or more & 4.3.3 Produce a plan or draft of one or two paragraphs"
            ],
            "Language Arts": [
                "5.2.1 Explain in simple language why they like or dislike an event & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.1.2 Find out about and Describe experiences up to now",
                "5.2.1 Explain in simple language why they like or dislike an event & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly through creating simple action songs & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts"
            ]
        },
        "Unit 3: Wild Life (World of Knowledge)": {
            "Listening": [
                "1.2.2 Understand with support specific information and details & 2.2.1 Keep interaction going in short exchanges",
                "1.2.1 Understand with support the main idea of longer simple texts & 2.2.1 Keep interaction going in short exchanges",
                "1.1.1 Recognise and reproduce with little or no support & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts"
            ],
            "Speaking": [
                "2.1.5 Describe people, places and objects using suitable statements & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "1.2.5 Understand a sequence of supported questions & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "2.2.1 Keep interaction going in short exchanges & 4.3.2 Spell a range of high-frequency words accurately"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues & 3.3.1 Read and enjoy A2 fiction/non-fiction print and digital texts",
                "2.1.2 Find out about and Describe experiences up to now & 4.3.2 Spell a range of high-frequency words accurately",
                "3.3.1 Read and enjoy A2 fiction/non-fiction print and digital texts & 1.2.1 Understand with support the main idea of longer simple texts"
            ],
            "Writing": [
                "2.1.5 Describe people, places and objects using suitable statements & 4.3.2 Spell a range of high-frequency words accurately",
                "3.2.2 Understand specific information and details of two paragraphs or more & 4.2.4 Describe people, places and objects using suitable statements",
                "4.3.3 Produce a plan or draft of one or two paragraphs & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly & 4.2.4 Describe people, places and objects using suitable statements",
                "4.3.2 Spell a range of high-frequency words accurately & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "4.3.2 Spell a range of high-frequency words accurately & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.2.1 Explain in simple language why they like or dislike an event & 2.1.5 Describe people, places and objects using suitable statements"
            ]
        },
        "Unit 4: Learning World (World of Self, Family and Friends)": {
            "Listening": [
                "1.3.1 Guess the meaning of unfamiliar words from clues & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts",
                "1.2.5 Understand a sequence of supported questions & 1.2.2 Understand with support specific information and details",
                "1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes & 2.2.1 Keep interaction going in short exchanges",
                "1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes & 2.2.1 Keep interaction going in short exchanges"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves & 4.2.1 Give detailed information about themselves",
                "2.1.2 Find out about and Describe experiences up to now & 2.2.1 Keep interaction going in short exchanges",
                "2.1.5 Describe people, places and objects using suitable statements & 1.2.4 Understand a sequence of supported classroom instructions"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of two paragraphs or more & 2.1.2 Find out about and Describe experiences up to now",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 4.2.4 Describe people, places and objects using suitable statements",
                "3.2.1 Understand the main idea of simple texts of two paragraphs or more & 2.1.1 Give detailed information about themselves"
            ],
            "Writing": [
                "4.3.2 Spell a range of high-frequency words accurately & 1.3.1 Guess the meaning of unfamiliar words from clues",
                "4.2.4 Describe people, places and objects using suitable statements & 2.2.1 Keep interaction going in short exchanges",
                "4.2.4 Describe people, places and objects using suitable statements & 2.2.2 Agree on a set of basic steps needed to complete short classroom tasks",
                "5.2.1 Explain in simple language why they like or dislike an event & 3.2.2 Understand specific information and details of two paragraphs or more",
                "4.3.2 Spell a range of high-frequency words accurately & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "4.3.3 Produce a plan or draft of one or two paragraphs & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.3.3 Produce a plan or draft of one or two paragraphs"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.3.3 Produce a plan or draft of one or two paragraphs"
            ]
        },
        "Unit 5: Food and Health (World of Knowledge)": {
            "Listening": [
                "1.2.1 Understand with support the main idea of longer simple texts & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "1.2.3 Understand with support longer simple narratives & 1.2.5 Understand a sequence of supported questions",
                "1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "1.2.5 Understand longer supported questions & 1.2.2 Understand with support specific information and details of longer simple texts"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately",
                "2.2.1 Keep interaction going in short exchanges & 2.2.2 Agree on a set of basic steps needed to complete short classroom tasks",
                "2.1.1 Give detailed information about themselves & 1.2.5 Understand a sequence of supported questions"
            ],
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts & 2.1.3 Ask for, give and respond to simple advice",
                "3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts & 2.3.1 Narrate short basic stories and events",
                "3.2.2 Understand specific information and details of simple texts & 4.3.2 Spell most high frequency words accurately in guided writing",
                "3.2.2 Understand specific information and details of simple texts & 3.2.3 Guess the meaning of unfamiliar words from clues"
            ],
            "Writing": [
                "4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "5.2.1 Explain in simple language why they like or dislike an event & 2.1.4 Ask about and describe future plans",
                "4.2.3 Narrate factual events and experiences of interest & 2.2.2 Agree on a set of basic steps needed to complete short classroom tasks",
                "4.2.1 Give detailed information about themselves & 2.1.3 Ask for, give and respond to simple advice",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 1.2.2 Understand with support specific information and details",
                "4.2.2 Ask for, give and respond to simple advice & 2.1.3 Ask for, give and respond to simple advice",
                "4.3.3 Produce a plan or draft of one or two paragraphs & 4.2.5 Connect sentences into one or two coherent paragraphs",
                "5.2.1 Explain in simple language why they like or dislike an event & 2.1.1 Give detailed information about themselves",
                "4.3.2 Spell most high frequency words accurately & 4.3.1 Use capital letters, full stops, question marks and commas in lists appropriately",
                "4.1.2 Use cursive writing in written work & 4.3.2 Spell most high frequency words accurately in guided writing"
            ],
            "Language Arts": [
                "5.2.1 Say in simple words and phrases how a text makes them feel & 3.3.1 Read and enjoy A1 fiction/non-fiction print and digital texts",
                "5.3.1 Respond imaginatively through creating picture stories & 2.2.2 Check steps needed to complete short classroom tasks",
                "5.3.1 Respond imaginatively through creating picture stories & 2.1.1 Explain and give reasons for basic opinions"
            ]
        },
        "Unit 6: Sport (World of Knowledge)": {
            "Listening": [
                "1.3.1 Guess the meaning of unfamiliar words from clues & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "1.2.3 Understand with support longer simple narratives & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "1.2.4 Understand a sequence of supported classroom instructions & 2.2.1 Keep interaction going in short exchanges"
            ],
            "Speaking": [
                "2.3.1 Narrate short basic stories and events & 1.2.1 Understand with support the main idea of longer simple texts",
                "2.1.2 Find out about and Describe experiences up to now & 1.2.5 Understand a sequence of supported questions",
                "1.3.1 Guess the meaning of unfamiliar words from clues & 3.2.1 Understand the main idea of simple texts of two paragraphs or more"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of two paragraphs or more & 3.2.4 Use with support familiar print and digital resources to check meaning",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "2.3.1 Narrate short basic stories and events & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately"
            ],
            "Writing": [
                "4.2.3 Narrate factual events and experiences of interest & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.2.2 Agree on a set of basic steps needed to complete short classroom tasks",
                "4.2.3 Narrate factual events and experiences of interest & 2.1.2 Find out about and Describe experiences up to now",
                "4.3.2 Spell a range of high-frequency words accurately & 2.1.1 Give detailed information about themselves",
                "5.2.1 Explain in simple language why they like or dislike an event & 4.2.5 Connect sentences into one or two coherent paragraphs",
                "3.2.2 Understand specific information and details of two paragraphs or more & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts",
                "4.3.3 Produce a plan or draft of one or two paragraphs & 4.2.5 Connect sentences into one or two coherent paragraphs",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.3.1 Narrate short basic stories and events"
            ]
        },
        "Unit 7: Growing Up (World of Knowledge)": {
            "Listening": [
                "1.1.1 Recognise and reproduce with little or no support & 2.1.1 Give detailed information about themselves",
                "1.2.2 Understand with support specific information and details & 1.2.5 Understand a sequence of supported questions",
                "1.2.4 Understand a sequence of supported classroom instructions & 2.1.2 Find out about and Describe experiences up to now"
            ],
            "Speaking": [
                "2.1.5 Describe people, places and objects using suitable statements & 1.2.4 Understand a sequence of supported classroom instructions",
                "1.2.3 Understand with support longer simple narratives & 3.2.3 Guess the meaning of unfamiliar words from clues",
                "2.1.3 Ask for, give and respond to simple advice & 4.2.2 Ask for, give and respond to simple advice"
            ],
            "Reading": [
                "3.2.4 Use with support familiar print and digital resources to check meaning & 2.1.5 Describe people, places and objects using suitable statements",
                "2.1.1 Give detailed information about themselves & 4.2.1 Give detailed information about themselves",
                "3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately"
            ],
            "Writing": [
                "4.2.1 Give detailed information about themselves & 3.2.1 Understand the main idea of simple texts of two paragraphs or more",
                "5.2.1 Explain in simple language why they like or dislike an event & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 4.3.2 Spell a range of high-frequency words accurately",
                "4.2.1 Give detailed information about themselves & 2.3.1 Narrate short basic stories and events",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 3.2.2 Understand specific information and details of two paragraphs or more",
                "3.2.4 Use with support familiar print and digital resources to check meaning & 4.3.2 Spell a range of high-frequency words accurately",
                "4.2.5 Connect sentences into one or two coherent paragraphs & 1.1.1 Recognise and reproduce with little or no support a wide range of target language phonemes",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.2.4 Describe people, places and objects using suitable statements",
                "4.3.2 Spell a range of high-frequency words accurately & 1.2.2 Understand with support specific information and details"
            ],
            "Language Arts": [
                "5.2.1 Explain in simple language why they like or dislike an event & 3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.2.4 Describe people, places and objects using suitable statements"
            ]
        },
        "Unit 8: Going Away (World of Knowledge)": {
            "Listening": [
                "1.3.1 Guess the meaning of unfamiliar words from clues & 1.2.2 Understand with support specific information and details",
                "1.3.1 Guess the meaning of unfamiliar words from clues & 1.2.3 Understand with support longer simple narratives",
                "1.2.2 Understand with support specific information and details & 2.1.4 Ask about and describe future plans"
            ],
            "Speaking": [
                "2.1.4 Ask about and describe future plans & 4.2.3 Narrate factual events and experiences of interest",
                "2.2.2 Agree on a set of basic steps needed to complete short classroom tasks & 1.2.5 Understand a sequence of supported questions",
                "1.2.3 Understand with support longer simple narratives & 1.2.2 Understand with support specific information and details"
            ],
            "Reading": [
                "3.2.2 Understand specific information and details of two paragraphs or more & 1.2.3 Understand with support longer simple narratives",
                "3.2.3 Guess the meaning of unfamiliar words from clues & 4.2.5 Connect sentences into one or two coherent paragraphs",
                "2.2.2 Agree on a set of basic steps needed to complete short classroom tasks & 2.3.1 Narrate short basic stories and events"
            ],
            "Writing": [
                "4.3.2 Spell a range of high-frequency words accurately & 2.3.1 Narrate short basic stories and events",
                "5.2.1 Explain in simple language why they like or dislike an event & 2.1.5 Describe people, places and objects using suitable statements",
                "4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately & 4.2.3 Narrate factual events and experiences of interest",
                "4.3.3 Produce a plan or draft of one or two paragraphs & 3.2.2 Understand specific information and details of two paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately",
                "3.3.1 Read and enjoy A2 fiction/ non-fiction print and digital texts & 3.2.2 Understand specific information and details of two paragraphs or more",
                "4.2.3 Narrate factual events and experiences of interest & 2.1.2 Find out about and Describe experiences up to now",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.3.1 Narrate short basic stories and events"
            ],
            "Language Arts": [
                "5.2.1 Explain in simple language why they like or dislike an event & 2.1.5 Describe people, places and objects using suitable statements",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 4.3.1 Use capital letters, full stops, commas in lists and question marks appropriately",
                "5.3.1 Respond imaginatively and intelligibly through creating simple roleplays & 2.3.1 Narrate short basic stories and events"
            ]
        }
    },
    "Year 6": {
        "Unit 0: Welcome (World of Self, Family and Friends)": {
            "Reading": ["3.2.1 Understand specific information and details of simple longer texts & 4.2.4 Describe personality"],
            "Writing": ["4.2.1 Give detailed information about themselves and others & 2.1.1 Give detailed information about themselves and others"],
            "Listening": ["1.2.2 Understand specific information and details & 1.1.1 Recognise and reproduce independently a wide range of target language phonemes"],
            "Speaking": ["4.2.1 Give detailed information about themselves and others & 2.1.1 Give detailed information about themselves and others"],
            "Language Arts": ["5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 1.1.1 Recognise and reproduce independently a wide range of target language phonemes"]
        },
        "Unit 1: It's an Emergency (World of Knowledge)": {
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues & 3.2.2 Understand specific information and details of simple longer texts",
                "3.2.2 Understand specific information and details of simple longer texts & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately"
            ],
            "Writing": [
                "4.2.3 Narrate factual and imagined events and experiences & 2.3.1 Narrate short stories, events and experiences",
                "4.2.3 Narrate factual and imagined events and experiences & 4.3.3 Produce a plan or draft of two paragraphs or more"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 1.2.1 Understand main idea",
                "1.2.2 Understand specific information and details & 2.1.3 Explain and give reasons for simple advice"
            ],
            "Speaking": [
                "2.3.1 Narrate short stories, events and experiences & 3.2.2 Understand specific information and details of simple longer texts",
                "2.3.1 Narrate short stories, events and experiences & 1.2.5 Understand more complex supported questions"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 2.1.5 Ask about and describe personality",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.3.2 Spell most high frequency words accurately"
            ]
        },
        "Unit 2: Life in the Past (World of Knowledge)": {
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues & 3.2.1 Understand the main idea of simple longer texts",
                "3.2.1 Understand the main idea of simple longer texts & 3.2.2 Understand specific information and details of simple longer texts",
                "3.2.2 Understand specific information and details of simple longer texts & 1.2.5 Understand more complex supported questions"
            ],
            "Writing": [
                "4.3.3 Produce a plan or draft of two paragraphs or more & 3.2.1 Understand the main idea of simple longer texts",
                "4.2.3 Narrate factual and imagined events and experiences & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately"
            ],
            "Listening": [
                "1.1.1 Recognise and reproduce independently a wide range of target language phonemes & 1.2.5 Understand more complex supported questions",
                "1.2.2 Understand specific information and details & 4.3.2 Spell most high frequency words accurately",
                "4.2.3 Narrate factual and imagined events and experiences & 3.2.4 Use with some support familiar print and digital resources",
                "1.2.1 Understand main idea & 2.1.4 Ask about and describe future plans or events"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 4.2.1 Give detailed information about themselves and others",
                "2.2.2 Agree a set of basic steps needed to complete extended classroom tasks & 2.1.4 Ask about and describe future plans or events",
                "2.2.1 Keep interaction going in short exchanges & 2.1.4 Ask about and describe future plans or events"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 2.1.1 Give detailed information about themselves and others"
            ]
        },
        "Unit 3: Adventure Time (World of Self, Family and Friends)": {
            "Reading": [
                "3.2.1 Understand the main idea of simple longer texts & 3.2.2 Understand specific information and details of simple longer texts",
                "3.2.2 Understand specific information and details of simple longer texts & 4.3.3 Produce a plan or draft of two paragraphs or more"
            ],
            "Writing": [
                "4.2.1 Give detailed information about themselves and others & 3.2.2 Understand specific information and details of simple longer texts",
                "4.3.3 Produce a plan or draft of two paragraphs or more & 4.2.3 Narrate factual and imagined events and experiences",
                "4.2.5 Connect sentences into two coherent paragraphs or more & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately"
            ],
            "Listening": [
                "1.2.5 Understand more complex supported questions & 2.1.1 Give detailed information about themselves and others",
                "1.2.2 Understand specific information and details & 1.3.1 Guess the meaning of unfamiliar words from clues",
                "1.2.2 Understand specific information and details & 1.3.1 Guess the meaning of unfamiliar words from clues"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 1.2.5 Understand more complex supported questions",
                "2.3.1 Narrate short stories, events and experiences & 1.2.3 Understand longer simple narratives",
                "2.1.1 Give detailed information about themselves and others & 1.2.5 Understand more complex supported questions"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 2.3.1 Narrate short stories, events and experiences",
                "5.2.1 Describe in simple language a character’s actions or feelings & 3.3.1 Read and enjoy A2 fiction/nonfiction texts",
                "3.3.1 Read and enjoy A2 fiction/nonfiction texts & 3.2.1 Understand the main idea of simple longer texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 3.2.2 Understand specific information and details of simple longer texts"
            ]
        },
        "Unit 4: Cool Jobs (World of Self, Family and Friends)": {
            "Reading": [
                "3.2.3 Guess the meaning of unfamiliar words from clues & 3.2.4 Use with some support familiar print and digital resources",
                "2.1.1 Give detailed information about themselves and others & 1.2.5 Understand more complex supported questions",
                "3.2.2 Understand specific information and details of simple longer texts & 4.2.1 Give detailed information about themselves and others",
                "3.2.2 Understand specific information and details of simple longer texts & 4.3.2 Spell most high frequency words accurately"
            ],
            "Writing": [
                "4.2.1 Give detailed information about themselves and others & 3.2.2 Understand specific information and details of simple longer texts",
                "4.2.1 Give detailed information about themselves and others & 4.2.4 Describe Personality",
                "4.2.2 Describe future plans or events & 3.2.2 Understand specific information and details of simple longer texts"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 1.2.5 Understand more complex supported questions",
                "1.2.1 Understand main idea & 1.3.1 Guess the meaning of unfamiliar words from clues",
                "1.2.5 Understand more complex supported questions & 1.3.1 Guess the meaning of unfamiliar words from clues"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 4.3.2 Spell most high frequency words accurately",
                "2.2.1 Keep interaction going in short exchanges & 3.2.2 Understand specific information and details of simple longer texts"
            ],
            "Language Arts": [
                "5.2.1 Describe in simple language a character’s actions or feelings & 4.3.2 Spell most high frequency words accurately",
                "5.2.1 Describe in simple language a character’s actions or feelings & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately",
                "5.2.1 Describe in simple language a character’s actions or feelings & 4.3.2 Spell most high frequency words accurately"
            ]
        },
        "Unit 5: Getting Around (World of Stories)": {
            "Reading": [
                "3.3.1 Read and enjoy A2 fiction/nonfiction texts & 3.2.1 Understand the main idea of simple longer texts",
                "3.2.1 Understand the main idea of simple longer texts & 2.3.1 Narrate short stories, events and experiences",
                "3.2.2 Understand specific information and details of simple longer texts & 4.2.5 Connect sentences into two coherent paragraphs or more"
            ],
            "Writing": [
                "4.2.5 Connect sentences into two coherent paragraphs or more & 1.2.3 Understand longer simple narratives",
                "4.2.3 Narrate factual and imagined events and experiences & 1.2.3 Understand longer simple narratives",
                "4.3.3 Produce a plan or draft of two paragraphs or more & 4.2.5 Connect sentences into two coherent paragraphs or more"
            ],
            "Listening": [
                "1.1.1 Recognise and reproduce independently a wide range of target language phonemes & 3.2.2 Understand specific information and details of simple longer texts",
                "1.2.2 Understand specific information and details & 1.3.1 Guess the meaning of unfamiliar words from clues",
                "1.2.5 Understand more complex supported questions & 1.1.1 Recognise and reproduce independently a wide range of target language phonemes"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 2.1.3 Explain and give reasons for simple advice",
                "2.1.2 Ask about and express rules and obligations & 2.2.2 Agree a set of basic steps needed to complete extended classroom tasks",
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand more complex supported questions"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 3.3.1 Read and enjoy A2 fiction/nonfiction texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 3.3.1 Read and enjoy A2 fiction/nonfiction texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.2.1 Give detailed information about themselves and others"
            ]
        },
        "Unit 6: How is it made? (World of Knowledge)": {
            "Reading": [
                "3.2.4 Use with some support familiar print and digital resources & 3.2.1 Understand the main idea of simple longer texts",
                "3.2.2 Understand Specific information and details of simple longer texts & 4.3.2 Spell most high frequency words accurately",
                "3.2.2 Understand Specific information and details of simple longer texts & 2.1.1 Give detailed information about themselves and others"
            ],
            "Writing": [
                "4.3.2 Spell most high frequency words accurately & 1.1.1 Recognise and Reproduce independently a wide range of target language phonemes",
                "4.2.5 Connect sentences into two coherent paragraphs or more & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately",
                "4.3.3 Produce a plan or draft of two paragraphs or more & 3.2.2 Understand Specific information and details of simple longer texts"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 3.2.2 Understand Specific information and details of simple longer texts",
                "1.2.2 Understand specific information and details & 2.1.1 Give detailed information about themselves and others",
                "1.2.2 Understand specific information and details & 1.2.1 Understand with little or no support the main idea"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 1.2.5 Understand more Complex supported questions",
                "2.2.2 Agree a set of basic steps needed to complete extended classroom tasks & 1.2.4 Understand longer sequences of supported classroom instructions",
                "2.1.3 Explain and give reasons for simple advice & 4.3.3 Produce a plan or draft of two paragraphs or more"
            ],
            "Language Arts": [
                "5.2.1 Describe in simple language a character’s actions or feelings & 2.1.1 Give detailed information about themselves and others",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.3.2 Spell most high frequency words accurately"
            ]
        },
        "Unit 7: Music & Song (World of Self, Family and Friends)": {
            "Reading": [
                "3.2.1 Understand the main idea of simple longer texts & 1.2.1 Understand with little or no support the main idea",
                "3.2.1 Understand the main idea of simple longer texts & 1.1.1 Recognise and Reproduce independently a wide range of target language phonemes",
                "3.2.1 Understand the main idea of simple longer texts & 2.3.1 Narrate short stories, events and experiences"
            ],
            "Writing": [
                "4.2.1 Give detailed information about themselves and others & 2.1.5 Ask about and Describe personality",
                "4.3.2 Spell most high frequency words accurately & 1.1.1 Recognise and Reproduce independently a wide range of target language phonemes",
                "4.2.1 Give detailed information about themselves and others & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 2.1.4 Ask about and describe future plans or events",
                "1.3.1 Guess the meaning of unfamiliar words & 3.2.2 Understand Specific information and details of simple longer texts",
                "1.2.3 Understand longer simple narratives & 3.3.1 Read and enjoy A2 fiction/nonfiction print and digital texts"
            ],
            "Speaking": [
                "2.1.4 Ask about and describe future plans or events & 4.2.2 Describe future plans or events",
                "2.1.1 Give detailed information about themselves and others & 4.2.5 Connect sentences into two coherent paragraphs or more",
                "2.1.1 Give detailed information about themselves and others & 2.2.1 Keep interaction going in short exchanges"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 2.2.1 Keep interaction going in short exchanges",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.3.2 Spell most high frequency words accurately"
            ]
        },
        "Unit 8: Tell me a story (World of Stories)": {
            "Reading": [
                "3.2.1 Understand the main idea of simple longer texts & 3.3.1 Read and enjoy A2 fiction/nonfiction print and digital texts",
                "3.2.2 Understand Specific information and details of simple longer texts & 3.2.1 Understand the main idea of simple longer texts",
                "3.2.1 Understand the main idea of simple longer texts & 2.1.3 Explain and give reasons for simple advice"
            ],
            "Writing": [
                "4.2.3 Narrate factual and imagined events and experiences & 3.2.2 Understand Specific information and details of simple longer texts",
                "4.2.3 Narrate factual and imagined events and experiences & 3.2.1 Understand the main idea of simple longer texts",
                "4.3.3 Produce a plan or draft of two paragraphs or more & 4.2.3 Narrate factual and imagined events and experiences"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 2.1.4 Ask about and describe future plans or events",
                "1.2.3 Understand longer simple narratives & 1.2.1 Understand with little or no support the main idea",
                "1.2.2 Understand specific information and details & 1.2.1 Understand with little or no support the main idea"
            ],
            "Speaking": [
                "2.1.4 Ask about and describe future plans or events & 4.2.2 Describe future plans or events",
                "2.3.1 Narrate short stories, events and experiences & 1.2.5 Understand more Complex supported questions"
            ],
            "Language Arts": [
                "5.2.1 Describe in simple language a character’s actions or feelings & 2.3.1 Narrate short stories, events and experiences",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 3.3.1 Read and enjoy A2 fiction/nonfiction print and digital texts",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.2.5 Connect sentences into two coherent paragraphs or more"
            ]
        },
        "Unit 9: What’s your opinion? (World of Knowledge)": {
            "Reading": [
                "3.2.1 Understand the main idea of simple longer texts & 3.2.3 Guess the meaning of unfamiliar words",
                "3.2.2 Understand Specific information and details of simple longer texts & 3.2.1 Understand the main idea of simple longer texts",
                "3.2.2 Understand Specific information and details of simple longer texts & 3.3.1 Read and enjoy A2 fiction/nonfiction print and digital texts"
            ],
            "Writing": [
                "4.2.1 Give detailed information about themselves and others & 4.2.5 Connect sentences into two coherent paragraphs or more",
                "4.3.3 Produce a plan or draft of two paragraphs or more & 4.2.5 Connect sentences into two coherent paragraphs or more",
                "4.2.1 Give detailed information about themselves and others & 2.1.4 Ask about and describe future plans or events"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 2.1.1 Give detailed information about themselves and others",
                "1.2.2 Understand specific information and details & 1.2.1 Understand with little or no support the main idea",
                "1.2.3 Understand longer simple narratives & 2.2.2 Agree a set of basic steps needed to complete extended classroom tasks"
            ],
            "Speaking": [
                "2.1.1 Give detailed information about themselves and others & 1.2.5 Understand more Complex supported questions",
                "2.2.1 Keep interaction going in short exchanges & 1.2.2 Understand specific information and details of longer simple texts",
                "1.2.2 Understand specific information and details & 2.1.1 Give detailed information about themselves and others"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.2.5 Connect sentences into two coherent paragraphs or more",
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 4.2.5 Connect sentences into two coherent paragraphs or more",
                "5.2.1 Describe in simple language a character’s actions or feelings & 2.1.1 Give detailed information about themselves and others"
            ]
        },
        "Unit 10: It’s a mystery! (World of Stories)": {
            "Reading": [
                "3.2.2 Understand Specific information and details of simple longer texts & 2.1.5 Ask about and describe personality",
                "2.2.1 Keep interaction going in short exchanges & 3.2.2 Understand Specific information and details of simple longer texts"
            ],
            "Writing": [
                "4.2.3 Narrate factual and imagined events and experiences & 3.2.2 Understand Specific information and details of simple longer texts",
                "4.2.3 Narrate factual and imagined events and experiences & 4.3.1 Use capital letters, full stops, commas in lists, question marks, and speech marks appropriately"
            ],
            "Listening": [
                "1.2.2 Understand specific information and details & 2.1.2 Ask about and express rules and obligations",
                "1.2.2 Understand specific information and details & 4.3.2 Spell most high frequency words accurately"
            ],
            "Speaking": [
                "2.2.1 Keep interaction going in short exchanges & 1.2.5 Understand more Complex supported questions",
                "2.3.1 Narrate short stories, events and experiences & 1.2.5 Understand more Complex supported questions",
                "2.3.1 Narrate short stories, events and experiences & 1.2.5 Understand more Complex supported questions"
            ],
            "Language Arts": [
                "5.3.1 Respond imaginatively and intelligibly through creating simple stories and simple poems & 3.3.1 Read and enjoy A2 fiction/nonfiction print and digital texts",
                "5.2.1 Describe in simple language a character’s actions or feelings & 2.1.1 Give detailed information about themselves and others",
                "5.2.1 Describe in simple language a character’s actions or feelings & 2.1.1 Give detailed information about themselves and others"
            ]
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
   
   **Success Criteria:** (Leave a blank line after this header)
   
   **1.** Pupils can [measurable action related to main objective].
   
   **2.** Pupils can [measurable action related to complementary objective].

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

    # Dynamic Units based on Year
    unit_options = list(SYLLABUS_DB[selected_year].keys())
    selected_unit = st.selectbox("2. Topic / Unit", unit_options)

    # Dynamic Skills based on Unit
    # Get available skills from DB
    available_skills = list(SYLLABUS_DB[selected_year][selected_unit].keys())
    
    # Define custom order
    skill_order = ["Listening", "Speaking", "Reading", "Writing", "Language Arts"]
    
    # Sort: specific order first, then alphabetical for anything else (unlikely)
    skill_options = sorted(available_skills, key=lambda x: skill_order.index(x) if x in skill_order else len(skill_order))
    
    selected_skill = st.selectbox("3. Focus Skill", skill_options)

    # Dynamic LS based on Skill
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
