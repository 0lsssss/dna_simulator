import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Relative DNA Content Simulator for Gametogenesis")
st.markdown("")

# 사용자 슬라이더 입력
s_phase_start = st.slider("S기 시작 시점 (G1 종료)", 0.0, 5.0, 2.0, step=0.1)
s_phase_end = st.slider("S기 종료 시점 (G2 시작)", s_phase_start + 0.1, 6.0, 4.0, step=0.1)
m1_time = st.slider("제1분열(M1) 시점", s_phase_end + 0.1, 7.0, 5.0, step=0.1)
m2_time = st.slider("제2분열(M2) 시점", m1_time + 0.1, 8.0, 6.0, step=0.1)
mutation = st.checkbox("비분리 돌연변이 발생 (감소 없음)", value=False)

def DNA_amount(t):
    if t < s_phase_start:
        return 2
    elif t < s_phase_end:
        return 2 + ((4 - 2) / (s_phase_end - s_phase_start)) * (t - s_phase_start)
    elif t < m1_time:
        return 4
    elif t < m2_time:
        return 4 if mutation else 2
    else:
        return 4 if mutation else 1

t_vals = np.linspace(0, 10, 500)
dna_vals = [DNA_amount(t) for t in t_vals]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t_vals, dna_vals, color='blue', linewidth=2, label="DNA 상대량")
ax.axvline(x=m1_time, linestyle='--', color='red', label="제1분열 시점")
ax.axvline(x=m2_time, linestyle='--', color='green', label="제2분열 시점")
ax.set_title("DNA 상대량 변화 시뮬레이션")
ax.set_xlabel("시간 t")
ax.set_ylabel("DNA 상대량")
ax.grid(True)
ax.legend()

st.pyplot(fig)
