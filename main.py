import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración de la página web
st.set_page_config(page_title="Simulador de Física", page_icon="🚀", layout="wide")

st.title("🚀 Simulador Maestro de Física")
st.markdown("Proyecto de Física 1")
st.markdown("---")

# Menú lateral web
st.sidebar.header("Menú de Navegación")
modulo = st.sidebar.radio("Selecciona el módulo:",
                          ["1. MRUV", "2. Caída Libre", "3. MRU", "4. Tiro Parabólico"])

# ==========================================
# 1. MÓDULO MRUV
# ==========================================
if modulo == "1. MRUV":
    st.header("Movimiento Rectilíneo Uniforme Variado (MRUV)")
    formula = st.selectbox("Selecciona la fórmula a utilizar:",
                           ["a = (Vf - Vo) / t", "Vf = Vo + a*t", "d = ((Vo + Vf) / 2) * t"])

    col1, col2 = st.columns(2)

    if formula == "a = (Vf - Vo) / t":
        with col1:
            vf = st.number_input("Velocidad Final (Vf) m/s:", value=35.0)
            vo = st.number_input("Velocidad Inicial (Vo) m/s:", value=15.0)
            t = st.number_input("Tiempo (t) s:", value=8.0, min_value=0.1)

        if st.button("Calcular Aceleración", type="primary"):
            a = (vf - vo) / t
            st.success(f"**Resultado:** La aceleración es {a:.2f} m/s²")

            # Gráfica Web de Velocidad vs Tiempo
            t_array = np.linspace(0, t, 100)
            v_array = vo + a * t_array

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t_array, v_array, 'b-', linewidth=2)
            ax.fill_between(t_array, v_array, alpha=0.2, color='blue')
            ax.set_title("Gráfica: Velocidad vs Tiempo")
            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Velocidad (m/s)")
            ax.grid(True)
            st.pyplot(fig)

    elif formula == "Vf = Vo + a*t":
        with col1:
            vo = st.number_input("Velocidad Inicial (Vo) m/s:", value=0.0)
            a = st.number_input("Aceleración (a) m/s²:", value=2.5)
            t = st.number_input("Tiempo (t) s:", value=10.0, min_value=0.1)

        if st.button("Calcular Velocidad Final", type="primary"):
            vf = vo + (a * t)
            st.success(f"**Resultado:** La Velocidad Final es {vf:.2f} m/s")

    elif formula == "d = ((Vo + Vf) / 2) * t":
        with col1:
            vo = st.number_input("Velocidad Inicial (Vo) m/s:", value=10.0)
            vf = st.number_input("Velocidad Final (Vf) m/s:", value=20.0)
            t = st.number_input("Tiempo (t) s:", value=5.0, min_value=0.1)

        if st.button("Calcular Distancia", type="primary"):
            d = ((vo + vf) / 2) * t
            st.success(f"**Resultado:** La distancia recorrida es {d:.2f} metros")

# ==========================================
# 2. MÓDULO CAÍDA LIBRE
# ==========================================
elif modulo == "2. Caída Libre":
    st.header("Simulador de Caída Libre")
    g = 9.81

    col1, col2 = st.columns(2)
    with col1:
        altura = st.number_input("Altura inicial (m):", value=100.0, min_value=0.1)
        v0 = st.number_input("Velocidad inicial (m/s):", value=0.0)

    if st.button("Simular Caída", type="primary"):
        # Cálculos cuadráticos
        a = -0.5 * g
        b = v0
        c = altura
        discriminante = b**2 - 4*a*c

        t1 = (-b + np.sqrt(discriminante)) / (2*a)
        t2 = (-b - np.sqrt(discriminante)) / (2*a)
        t_total = max(t1, t2)

        st.success(f"**Resultado:** El objeto toca el suelo en {t_total:.2f} segundos.")

        # Gráfica Web de la trayectoria
        t_array = np.linspace(0, t_total, 100)
        y_array = altura + v0 * t_array - 0.5 * g * t_array**2

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(np.zeros_like(y_array), y_array, 'ro-', markevery=[-1], markersize=10)
        ax.set_title("Trayectoria de Caída")
        ax.set_ylabel("Altura (m)")
        ax.set_xticks([]) # Ocultar eje X
        ax.grid(True)
        st.pyplot(fig)

# ==========================================
# 3. MÓDULO MRU
# ==========================================
elif modulo == "3. MRU":
    st.header("Movimiento Rectilíneo Uniforme (MRU)")

    col1, col2 = st.columns(2)
    with col1:
        v = st.number_input("Velocidad Constante (m/s):", value=15.0)
        t_total = st.number_input("Tiempo de recorrido (s):", value=10.0, min_value=0.1)

    if st.button("Simular MRU", type="primary"):
        d_total = v * t_total
        st.success(f"**Resultado:** La distancia total recorrida es {d_total:.2f} metros.")

        t_array = np.linspace(0, t_total, 100)
        x_array = v * t_array

        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(x_array, np.zeros_like(x_array), 'g-', linewidth=3)
        ax.plot(x_array[-1], 0, 'go', markersize=12) # Punto final
        ax.set_title("Recorrido en MRU")
        ax.set_xlabel("Distancia (m)")
        ax.set_yticks([])
        st.pyplot(fig)

# ==========================================
# 4. MÓDULO TIRO PARABÓLICO
# ==========================================
elif modulo == "4. Tiro Parabólico":
    st.header("Simulador de Tiro Parabólico")
    g = 9.81

    col1, col2 = st.columns(2)
    with col1:
        v0 = st.number_input("Velocidad Inicial (Vo) en m/s:", value=50.0, min_value=0.1)
        angulo_grados = st.number_input("Ángulo de lanzamiento (Grados):", value=45.0, min_value=0.0, max_value=90.0)

    if st.button("Lanzar Proyectil", type="primary"):
        angulo_rad = math.radians(angulo_grados)
        v0x = v0 * math.cos(angulo_rad)
        v0y = v0 * math.sin(angulo_rad)

        t_total = (2 * v0y) / g
        h_max = (v0y**2) / (2 * g)
        d_max = v0x * t_total

        st.success(f"**Resultados:** Tiempo de vuelo: {t_total:.2f} s | Altura máxima: {h_max:.2f} m | Alcance: {d_max:.2f} m")

        t_array = np.linspace(0, t_total, 100)
        x_array = v0x * t_array
        y_array = v0y * t_array - 0.5 * g * t_array**2

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x_array, y_array, 'r--')
        ax.plot(x_array[-1], y_array[-1], 'ro', markersize=10) # Impacto
        ax.set_title("Trayectoria Parabólica")
        ax.set_xlabel("Distancia (m)")
        ax.set_ylabel("Altura (m)")
        ax.set_ylim(bottom=0)
        ax.grid(True)
        st.pyplot(fig)
