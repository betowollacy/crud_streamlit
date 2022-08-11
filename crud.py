import streamlit as st;
import pandas as pd
import numpy as np
import random



st.header("Usando Streamlit para coleta de dados")

with st.form(key="includ_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sua idade",format="%d", step=1)
    input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor", "Musico", "Desiner", "Professor"])
    input_button_submit = st.form_submit_button("Enviar")


if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade: {input_age} Anos')
    st.write(f'Ocupação: {input_occupation}')



