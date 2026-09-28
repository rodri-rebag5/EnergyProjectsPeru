
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import TagFilterButton

# Load data
EPO = pd.read_csv("EPOV2.csv")

# st.markdown("""
# <style>
#     /* Main background */
#     .stApp {
#         background-color: #FFFFFF;
#         color: #222222;
#     }
#
#     /* Text */
#     h1, h2, h3, p, label {
#         color: #222222;
#     }
# </style>
# """, unsafe_allow_html=True)


st.set_page_config(layout="wide")
st.title("Energy Projects in Peru")
st.write("This website allows anyone to observe the location of the different potential energy projects in Peru")

col1, col2 = st.columns(2)

with col1:

    # Create map
    m = folium.Map(
        location=[EPO["Latitud"].mean(), EPO["Longitud"].mean()],
        zoom_start=10
    )

    tags = ["Solar", "Electric"]

    # Add markers
    for _, row in EPO.iterrows():
        if row["Nombre del Estudio"][:4] == "C.S.":
            folium.Marker(
                location=[row["Latitud"], row["Longitud"]],
                popup=f"""
                <b>{row["Nombre del Estudio"]}</b><br>
                Coordinates: {row["Latitud"]}, {row["Longitud"]}
                """,
                icon = folium.Icon(icon="cloud", color='blue'),
                tag = "Solar"
            ).add_to(m)
        elif row["Nombre del Estudio"][:4] == "C.E.":
            folium.Marker(
                location=[row["Latitud"], row["Longitud"]],
                popup=f"""
                        <b>{row["Nombre del Estudio"]}</b><br>
                        Coordinates: {row["Latitud"]}, {row["Longitud"]}
                        """,
                icon=folium.Icon(icon="glyphicon glyphicon-flash", color='green'),
                tag = "Electric"
            ).add_to(m)

    # Display map
    st_folium(m, width=1500, height=600)
    TagFilterButton(tags).add_to(m)

with col2:
    st.dataframe(EPO, use_container_width=True)
