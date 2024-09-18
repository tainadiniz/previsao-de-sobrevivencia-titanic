# Titanic Survival Prediction App 🚢

Este repositório contém meu primeiro aplicativo desenvolvido em Python, utilizando Streamlit, que permite classificar se uma pessoa, com base em determinados perfis, sobreviveria ou não ao naufrágio do Titanic.

## Introdução

Sou estudante de Ciência de Dados para Negócios na Universidade Federal da Paraíba (UFPB) e desenvolvi este aplicativo durante o 5º período do meu curso, enquanto aprendia sobre regressão logística em uma aula de aprendizagem supervisionada. O objetivo principal deste projeto é aplicar um modelo de classificação para prever a sobrevivência dos passageiros do Titanic com base em suas características.

## Sobre o Projeto

O aplicativo foi desenvolvido com as seguintes ferramentas e bibliotecas:


- **Scikit-learn**: Para implementação do modelo de regressão logística.
- **Pandas**: Para manipulação e análise dos dados.
- **Yellowbrick**: Para visualização das importâncias das features no modelo.

## Pré-requisitos

Para rodar este projeto localmente, você precisará das seguintes bibliotecas:

```python
pip install scikit-learn
pip install pandas
pip install yellowbrick
```
## Conjunto de Dados

Os dados utilizados neste projeto foram extraídos do repositório [hbiostat.org](https://hbiostat.org/data/), e contêm informações detalhadas sobre os passageiros do Titanic.

### Pré-processamento e Normalização dos Dados

Antes de treinar o modelo de regressão logística, foi necessário realizar o pré-processamento e a normalização dos dados

- **Exclusão de Colunas Irrelevantes**: As colunas `name`, `ticket`, `home.dest`, `boat`, `body`, e `cabin` foram excluídas do conjunto de dados, pois não agregam valor direto ao modelo de classificação.

- **Tratamento de Variáveis Categóricas**: As variáveis categóricas foram convertidas em variáveis dummy, facilitando a utilização do modelo de regressão logística.

- **Normalização das Variáveis Numéricas**: As variáveis numéricas como `age`, `sibsp`, `parch`, e `fare` foram normalizadas utilizando a técnica de Min-Max Scaling (ou padronização, dependendo da configuração), o que ajuda a melhorar o desempenho do modelo.
## Explicação das Informações de Previsão:

A partir das informações fornecidas pelo usuário (sexo e idade), o código normaliza esses dados e utiliza um modelo de classificação para prever se essa pessoa teria sobrevivido ou não ao naufrágio do Titanic. A previsão é apresentada ao usuário junto com a probabilidade estimada de sobrevivência. O usuário pode então decidir se deseja realizar outra simulação ou encerrar o programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato

Se você deseja entrar em contato comigo, sinta-se à vontade para me enviar um e-mail ou me conectar no LinkedIn:

- **E-mail**: [tainadiniz9@gmail.com](mailto:tainadiniz9@gmail.com)
- **LinkedIn**: [Tainá Diniz](https://www.linkedin.com/in/tain%C3%A1-diniz-68a711270/)

