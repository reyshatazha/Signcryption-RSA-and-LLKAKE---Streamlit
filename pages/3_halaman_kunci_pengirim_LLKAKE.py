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

def find_sophie_germain_primes():
    while True:
        num = random.getrandbits(32)
        if fermat(num) and fermat(2 * num + 1):
            number = 2 * num + 1
            return number

def generate_nilai_ks():
    KS = random.getrandbits(32)
    return KS


st.write("halaman membangkitkan kunci untuk sign LLKAKE")
if 'p_LLKAKE' not in st.session_state:
  st.session_state.p_LLKAKE = None
if 'q_LLKAKE' not in st.session_state:
  st.session_state.q_LLKAKE = None
if 'r1_LLKAKE' not in st.session_state:
  st.session_state.r1_LLKAKE = None
if 'r2_LLKAKE' not in st.session_state:
  st.session_state.r2_LLKAKE = None

if 'KS_LLKAKE' not in st.session_state:
    st.session_state.KS_LLKAKE = None

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  if st.button('generate kunci LLKAKE'):
    if st.session_state.p_LLKAKE is None:
      st.session_state.p_LLKAKE = find_sophie_germain_primes()
      st.session_state.q_LLKAKE = find_sophie_germain_primes()
      st.session_state.r1_LLKAKE = random.getrandbits(16)
      st.session_state.r2_LLKAKE = random.getrandbits(16)
      st.session_state.KS_LLKAKE = generate_nilai_ks()
      end_time = time.time()


if st.session_state.p_LLKAKE and st.session_state.q_LLKAKE and st.session_state.r1_LLKAKE and st.session_state.r2_LLKAKE and st.session_state.KS_LLKAKE is not None:
    n = st.session_state.p_LLKAKE * st.session_state.q_LLKAKE
    r = st.session_state.r1_LLKAKE * st.session_state.r2_LLKAKE
    PKS = st.session_state.KS_LLKAKE + r * st.session_state.p_LLKAKE

    st.write('nilai p adalah :',st.session_state.p_LLKAKE)
    st.write('nilai q adalah :',st.session_state.q_LLKAKE)
    st.write('nilai n adalah :', n)
    st.write('nilai r adalah :',r)
    st.write('nilai r1 adalah :',st.session_state.r1_LLKAKE)
    st.write('nilai r2 adalah :',st.session_state.r2_LLKAKE)
    st.write('nilai KS adalah :',st.session_state.KS_LLKAKE)
    st.write('nilai PKS adalah :',PKS)

    col1,col2 = st.columns(2)

    with col1:
        if st.button('download kunci verifikasi'):
            with open('Kunci_verifikasi_llkake.txt','w') as f:
                f.write(str(n) + '\n')
                f.write(str(r) + '\n')
                f.write(str(st.session_state.r1_LLKAKE) + '\n')
                f.write(str(PKS) + '\n')

    with col2:
        if st.button('download kunci sign'):
            with open('Kunci_sign_llkake.txt','w') as f:
                f.write(str(st.session_state.KS_LLKAKE) + '\n')
                f.write(str(st.session_state.r2_LLKAKE) + '\n')
                f.write(str(st.session_state.p_LLKAKE) + '\n')
                f.write(str(n) + '\n')