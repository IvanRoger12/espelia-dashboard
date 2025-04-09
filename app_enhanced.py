
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Espelia - Visualisation et Candidature", layout="wide")

# Titre principal
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌍 Espelia & Ma Candidature</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("""
Bienvenue sur cette mini-application conçue pour illustrer mon intérêt pour **Espelia** et démontrer mes compétences en data visualisation.
""")

# Section : À propos d’Espelia
st.header("🏢 À propos d’Espelia")
st.markdown("""
**Espelia**, fondée en 1995, est un acteur engagé au service de l'intérêt général. Avec plus de 200 collaborateurs et plusieurs filiales (Tecurbis, RCF), elle accompagne la transformation des services publics sur l'ensemble du territoire français, ainsi qu'à l'international.

Le pôle **Solutions Numériques** développe des outils sur-mesure pour soutenir les politiques publiques, avec une forte expertise en data visualisation, ingénierie de données, et accompagnement agile des projets métiers.
""")

# Données sur les implantations
df = pd.read_csv("data_espelia.csv")

st.subheader("📍 Implantations géographiques")
fig_map = px.scatter_geo(df,
                         lat='Latitude',
                         lon='Longitude',
                         text='Ville',
                         hover_name='Ville',
                         projection="natural earth",
                         title="Présence d’Espelia en France et à l'international",
                         template='plotly_white')
st.plotly_chart(fig_map, use_container_width=True)

# Chiffres clés
st.subheader("🔢 Chiffres clés")
col1, col2, col3 = st.columns(3)
col1.metric("Année de création", "1995")
col2.metric("Collaborateurs", "200+")
col3.metric("Bureaux", "9 en France + Hanoï")

# Section : Mes motivations et profil
st.header("🙋‍♂️ À propos de moi – Ivan Nfinda")
st.markdown("""
🎓 **Formation** : MBA en Big Data & Intelligence Artificielle (ESG)  
💼 **Expériences** : Data Analyst chez Endo Data, Naturalia, Micropole  
🛠️ **Compétences** : Python, Power BI, SQL, reporting automatisé, visualisation de données  
💬 **Objectif** : Rejoindre Espelia pour contribuer à la transformation numérique du service public en France et à l’international.
""")

# Graphique de croissance des projets fictifs
st.subheader("📈 Évolution fictive des projets Espelia")
projets = pd.DataFrame({
    "Année": list(range(2016, 2025)),
    "Projets": [40, 55, 70, 85, 105, 130, 160, 190, 220]
})
fig_line = px.line(projets, x="Année", y="Projets", markers=True,
                   title="Croissance fictive du nombre de projets",
                   template='plotly_white')
st.plotly_chart(fig_line, use_container_width=True)

# Pie chart : répartition imaginaire des projets par secteur
st.subheader("📊 Répartition (fictive) des projets par secteur")
secteurs = pd.DataFrame({
    "Secteur": ["Collectivités locales", "Santé publique", "Environnement", "Éducation", "Autres"],
    "Projets": [80, 45, 30, 25, 20]
})
fig_pie = px.pie(secteurs, names="Secteur", values="Projets", hole=0.3,
                 title="Répartition sectorielle des projets Espelia")
st.plotly_chart(fig_pie, use_container_width=True)

# Remerciement
st.markdown("---")
st.markdown("<p style='text-align: center;'>📝 Réalisé par <strong>Ivan Nfinda</strong> – Avril 2025</p>", unsafe_allow_html=True)
