import streamlit as st

st.write("tata cara melakukan signcryption : ")
st.write("1. bangkitkan kunci penerima di halaman kunci penerima RSA")
st.write("2. bangkitkan kunci pengirim di halaman kunci pengirim LLKAKE")
st.write("3. halaman sign dan enkripsi yang dilakukan oleh pengirim")
st.write("4. halaman verifikasi dan dekripsi yang dilakukan oleh penerima")
st.write("\n")
st.write("syarat dan ketentuan : ")
st.write("1. hanya pengirim yang melakukan pembangkitan kunci di halaman kunci pengirim")
st.write("2. hanya penerima yang melakukan pembangkitan kunci di halaman kunci penerima")
st.write("3. halaman sign dan enkripsi di lakukan oleh pengirim dengan syarat penerima harus memberikan kunci enkripsi")
st.write("4. halaman verifikasi dan dekripsi yang dilakukan oleh penerima dengan syarat pengirim harus memberikan kunci verifikasi")
