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

def is_coprime(a, b):
  while b != 0:
    a, b = b, a % b
  return a == 1

def extended_euclidean(a, b):
  if b == 0:
    return a, 1, 0
  else:
    gcds, x, y = extended_euclidean(b, a % b)
    return is_coprime, y, x - (a // b) * y


st.write("halaman membangkitkan kunci untuk enkripsi RSA")
if 'p_rsa' not in st.session_state:
  st.session_state.p_rsa = None
if 'q_rsa' not in st.session_state:
  st.session_state.q_rsa = None
if 'e_rsa' not in st.session_state:
  st.session_state.e_rsa = None

col1, col2, col3 = st.columns(3)

with col1:
  if st.button('bangkitkan kunci'):
    if st.session_state.p_rsa is None:
      st.session_state.p_rsa = generate_random_prime()
      st.session_state.q_rsa = generate_random_prime()
      st.session_state.e_rsa = generate_random_prime()
      end_time = time.time()

if st.session_state.p_rsa and st.session_state.q_rsa and st.session_state.e_rsa is not None:
  n_rsa = st.session_state.p_rsa * st.session_state.q_rsa
  phi_rsa = (st.session_state.p_rsa - 1) * (st.session_state.q_rsa - 1)
  gcds, x, y = extended_euclidean(st.session_state.e_rsa, phi_rsa)

  if x > 0:
    d = x
  if x < 0:
    d = x % phi_rsa
  st.write('nilai p :', st.session_state.p_rsa)
  st.write('nilai q :', st.session_state.q_rsa)
  st.write('nilai e :', st.session_state.e_rsa)
  st.write('nilai n :', n_rsa)
  st.write('nilai phi :', phi_rsa)
  st.write('nilai d :', d)

  cola, colb = st.columns(2)

  with cola:
    if st.button('download kunci enkripsi'):
      with open("kunci enkripsi.txt", "w") as file:
        file.write(str(st.session_state.p_rsa) + '\n')
        file.write(str(st.session_state.q_rsa) + '\n')
        file.write(str(st.session_state.e_rsa) + '\n')
        file.write(str(n_rsa) + '\n')

  with colb:
    if st.button('download kunci dekripsi'):
      with open("kunci dekripsi.txt", "w") as file:
        file.write(str(d) + '\n')
        file.write(str(n_rsa) + '\n')