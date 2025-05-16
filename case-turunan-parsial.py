import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("Aplikasi Analisis Laba Perusahaan")
st.markdown("Fungsi laba: *f(x, y) = xy - 0.1x² - 0.2y²*")

# Input dari user
x_val = st.slider("Harga jual produk (x)", 0.0, 50.0, 10.0)
y_val = st.slider("Jumlah produk terjual (y)", 0.0, 50.0, 10.0)

# Fungsi laba dan turunannya
def f(x, y):
    return x * y - 0.1 * x*2 - 0.2 * y*2

def df_dx(x, y):
    return y - 0.2 * x

def df_dy(x, y):
    return x - 0.4 * y

# Hasil evaluasi
z_val = f(x_val, y_val)
partial_x = df_dx(x_val, y_val)
partial_y = df_dy(x_val, y_val)

st.write(f"Nilai fungsi laba f(x, y): *{z_val:.2f}*")
st.write(f"Turunan parsial terhadap x (∂f/∂x): *{partial_x:.2f}*")
st.write(f"Turunan parsial terhadap y (∂f/∂y): *{partial_y:.2f}*")

# Grafik 3D permukaan fungsi
st.subheader("Grafik Permukaan Laba")

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(0, 50, 50)
Y = np.linspace(0, 50, 50)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel("x (Harga jual)")
ax.set_ylabel("y (Jumlah terjual)")
ax.set_zlabel("Laba f(x, y)")
ax.set_title("Permukaan Fungsi Laba")

st.pyplot(fig)
