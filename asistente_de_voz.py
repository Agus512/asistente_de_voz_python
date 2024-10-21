from streamlit_mic_recorder import speech_to_text  #Reconocimiento de audio
from langchain_openai import ChatOpenAI  #GPT-4
import streamlit as st  #Graficos


openai_api_key = "insertar api key"

#Inicializa
llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key)

#Streamlit
st.title("Tu asistente de Voz Todo en Uno")
st.write("Aplicación de chat habilitada por voz")

text = speech_to_text(language="es", use_container_width=True, just_once=False, key="STT")

if text:
    st.write("Tu: ", text)
    response = llm(text)  
    st.write("Respuesta del modelo: ", response.content)
