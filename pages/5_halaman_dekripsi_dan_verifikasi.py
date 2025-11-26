import base64
import streamlit as st
import random
import math
import time

def dekripsi(enkripsi,d,n):
    dekripsi = []
    for num in enkripsi:
        dekripsi.append(pow(num,d,n))
    return dekripsi

def verification(file_hash,PKS,S1,S2,r1,n):
    x = pow(file_hash, PKS, n)
    nilais2 = pow(S2, r1)
    y = (S1 * nilais2) % n

    return x,y
def kembalian_char(dekripsi):
    nilai_bilangan_asli = []

    for char in dekripsi:
        ascii_value = chr(char)
        nilai_bilangan_asli.append(ascii_value)

    result_akhir = ''.join(nilai_bilangan_asli)

    gabungan = result_akhir.encode()

    decod64 = base64.b64decode(gabungan)
    return decod64

upload_file = st.file_uploader("Upload File enkripsi")

if upload_file is not None:
    with open(upload_file.name, "r") as f:
        data = f.readlines()

    nilai_enkripsi_baru = [nilai.rstrip() for nilai in data]

    upload_file_hash = st.file_uploader("Upload File Hash")

    if upload_file_hash is not None:
        with open(upload_file_hash.name, "r") as file:
            data_hash = file.read()

            nilai_hash = int(data_hash)
            upload_file_kunci_rsa = st.file_uploader("Upload Kunci dekripsi RSA")
            upload_file_kunci_llkake = st.file_uploader("Upload Kunci verifikasi LLKAKE")
            upload_file_sign = st.file_uploader("Upload File Sign")
            if upload_file_kunci_llkake and upload_file_kunci_rsa and upload_file_sign is not None:
                with open(upload_file_kunci_rsa.name, "r") as file_rsa:
                    data_kunci_rsa = file_rsa.readlines()
                with open(upload_file_kunci_llkake.name, "r") as file:
                    data_kunci_llkake = file.readlines()
                with open(upload_file_sign.name, "r") as file_sign:
                    data_sign = file_sign.readlines()

                start_time = time.time()

                S1 = int(data_sign[0])
                S2 = int(data_sign[1])
                d_rsa = int(data_kunci_rsa[0])
                n_rsa = int(data_kunci_rsa[1])
                n_llkake = int(data_kunci_llkake[0])
                r_llkake = int(data_kunci_llkake[1])
                r1_llkake = int(data_kunci_llkake[2])
                pks_llkake = int(data_kunci_llkake[3])

                nilai_integer = [int(angka) for angka in nilai_enkripsi_baru]
                nilai_dekripsi = dekripsi(nilai_integer, d_rsa, n_rsa)
                nilai_kembalian_char = kembalian_char(nilai_dekripsi)

                verifikasi = verification(nilai_hash,pks_llkake,S1,S2,r1_llkake,n_llkake)
                x,y = verifikasi

                if st.button("Verify"):
                    if x == y:
                        st.write("data telah terverifikasi")
                        st.write("nilai x : ",x)
                        st.write("nilai y : ",y)
                    if x != y:
                        st.write("data tidak terverifikasi")
                        st.write("nilai x : ", x)
                        st.write("nilai y : ", y)

                title = st.text_input("masukkan nama file baru")
                if st.button("unduh pesan asli"):
                    with open(title, "wb") as file:
                        file.write(nilai_kembalian_char)