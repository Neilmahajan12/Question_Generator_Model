
# import streamlit as st
# from google import genai
import os
api_key = os.getenv("GEMINI_API_KEY")
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


# # Initialize Gemini Client
# genai_client = genai.Client(api_key=api_key)

# # Streamlit UI
# st.title("📖 Question Generator with Gemini")

# # User input paragraph
# paragraph = st.text_area("Enter a paragraph:", height=200)

# # Button to generate questions
# if st.button("Generate Questions"):
#     if not paragraph.strip():
#         st.warning("Please enter a paragraph first.")
#     else:
#         with st.spinner("Generating questions..."):
#             try:
#                 # Format input prompt
#                 prompt = f"""Generate 10 to 12 high-quality questions based on the following paragraph:
                
# {paragraph}

# Only return the questions as bullet points or numbered list."""
                
#                 # Call Gemini model
#                 response = genai_client.models.generate_content(
#                     model="gemini-2.0-flash",
#                     contents=prompt
#                 )

#                 # Display questions
#                 st.subheader("📝 Generated Questions:")
#                 st.markdown(response.text)
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")





# this is flask code of above model 


from flask import Flask, render_template, request
from google import genai

# Initialize Gemini client with your API key
genai_client = genai.Client(api_key=api_key)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    questions = None
    error = None

    if request.method == 'POST':
        paragraph = request.form.get('paragraph')

        if not paragraph.strip():
            error = "Please enter a paragraph."
        else:
            try:
                prompt = f"""Generate 10 to 12 high-quality questions based on the following paragraph:

{paragraph}

Only return the questions as bullet points or numbered list."""

                response = genai_client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                questions = response.text.strip()
            except Exception as e:
                error = f"An error occurred: {e}"

    return render_template('home.html', questions=questions, error=error)

if __name__ == '__main__':
    app.run(debug=True)
