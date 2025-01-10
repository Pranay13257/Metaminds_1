import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "e0bff40c-a61e-4aad-9b09-7b1eaac2a17b"
FLOW_ID = "f06fcbcc-3704-4a7f-8d41-2a8bf38b4d7f"
APPLICATION_TOKEN = "AstraCS:cZmnppbdotlURNekdWwcXZpN:a46f141b5bbac9b3a8e60dbbbac89e1002f6099cdf05cb143f9d6a9b7ff06331"
ENDPOINT = "metaminds_1"


def run_flow(message:str)-> dict:
    api_url=f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload={
        "input_value": message,
        "output_type":"chat",
        "input_type":"chat",
    }
    headers ={"Authorization ":"Bearer "+APPLICATION_TOKEN,"Content-Type":"application/json"}
    response=requests.post(api_url,json=payload,headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    message=st.text_area("Message",placeholder="Ask Your Query......")
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
        try:
            with st.spinner("Running Flow...."):
                response= run_flow(message)
            response =response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))
if __name__=="__main__":
    main()
            
    
