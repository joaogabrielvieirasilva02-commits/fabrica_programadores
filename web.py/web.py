#Altor: joao gabriel 
#projeto ; minha primeira pagina web 

#importando a biblioteca 
import streamlit as st

st.title('--- Sistema de calculo de imc---')
peso = st.number_input('digite seu peso: ')
altura = st.number_input('digite sua altura: ')
if st.button('calcular imc'):
    if peso > 0 and altura >0:
        imc = peso / (altura ** 2)
        st.success(f'seu imc e: {imc:.2f}!', icon="✅")
        if imc <= 18.5:
            st.error('abixo do peso', icon="🚨")
        elif imc <= 24.9:
            st.success('peso normal!', icon="✅")
        elif imc <= 29.9:
            st.warning('acima do peso!', icon="⚠️")
        elif imc <= 34.9:
            st.warning('obesidade grau I!', icon="⚠️")
        elif imc <= 39.9:
            st.warning('obseidade grau II!', icon="⚠️")
        else:
            st.error('obesidade grau III(mórbida)!', icon="🚨")
    else:
        st.error('digite um numero valido!', icon="🚨")