import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import os
st.header("Periodic Table Explorer")
# Title
st.sidebar.title("Sidebar Menu")
page = st.sidebar.radio("Select Page", ["Search", "Radius Trends","ionization_energy Trends","electron_affinity Trends"])
# Search pages in menu bar
if page=="Search":
    name = st.text_input("enter the element name")
    if name:
        try:
            img_path = f"{name}.png"
            if os.path.exists(img_path):
                img = Image.open(img_path)
                st.image(img, caption=name)
            else:
                st.warning(f"No image found for {name}.")
        except Exception as e:
            st.error("Something went wrong while loading the image.")
       
#Radius trends in menu bar
elif page == "Radius Trends":
    df = pd.read_csv("elements.csv")
    group_number =st.number_input("enter the element group number")
    df_group = df[df["group"]==group_number]
    fig, ax = plt.subplots()
    ax.plot(df_group["element"],df_group["radii"],marker = 'o',)
    ax.set_xlabel("element's name")
    ax.set_ylabel("Radius (pm)")
    st.pyplot(fig)
#ionization_energy Trends in menu bar
elif page == "ionization_energy Trends":
    df = pd.read_csv("elements.csv")
    group_number =st.number_input("enter the element group number")
    df_group = df[df["group"]==group_number]
    fig, ax = plt.subplots()
    ax.plot(df_group["element"],df_group["ionization_energy"],marker = 'o',)
    ax.set_xlabel("element's name")
    ax.set_ylabel("ionization_energy in (kJ/mol)")
    st.pyplot(fig)
#electron_affinity Trends in menu bar
elif page == "electron_affinity Trends":
    df = pd.read_csv("elements.csv")
    group_number =st.number_input("enter the element group number")
    df_group = df[df["group"]==group_number]
    fig, ax = plt.subplots()
    ax.plot(df_group["element"],df_group["electron_affinity"],marker = 'o',)
    ax.set_xlabel("element's name")
    ax.set_ylabel("electron_affinity in (kJ/mol)")
    st.pyplot(fig)
