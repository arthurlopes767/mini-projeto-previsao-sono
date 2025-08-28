# Mini Projeto: Previsão de Qualidade e Duração do Sono


## Sobre o projeto:
Este projeto tem como objetivo estimar a qualidade do sono (no intervalo 0–10) e a duração do sono (em horas) a partir de variáveis simples como idade, nível de estresse, profissão e frequência cardíaca. Foi desenvolvido como exercício prático de machine learning, unindo a modelagem de dados com a criação de uma interface interativa.

---

## Tecnologias utilizadas
- Python 3.10+
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Matplotlib / Seaborn
- Plotly Express 

---

## Pré-requisitos
Antes de rodar o projeto, instale as dependências listadas abaixo:

streamlit
pandas
scikit-learn
joblib
matplotlib
seaborn
plotly
numpy

---

## Estrutura do projeto
O repositório contém os seguintes arquivos:
- app_sono.py: O código-fonte do projeto no Streamlit.
- modelo_quality.joblib: O modelo de aprendizado de máquina para prever a qualidade do sono.
- modelo_duration.joblib: O modelo de aprendizado de máquina para prever a duração do sono.
- Sleep_health_and_lifestyle_dataset.csv: O dataset original usado para treinar os modelos.
- requirements.txt: Lista as bibliotecas Python necessárias para executar o aplicativo.

---

## Como executar o projeto localmente
Para executar o projeto na sua máquina, siga os seguintes passos no prompt de comando
1. Clone o repositório

git clone https://github.com/arthurlopes767/mini-projeto-previsao-sono.git
cd mini-projeto-previsao-sono

2. Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate  

*No Windows, use `venv\Scripts\activate`*

3. Instale as dependências

pip install -r requirements.txt

4. Por fim, execute o aplicativo

streamlit run app_sono.py

---

## Autores
 
Arthur Luiz Lopes Araujo (https://www.linkedin.com/in/arthur-luiz-lopes-araujo-391aa3218/)
Gabriela Nogueira (https://www.linkedin.com/in/gabriela-nogueira-5a04a5351/utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
Gustavo Hideki Kato (https://www.linkedin.com/in/gustavo-hideki-kato-287187307/)
Isaque Yikang Chen
Luiz Gabriel Bocalão Costa (https://www.linkedin.com/in/luizgabrielcosta)

Com ajuda de: Lucas Fernandez Gallegov (https://www.linkedin.com/in/lucas-fernandez-gallego/)
