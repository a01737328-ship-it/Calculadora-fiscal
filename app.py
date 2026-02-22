import streamlit as st
import myabe

st.title("Calculadora Fiscal")

if st.button("Calcular"):
    resultado = myabe.main()
    st.write(resultado)
