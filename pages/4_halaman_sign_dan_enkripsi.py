import base64
import streamlit as st
import hashlib
import random
import math
import time

def fermat(p):
  jumlahpercobaan = len(str(p)) * 3

  for i in range(jumlahpercobaan):
    a = random.randint(2, p)
    if pow(a, p - 1, p) != 1:
      return False
  return True

def generate_random_prime():
  while True:
    num = random.getrandbits(48)
    if fermat(num):
      return num

def find_sophie_germain_primes():
    while True:
        num = random.getrandbits(48)
        if fermat(num) and fermat(2 * num + 1):
            number = 2 * num + 1
            return number

def generate_r():
    r1 = random.getrandbits(12)
    r2 = random.getrandbits(12)

    r = r1*r2
    return r,r1,r2

def generate_nilai_ks():
    KS = random.getrandbits(24)
    return KS

def signing_file(m,KS,n,r2,nilai_p):
    nilai = r2*nilai_p

    S1 = pow(m,KS,n)
    S2 = pow(m,nilai,n)
    return S1,S2

def verification(file_hash,PKS,S1,S2,r1,n):
    x = pow(file_hash, PKS, n)
    nilais2 = pow(S2, r1)
    y = (S1 * nilais2) % n

    return x,y

def is_coprime(a, b):
  while b != 0:
    a, b = b, a % b
  return a == 1

def generate_coprime_pair(phi):
  while True:
    num1 = random.getrandbits(24)
    if is_coprime(num1, phi):
      return num1, phi
def extended_euclidean(a, b):
  if b == 0:
    return a, 1, 0
  else:
    gcds, x, y = extended_euclidean(b, a % b)
    return is_coprime, y, x - (a // b) * y

def ascii_value(list_nama):
    ascii_values = []

    for char in list_nama:
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

def enkripsi(ascii_values,e,n):
    enkripsi = []
    for num in ascii_values:
        enkripsi.append(pow(num, e, n))
    return enkripsi

def kembalian_char(enkripsi):
    nilai_bilangan_asli = []
    for char in enkripsi:
        ascii_value = chr(char)
        nilai_bilangan_asli.append(ascii_value)

def penggabungan(kembalian_char):
    result_akhir = ''.join(kembalian_char)

    gabungan = result_akhir.encode()
    return gabungan

uploaded_file = st.file_uploader("Unggah file Anda")

if uploaded_file is not None:
    with open(uploaded_file.name, "rb") as f:
        data = f.read()

    base64_data = base64.b64encode(data)
    base64_data12 = base64_data.decode()

    hash_object = getattr(hashlib, 'sha256')()
    hash_object.update(data)
    filesa = hash_object.hexdigest()
    file_hash = int(filesa, 16)

    uploaded_file3 = st.file_uploader("Unggah file kunci signing")
    uploaded_file2 = st.file_uploader("Unggah file kunci enkripsi")

    if uploaded_file2 is not None:
        with open(uploaded_file2.name, "r") as f:
            data_key = f.readlines()

        p_rsa = int(data_key[0])
        q_rsa = int(data_key[1])
        e_rsa = int(data_key[2])
        n_rsa = int(data_key[3])

    if uploaded_file3 is not None:
        with open(uploaded_file3.name, "r") as f:
            data_key_sign = f.readlines()

        ks_llkake = int(data_key_sign[0])
        r2_llkake = int(data_key_sign[1])
        p_llkake = int(data_key_sign[2])
        n_llkake = int(data_key_sign[3])

        if e_rsa and n_rsa and ks_llkake and n_llkake and r2_llkake and p_llkake is not None:
            list_nama = [char for char in base64_data12]

            ascii_values = ascii_value(list_nama)

            nilai_enkripsi = enkripsi(ascii_values, e_rsa, n_rsa)

            nilai_sign = signing_file(file_hash, ks_llkake, n_llkake, r2_llkake, p_llkake)

            S1, S2 = nilai_sign
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button('download teks enkripsi'):
                    with open("nilai_enkripsi.txt", "w") as file:
                        for nilai in nilai_enkripsi:
                            file.write(f"{nilai}\n")
            with col2:
                if st.button('download teks signing'):
                    with open("nilai_signing.txt", "w") as file:
                        file.write(str(S1) + '\n')
                        file.write(str(S2) + '\n')

            with col3:
                if st.button('download teks hash'):
                    with open("nilai_hash.txt", "w") as file:
                        file.write(str(file_hash))