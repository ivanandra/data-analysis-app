import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly_express as px

#title#
st.set_page_config(page_title="Análise de Dados Excel", 
                    page_icon=":bar_chart:", 
                    layout="centered")
        
st.subheader("APP de Análise de Dados Excel")

#sidebar#
st.sidebar.subheader("Configurações e Gráficos")

#fileupload#
uploaded_file = st.sidebar.file_uploader(label="Faça o Upload do seu arquivo CSV ou excel.", type=["csv", "xlsx"])

global df
if uploaded_file is not None:
    try: 
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
try:
    
    numeric_columns = list(df.select_dtypes(exclude=[None]).columns)
    st.sidebar.header("Filtre as colunas da tabela:")
    multi = list()
    for sel in numeric_columns:
        multi.append(sel)

    colunasSelecionadas = st.sidebar.multiselect("Selecione as colunas:", options=multi, default=multi)
    
    drop_these = list(set(list(multi)) - set(colunasSelecionadas))

    df_sel = df.drop(labels=drop_these, axis=1)
    df_sel.head()

    st.write("Dados da planilha:")
    st.dataframe(df_sel)

except Exception as e:
    print(e)
    st.write("Por favor, faça o Upload de um arquivo para visualizar seus dados.")

#select box to configure the chart type#
chart_select = st.sidebar.selectbox(
    label="Selecione o tipo de gráfico",
    options=["Scatterplots", "Lineplots", "Histogram", "Boxplot"]
)

if chart_select == "Scatterplots":
    st.sidebar.subheader("Configurações de gráficos Scatterplot")
    try:
        x_values = st.sidebar.selectbox("Eixo X", options=colunasSelecionadas)
        y_values = st.sidebar.selectbox("Eixo Y", options=colunasSelecionadas)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, title=uploaded_file.name, width=900, height=600)

        st.subheader("Gráficos")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == "Boxplot":
    st.sidebar.subheader("Configurações de gráficos Boxplot")
    try:
        x_values = st.sidebar.selectbox("Eixo X", options=colunasSelecionadas)
        y_values = st.sidebar.selectbox("Eixo Y", options=colunasSelecionadas)

        plot = px.bar(df, x = x_values, y = y_values, title=uploaded_file.name, width=900, height=600)

        st.subheader("Gráficos")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == "Lineplots":
    st.sidebar.subheader("Configurações de gráficos Lineplot")
    try:
        x_values = st.sidebar.selectbox("Eixo X", options=colunasSelecionadas)
        y_values = st.sidebar.selectbox("Eixo Y", options=colunasSelecionadas)

        plot = px.line(df, x = x_values, y = y_values, title=uploaded_file.name, width=900, height=600)

        st.subheader("Gráficos")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == "Histogram":
    st.sidebar.subheader("Configurações de gráficos Histogram")
    try:
        x_values = st.sidebar.selectbox("Eixo X", options=colunasSelecionadas)
        y_values = st.sidebar.selectbox("Eixo Y", options=colunasSelecionadas)

        plot = px.histogram(df, x = x_values, y = y_values, title=uploaded_file.name, width=900, height=600)

        st.subheader("Gráficos")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

#remove streamlit styling#
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    .css-hxt7ib {padding-top: 1rem; padding-bottom: 2rem}
    .css-12oz5g7 {padding-top: 1rem;} 
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
