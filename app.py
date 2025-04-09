
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Espelia en chiffres", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>📊 Espelia en chiffres</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
Bienvenue sur ce mini-projet de visualisation réalisé pour appuyer ma candidature au poste de Data Analyst chez **Espelia**.  
Ce tableau de bord présente une vue d'ensemble des implantations géographiques du groupe, ainsi que quelques données symboliques de son activité.
""")

# Données
df = pd.read_csv("data_espelia.csv")

# Carte
st.subheader("📍 Implantations géographiques")
fig_map = px.scatter_geo(df,
                         lat='Latitude',
                         lon='Longitude',
                         text='Ville',
                         scope='world',
                         title='Présence d'Espelia en France et à l'international',
                         template='plotly_white')
st.plotly_chart(fig_map, use_container_width=True)

# Chiffres clés
st.subheader("🔢 Chiffres clés")
col1, col2, col3 = st.columns(3)
col1.metric("Année de création", "1995")
col2.metric("Nombre de collaborateurs", "200+")
col3.metric("Filiales", "Tecurbis, RCF")

# Croissance des projets
st.subheader("📈 Croissance des projets (fictive)")
projets = pd.DataFrame({
    "Année": list(range(2016, 2025)),
    "Projets": [40, 55, 70, 85, 105, 130, 160, 190, 220]
})
fig_line = px.line(projets, x="Année", y="Projets", markers=True,
                   title="Évolution fictive du nombre de projets Espelia",
                   template='plotly_white')
st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")
st.markdown("📝 Projet réalisé par **Ivan Nfinda** – Avril 2025")
