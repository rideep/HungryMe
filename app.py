from openai import OpenAI
import streamlit as st

#auth
client = OpenAI(api_key=st.secrets["api_key"])

#Title
st.title("HungryMe")

st.header("Getting you deliciously fed!")

instructions = st.text_area(
    "Tell me what you want to eat and I will tell you:Specify Breakfast,Lunch or Dinner"
)

if len(instructions)<1000:
    if st.button("Show Options"):
        response = client.chat.completions.create(
            model ="gpt-4o-mini",
            messages=[
                {"role":"system","content":"You are a personal chef who gives delicious food suggestions:"+prompt},
                {"role":"user","content":instructions}
                
            ],
            temperature=0,
            max_tokens=100,
            stop = None
        )
        message= response.choices[0].message.content
        st.subheader("Here’s what I suggest:")
        st.write(message)
    else:
        st.warning("input too large!write less than 1000 words and try again!")