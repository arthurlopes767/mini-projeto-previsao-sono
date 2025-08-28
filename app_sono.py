import streamlit as st
import pandas as pd
from joblib import load
import plotly.express as px
import os

# Carregando Modelos
modelo_quality = load('modelo_quality.joblib')
modelo_duration = load('modelo_duration.joblib')

st.title("Mini Projeto: Previsão de Tempo e Qualidade de Sono")

# Criando guias
abas = st.tabs(["Previsão", "Sobre o Projeto"])

with abas[0]:
    # Inputs
    idade = st.number_input("Idade", min_value=0, max_value=120, value=25)
    nivel_estresse = st.slider("Nível de Estresse", 0, 10, 5)
    profissao = st.selectbox("Profissão",['Saúde', 'Negócios/Corporativo', 'Técnico/Científico', 'Jurídico/Educação'])
    heart_rate = st.number_input("Frequência Cardíaca", min_value=40, max_value=200, value=70)

    # Dataframe
    entrada = pd.DataFrame({
        'Age': [idade],
        'Stress Level': [nivel_estresse],
        'Occupation_Grouped_Negócios/Corporativo': [1 if profissao == 'Negócios/Corporativo' else 0],
        'Occupation_Grouped_Técnico/Científico': [1 if profissao == 'Técnico/Científico' else 0],
        'Occupation_Grouped_Jurídico/Educação': [1 if profissao == 'Jurídico/Educação' else 0],
        'Heart Rate': [heart_rate]
    })

    # Previsão
    pred_quality = modelo_quality.predict(entrada)[0]
    pred_duration = modelo_duration.predict(entrada)[0]

    horas = int(pred_duration)
    minutos = round((pred_duration - horas) * 60)
    if minutos == 60:  
        horas += 1
        minutos = 0

    st.subheader("Resultados da Previsão")
    st.write(f"Qualidade estimada do sono: {pred_quality:.2f} (0 a 10)")
    st.write(f"Duração estimada do sono: {horas:02d}:{minutos:02d} horas")

    # Gráficos
    st.subheader("Análises do Dataset")

    try:
        caminho_arquivo = os.path.join(os.path.dirname(__file__), 'Sleep_health_and_lifestyle_dataset.csv')
        df = pd.read_csv(caminho_arquivo)

        # Matriz de correlação
        numerical_df = df.select_dtypes(include=['number'])
        corr = numerical_df.corr().round(2)
        fig_corr = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Matriz de Correlação"
        )
        st.plotly_chart(fig_corr, use_container_width=True)

        # Boxplot de Estresse (sem pontos)
        fig_stress = px.box(
            df,
            y="Stress Level",
            points=False,
            title="Distribuição do Nível de Estresse"
        )
        st.plotly_chart(fig_stress)

        # Boxplot de Idade (sem pontos)
        fig_age = px.box(
            df,
            y="Age",
            points=False,
            title="Distribuição das Idades"
        )
        st.plotly_chart(fig_age)

    except FileNotFoundError:
        st.warning("CSV do dataset não encontrado. Apenas a previsão está disponível.")

with abas[1]:
    st.header("Sobre o Projeto")
    st.subheader("1. Etapas do Machine Learning")
    st.markdown("""
    <div style="text-align: justify">
    <b>1.1 Exposição e tratamento dos dados:</b> foi feita a importação do dataset Sleep_health_and_lifestyle_dataset.csv. 
    Em seguida, ocorreu a exclusão da coluna de ID por não ter relevância para o modelo, a transformação de variáveis categóricas em binárias 
    (por exemplo, sexo → masculino = 1 e feminino = 0), a separação da pressão sanguínea em duas colunas (sistólica e diastólica) para melhor análise, 
    a categorização da variável desordem do sono em binária (tem ou não tem desordem), além do agrupamento das profissões em quatro grupos principais 
    (Saúde, Negócios/Corporativo, Técnico/Científico e Jurídico/Educação).  
    <br>
    <b>1.2 Análises exploratórias e pré-processamento:</b> foi criada uma matriz de correlação para identificar as variáveis mais relacionadas à qualidade e à duração do sono. 
    Também foram elaborados boxplots para verificar a existência de outliers em idade e nível de estresse, de forma a avaliar a consistência dos dados.  
    <br>
    <b>1.3 Construção e treino dos modelos:</b> após o tratamento e análise, foram desenvolvidos modelos de Machine Learning com o objetivo de prever tanto a qualidade do sono 
    (em escala de 0 a 10) quanto a duração do sono (em horas). Os modelos treinados foram posteriormente salvos em arquivos no formato .joblib, sendo eles 
    modelo_quality.joblib e modelo_duration.joblib.
    <br>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("2. Etapas do Streamlit")
    st.markdown("""
    <div style="text-align: justify">
    <b>2.1 Carregamento dos modelos:</b> os arquivos .joblib gerados na etapa anterior foram carregados dentro do código do aplicativo em Streamlit.  
    <br>
    <b>2.2 Interface com o usuário:</b> o aplicativo solicita ao usuário alguns inputs: idade, nível de estresse (escala de 0 a 10), profissão 
    (escolhida entre quatro grupos previamente definidos) e frequência cardíaca em bpm.  
    <br>
    <b>2.3 Preparação do DataFrame de entrada:</b> os dados fornecidos pelo usuário são organizados em um DataFrame no mesmo formato exigido pelos modelos, 
    incluindo a criação automática de variáveis dummies para os grupos de profissão.  
    <br>
    <b>2.4 Predições:</b> o app realiza a previsão da qualidade do sono (valor entre 0 e 10) e da duração do sono, convertida automaticamente para o formato horas e minutos.  
    <br>
    <b>2.5 Visualização dos resultados:</b> os valores preditos são exibidos na tela de forma clara e amigável ao usuário.  
    <br>
    <b>2.6 Gráficos exploratórios:</b> caso o dataset esteja disponível, o aplicativo também mostra uma matriz de correlação (em formato de heatmap) 
    e boxplots referentes ao nível de estresse e às idades, oferecendo uma análise visual adicional dos dados.  
    <br>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Autores")
    st.markdown("""
    - [Arthur Luiz Lopes Araujo](https://www.linkedin.com/in/arthur-luiz-lopes-araujo-391aa3218/)  
    - [Gabriela Nogueira](https://www.linkedin.com/in/gabriela-nogueira-5a04a5351/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
    - [Gustavo Hideki Kato](https://www.linkedin.com/in/gustavo-hideki-kato-287187307/)  
    - Isaque Yikang Chen  
    - [Luiz Gabriel Bocalão Costa](https://www.linkedin.com/in/luizgabrielcosta)  

    Com ajuda de:
    - [Lucas Fernandez Gallego](https://www.linkedin.com/in/lucas-fernandez-gallego/)  
    """)

