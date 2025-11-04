import streamlit as st
from src.auth import registrar, verificar

st.title("🔐 Login súper simple (TDD)")

user = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Entrar"):
    if verificar(user, password):
        st.success(f"Bienvenido, {user}")
    else:
        st.error("Usuario o contraseña incorrectos")

st.write("---")
st.subheader("Registro rápido")

new_user = st.text_input("Nuevo usuario")
new_pass = st.text_input("Nueva contraseña", type="password")

if st.button("Registrar"):
    if registrar(new_user, new_pass):
        st.success("Usuario creado correctamente.")
    else:
        st.warning("El usuario ya existe o los datos no son válidos.")
