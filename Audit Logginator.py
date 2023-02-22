import streamlit as st
import openai
import re

# Load the response model
openai.api_key = "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" # Replace with API key 
model_engine = "text-davinci-002"

# Define the mapping of input phrases and their replacements
input_mapping = {
    r"\b(?!23|7|11|44|16|8|9|\d)\d+\b": "#NUMBER#",
    "7": "Status 7",
    "23": "Status 23",
    "LL": "Landlord",
    "TT": "Tenant",
    "IRR": "Irregularity",
    "POO": "Proof of Ownership",
    "8": "Status 8",
    "9": "Status 9",
    "44": "Status 44",
    "11": "Status 11",
    "ERAP": "Emergency rent asssistant program application",
}

# Define the examples of professional language
professional_examples = [
    "The following statement presents a more formal and polished language:",
    "To convey the same message in a more professional tone:",
    "Here's an example of a more sophisticated and refined phrasing:"
    "In consideration of the above, we propose the following course of action:"
    "The data suggests that a more nuanced approach may be appropriate in this context."
    "It is our belief that a comprehensive review of the relevant literature is essential to making informed decisions in this area."
]

# Define the layout of the Streamlit app
st.title("The Script")
user_input = st.text_area("You: ", height=200)
chat_output = st.empty()

# Generate paraphrased version of user input
if user_input:
    with st.spinner("Thinking..."):
        # Replace input phrases with their corresponding replacements
        for key, value in input_mapping.items():
            user_input = re.sub(key, value, user_input)

        # Separate numbers from words
        user_input = re.sub(r"\b(?!23|7|11|44|16|8|9|\d)\d+\b", r"#NUMBER#", user_input)

        # Include professional examples as prompts for the model
        prompts = professional_examples + [f"Paraphrase the following text in a more professional manner:\n{user_input}"]

        paraphrase_response = openai.Completion.create(
            engine=model_engine,
            prompt="\n".join(prompts),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        paraphrase = paraphrase_response.choices[0].text.strip()

        # Replace special symbols with original numbers
        paraphrase = re.sub(r"#NUMBER#", r"\g<0>", paraphrase)

        # Rewrite the user input as an audit log note and put it in a box with height 200
        audit_log_note = f"User input: {user_input}\n\nAudit Log Note: {paraphrase}"
        chat_output_box = st.text_area("TrailLogger:", value=paraphrase, height=200)

       


