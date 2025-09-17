import streamlit as st
import pandas as pd
from main import processar_pasta

st.title("Analisador de Currículos")
st.write("Coloque os currículos na pasta 'curriculos' e clique abaixo")

if st.button("Analisar"):
    df = processar_pasta('curriculos')
    st.dataframe(df)
    st.success("Análise Concluída!")