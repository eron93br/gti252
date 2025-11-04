import numpy as np
import pandas as pd
import streamlit as st
import datetime
from common import stream_data, load_tips_dataset, make_visualization1 , make_vis_tb, make_piechart
import plotly.express as px

df = pd.read_csv('assets/tips.csv')

with st.sidebar:
    st.write("Sidebar")
    rslider_values = st.slider("Selecionar os valores do range slider", float(df["tip"].min()), float(df["tip"].max()), (2.34, 6.37))
    print(f"No range slider você selecionou: {rslider_values[0]} e {rslider_values[1]}")
    st.write(" ")
    d = st.date_input("Coloque a data do seu aniversário", value=None)
    st.write("Your birthday is:", d)

with st.container():
    st.title("Dashboard GTI 3")
    st.image("assets/tips_img.png")

    # Etapa de carregar os dados
    #df = load_tips_dataset()
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.write("---- Dashboard GTI 2025 -----")
    
    left, middle, right = st.columns(3)
    if left.button("Plain button"):
        left.markdown("You clicked the plain button.")
    if middle.button("Emoji button", icon="😃"):
        middle.markdown("You clicked the emoji button.")
    if right.button("Material button", icon=":material/mood:"):
        right.markdown("You clicked the Material button.")

    # ------------ FIGURA 0 ------------------------
    st.header("Histograma da Gorjeta (tip).")

    fig = make_visualization1(df, rslider_values[0], rslider_values[1])
    st.plotly_chart(fig)
    
    # LINHA 2, DUAS FIGURAS LADO A LADO
    l2_col1, l2_col2 = st.columns(2)

    with l2_col1:
        st.write("COluna 1")
        fig2 = make_vis_tb(df)
        st.plotly_chart(fig2)

    with l2_col2:
        st.write("COluna 2")
        fig3 = make_piechart(df)
        st.plotly_chart(fig3)    

    st.header("Detalhamento do Prompt")

    st.write("Dashboard GTI 2025")

    if st.button("Stream data"):
        st.write_stream(stream_data)