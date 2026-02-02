import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="CS Insights Dashboard", layout="wide")

st.title("🎧 Customer Service Analytics")
st.markdown("Reemplazando la vista de marketing por una visión de **servicio humano**.")

# --- SIDEBAR (Filtros para la demo) ---
st.sidebar.header("Filtros de Demo")
canal = st.sidebar.multiselect("Canal de contacto", ["WhatsApp", "Email", "Chat Web"], default=["WhatsApp", "Email", "Chat Web"])

# --- KPIs PRINCIPALES ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Personas Contactadas", value="1,284", delta="12% vs ayer")
with col2:
    st.metric(label="Mensajes Respondidos", value="1,150", delta="94% tasa de éxito")
with col3:
    st.metric(label="Tiempo de Respuesta", value="3.5 min", delta="-1.2 min", delta_color="normal")
with col4:
    st.metric(label="Satisfacción (CSAT)", value="4.8 / 5", delta="⭐")

st.divider()

# --- GRÁFICOS ---
c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("Volumen de Conversaciones (Últimas 24h)")
    # Datos simulados
    df_chart = pd.DataFrame({
        'Hora': list(range(24)),
        'Mensajes': [10, 5, 2, 1, 0, 3, 15, 45, 80, 110, 95, 120, 130, 100, 90, 115, 140, 120, 80, 60, 40, 30, 20, 15]
    })
    fig = px.line(df_chart, x='Hora', y='Mensajes', template="plotly_white", line_shape="spline")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Temas más consultados")
    temas = {"Envíos": 45, "Precios": 30, "Garantías": 15, "Otros": 10}
    fig_pie = px.pie(values=list(temas.values()), names=list(temas.keys()), hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- TABLA DE AGENTES ---
st.subheader("Estatus del Equipo en Vivo")
agentes = pd.DataFrame({
    "Agente": ["Ana García", "Carlos Ruiz", "Sofía López"],
    "Mensajes Hoy": [145, 132, 156],
    "Promedio Calificación": [4.9, 4.7, 5.0],
    "Estado": ["🟢 Online", "🟡 En Almuerzo", "🟢 Online"]
})
st.table(agentes)
