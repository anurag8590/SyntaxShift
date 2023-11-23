import streamlit as st
from openai import OpenAI

st.set_page_config(layout="wide")   # to start with default wide screen.

# reading the file contents from the code file.
def read_file_content(uploaded_file):
    try:
        content = uploaded_file.read().decode("utf-8") 
        return content
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        return None
    

# title of the web app.
st.title('Syntax Shift by OpenAI 🚀')

# OpenAPI key
api_key = st.text_input('Enter your OpenAI API.')

client = OpenAI(api_key=api_key)




####################################################
# following code maps the options, when user select one option and it shows rest of other options.
# options_mapping = {
#     "C++": ["Java", "Python3","Javascript"],
#     "Java": ["C++", "Python3","Javascript"],
#     "Python3": ["C++", "Java","Javascript"],
#     "Javascript":["C++","Java","Python3"]
# }

# option_1 = list(options_mapping.keys())

# lang1 = st.sidebar.selectbox("Original Language", option_1)

# option_2 = options_mapping.get(lang1, [])

# lang2 = st.sidebar.selectbox("Convert to?", option_2)
####################################################

lang1 = st.sidebar.text_input('Original Language?')
lang2 = st.sidebar.text_input('Convert to?')

col1, col2 = st.columns(2)

with col1:
    code = st.text_area('Enter the code you want to convert.')

with col2:

    code_file = st.file_uploader("or Upload a file!!",)

    if code_file is not None:

        code = read_file_content(code_file)

# execution will start when hit the convert button.
if(st.button('Convert!!')):
    
    def generate_code(prompt): 
        
        response = client.completions.create(
            model="text-davinci-003",  
            prompt=prompt,
            temperature = 0.1,
            max_tokens=1024 
        )

        
        generated_code = response.choices[0].text

        return generated_code

    code_prompt = f'''You are a code converter , you have to convert the following {lang1} code to {lang2} code.

                {code}

            '''

    
    generated_code_response = generate_code(code_prompt)

    st.code(generated_code_response,language='lang2')



footer = st.empty()

# add the markdown content at the bottom
footer.markdown("[![Title](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/anurag8590)")


