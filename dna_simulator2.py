import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Relative DNA Content Simulator of Meiosis")

s_phase_start = st.slider("S Start", 0.0, 7.0, 2.0, step=0.1)
s_phase_end = st.slider("G2 Start", s_phase_start + 0.1, 8.0, 4.0, step=0.1)
m1_time = st.slider("M1 Metaphase", s_phase_end + 0.1, 9.0, 5.0, step=0.1)
m2_time = st.slider("M2 Metaphase", m1_time + 0.1, 10.0, 6.0, step=0.1)

non_disjunction_m1 = False
non_disjunction_m2 = False

non_disjunction_m1 = st.checkbox("M1 Nondisjunction", value=False)
non_disjunction_m2 = st.checkbox("M2 Nondisjunction", value=False)

def dna_amount(t):
    if t < s_phase_start:
        return 2
    elif t < s_phase_end:
        return 2 + ((4 - 2) / (s_phase_end - s_phase_start)) * (t - s_phase_start)
    elif t < m1_time:
        return 4
    elif t < m2_time:
        return 4 if non_disjunction_m1 else 2
    else:
        if non_disjunction_m1:
            return 4 if non_disjunction_m2 else 2
        else:
            return 2 if non_disjunction_m2 else 1

t_vals = np.linspace(0, 10, 500)
dna_vals = [dna_amount(t) for t in t_vals]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t_vals, dna_vals, label="DNA Content", color="blue", linewidth=2)
ax.axvline(m1_time, linestyle='--', color='red', label="M1 Metaphase")
ax.axvline(m2_time, linestyle='--', color='green', label="M2 Metaphase")
ax.set_xlabel("Time")
ax.set_ylabel("Relative DNA Content")
ax.set_title("Changes in Relative DNA Content under Conditions of Nondisjunction")
ax.legend()
ax.grid(True)
st.pyplot(fig)
