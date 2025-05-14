import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input fungsi
st.title("Aplikasi Turunan Parsial dan Grafik 3D")

x, y = sp.symbols('x y')
fungsi_input = st.text_input("Masukkan fungsi f(x, y):", "x*2 + y*2")

try:
    f = sp.sympify(fungsi_input)

    # Hitung turunan parsial
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.write(f"Turunan parsial ∂f/∂x = {fx}")
    st.write(f"Turunan parsial ∂f/∂y = {fy}")

    # Input titik evaluasi
    x0 = st.number_input("Masukkan nilai x₀", value=1.0)
    y0 = st.number_input("Masukkan nilai y₀", value=1.0)

    fx_val = fx.evalf(subs={x: x0, y: y0})
    fy_val = fy.evalf(subs={x: x0, y: y0})
    f_val = f.evalf(subs={x: x0, y: y0})

    st.write(f"f({x0}, {y0}) = {f_val}")
    st.write(f"∂f/∂x({x0}, {y0}) = {fx_val}")
    st.write(f"∂f/∂y({x0}, {y0}) = {fy_val}")

    # Grafik 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(x0 - 2, x0 + 2, 50)
    Y = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(X, Y)
    f_lambd = sp.lambdify((x, y), f, "numpy")
    Z = f_lambd(X, Y)

    # Grafik fungsi
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

    # Bidang singgung
    Z_tangent = f_val + fx_val * (X - x0) + fy_val * (Y - y0)
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")