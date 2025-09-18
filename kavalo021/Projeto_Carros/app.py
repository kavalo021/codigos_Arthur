import streamlit as st

st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha o carro ideal para voce!")
carros = ["gol", "bmw", "toro","corsa"]
st.sidebar.selectbox("selecione o modelo do carro:", carros)
st.title("maximus cars - aluguel de carros")
st.image(f"(opção), png")
st.markdown(f"## voce alugou o modelo: {opção}")
st.markdown("")