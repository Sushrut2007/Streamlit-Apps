"""
3.Dynamic_Markdown_Previewer.py

Module 1 Exercise: Introduction & Setup - Dynamic Markdown Previewer

Objective:
- Build on previous exercises (1.Hello_Streamlit.py and 2.Display_Content.py)
- Practice dynamic content creation in Python using strings, lists, loops, and basic formatting
- Simulate Markdown output that could later be used in Streamlit

Exercise Description:
- The user will create a summary of a specific topic (e.g., "My Favorite Space Missions")
- The program will take the following inputs from the user:
    1. Title of the summary
    2. Subtitle or description
    3. A short paragraph about the topic
    4. A list of items (e.g., favorite missions or key points)
    5. Optionally, select words or phrases from the paragraph/items to highlight (bold/italic)
    6. Additional facts or numbers related to each item (to display as a numbered list)
- The program will combine all inputs into a **single Markdown-formatted string**
- Output should dynamically reflect **user inputs and selected highlights**
- Optional: add emojis or decorative lines to make it visually appealing

Learning Goals:
- Understand how to handle **user input** and **store it in lists/variables**
- Learn **dynamic string manipulation and Markdown formatting**
- Prepare for interactive widgets in **Module 2**
"""


import streamlit as st


# Format Title & Tagline
def format_title_tagline(title, tagline):
    # These will be passed to st.markdown(title) or tagline as a literal string, which is actually formatted text
    title = f'## {title}'
    tagline = f'###### *{tagline}*'

    return title, tagline


# Format paragraph description (including words to be bold) and bullet points
def format_paragraph(text, words):
    # separate text by '.' and filter out empty strings (extra '-' problem solution)
    seperated_text = [sentence.strip() for sentence in text.split('.') if sentence.strip()] # list of sentences / points
    
    # for each sentence, add '-', so that st.markdown() can convert '-' to bullet point
    for i in range(len(seperated_text)): # i will be a sentence
        seperated_text[i] = f'- {seperated_text[i]}'
     
    
    # check if user dont want to bold specific words
    if not words:
        return '\n'.join (seperated_text) # just format as a literal text for each sentence in the list

    else:
        # convert words into a list
        word_list = [word.strip() for word in words.split(',')]
        
        # process each sentence
        processed_sentence = []
        # format each specified word with **word**
        for sentence in seperated_text:
            formatted_sentence = sentence # backup variable to hold each formatted sentence
            
            for word in word_list:
                formatted_sentence = formatted_sentence.replace(word, f'**{word}**')
    
            processed_sentence.append(formatted_sentence)
        
        return  '\n'.join(processed_sentence)


# format space mission list
def format_list(list):
    formatted_missions = [f'{num}. *{mission}*' for num, mission in enumerate(list, start = 1)]
    
    # A very nice approach : 
    # Instead of looping through mission_list & doing st.markdown(i) -> 
    return '\n'.join(formatted_missions) # gives a string, not a list
    
# Title
st.title('📟Dynamic Markdown Previewer')

st.markdown('### Please Enter your information about your favourite space missions')

# Input title of the paragraph/text 
title = st.text_input('**Title** of the paragraph')


# Input a tagline for the text
tagline = st.text_input('**Tagline** describing the topic')


# Input a short paragraph on the topic (notice text_area())
topic_desc = st.text_area('**Short paragraph** describing your topic')


# Optional : Input important words from the paragraph the user wants to be in bold
words_to_be_bold = st.text_input(' **(Optional)** Enter important words to be highlighted as **bold** in the paragraph seperated  by **commas**')

# Input favorite missions list
mission_input = st.text_input('Enter favourite mission list seperated by **commas**')
raw_mission_list = [mission.strip() for mission in mission_input.split(',') if mission_input and mission.strip()]


# ------------------------------------------------------------------------------------------------------
# Display the Markdown Previewer

st.write('Here is your markdown preview!')

if any([title, tagline, topic_desc, words_to_be_bold, raw_mission_list]):
    
    if title or tagline:
    # call format title & tagline
        title, tagline = format_title_tagline(title, tagline)

        st.markdown(title)
        st.markdown(tagline)
    
    if topic_desc:
        sentences = format_paragraph(topic_desc, words_to_be_bold)
        st.markdown(sentences)
        
    if raw_mission_list:
        mission = format_list(raw_mission_list)
        st.markdown(mission)