import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Laba Menggunakan Turunan Parsial")
st.subheader("Fungsi: f(x, y) = xy - 0.1x² - 0.2y²")

# Input dari pengguna
x = st.slider("Harga per Unit (x)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)
y = st.slider("Jumlah Terjual (y)", min_value=0.0, max_value=50.0, value=30.0, step=1.0)

# Fungsi laba dan turunannya
def laba(x, y):
    return x * y - 0.1 * x*2 - 0.2 * y*2

def turunan_x(x, y):
    return y - 0.2 * x

def turunan_y(x, y):
    return x - 0.4 * y

# Perhitungan
hasil_laba = laba(x, y)
df_dx = turunan_x(x, y)
df_dy = turunan_y(x, y)

# Tampilkan hasil
st.write(f"*Laba f({x}, {y}) = {hasil_laba:.2f}*")
st.write(f"Turunan parsial terhadap x (∂f/∂x) = {df_dx:.2f}")
st.write(f"Turunan parsial terhadap y (∂f/∂y) = {df_dy:.2f}")

# Visualisasi grafik 3D
st.subheader("Visualisasi Permukaan Laba")
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

# Grid nilai
x_vals = np.linspace(0, 50, 50)
y_vals = np.linspace(0, 50, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = laba(X, Y)

# Plot permukaan
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel("Harga per Unit (x)")
ax.set_ylabel("Jumlah Terjual (y)")
ax.set_zlabel("Laba f(x, y)")
ax.view_init(elev=30, azim=135)

st.pyplot(fig)