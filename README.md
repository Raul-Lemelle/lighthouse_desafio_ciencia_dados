# Projeto IMDb

Este projeto visa desenvolver um modelo de regressão para prever a nota do IMDb de filmes com base em suas características. O projeto inclui desde a preparação dos dados até a aplicação prática do modelo treinado para previsão de notas de novos filmes.

![Workflow do Projeto](https://github.com/Raul-Lemelle/data/blob/main/docs/workflow_imdb.jpg)

## Estrutura do Projeto

```
projeto/
│
├── data/
│   ├── raw/                 # Dados brutos (não processados)
│   ├── processed/           # Dados processados (limpos, transformados)
│   └── external/            # Dados externos adicionais
│
├── notebooks/
│   ├── eda.ipynb                                        # Análise exploratória dos dados (EDA)
│   ├── modelagem_dados_imdb.ipynb                       # Modelagem preditiva
│   ├── analysis_random_forest_regressor_imdb.ipynb      # Insights e predição de notas do IMDb para novos filmes (Random Forest Regressor)
│   ├── analysis_regressao_linear_gross.ipynb            # Insights e predição de faturamento com base no diretor e atores/atrizes (Linear Regression)
│   └── analysis_regressao_linear_imdb.ipynb             # Insights e predição de notas do IMDb para novos filmes (Linear Regression)
│
├── reports/
│   ├── relatorio_eda_imdb.pdf                    # Relatório da análise exploratória dos dados
│   ├── relatorio_previsao_nota_imdb              # Relatório dos modelos de predição
│   └── imdb_relatorio_final_das_analises.pdf     # Relatório final do projeto
│
├── src/
│   ├── __init__.py
│   ├── gross/regressao_linear
│   │   ├── data_preparation_gross.py  # Scripts para preparação e transformação dos dados de faturamento
│   │   ├── model_training_gross.py    # Scripts para treinamento e avaliação do modelo de faturamento
│   │   └── prediction_gross.py        # Scripts para predição utilizando o modelo treinado de faturamento
│   │
│   └── imdb/
│        ├── regressao_linear/
│        │   ├── data_preparation_imdb.py  # Scripts para preparação e transformação dos dados do IMDb
│        │   ├── model_training_imdb.py    # Scripts para treinamento e avaliação do modelo do IMDb
│        │   └── prediction_imdb.py        # Scripts para predição utilizando o modelo treinado do IMDb
│        │      
│        └── random_forest_regressor/ 
│            ├── data_preparation_imdb.py  # Scripts para preparação e transformação dos dados do IMDb
│            ├── model_training_imdb.py    # Scripts para treinamento e avaliação do modelo do IMDb
│            └── prediction_imdb.py        # Scripts para predição utilizando o modelo treinado do IMDb
│
│
│
├── models/
│   ├── modelo_random_forest_imdb.pkl              # Modelo treinado salvo para nota do IMDb (Random Forest Regressor)
│   ├── modelo_regressao_linear_gross.pkl          # Modelo treinado salvo para faturamento (Linear Regression)
│   └── modelo_regressao_linear_imdb_rating.pkl    # Modelo treinado salvo para nota do IMDb (Linear Regression)
│
├── .gitignore                                # Arquivos e diretórios a serem ignorados pelo Git
├── README.md                                 # Instruções de instalação e execução do projeto
├── requirements.txt                          # Lista de dependências
├── CODE_OF_CONDUCT.md                        # Código de conduta do projeto
├── CONTRIBUTING.md                           # Como contribuir no projeto
├── main_random_forest_regressor_imdb.py      # Script principal para nota do IMDb (Random Forest Regressor)
├── main_regressao_linear_gross.py            # Script principal para faturamento (Linear Regression)
└── main_regressao_linear_imdb.py             # Script principal para nota do IMDb (Linear Regression)
```

## Funcionalidades

- **Data**: Contém diretórios para dados brutos, processados e externos.
- **Notebooks**: Inclui notebooks Jupyter para análise exploratória e previsões específicas.
- **Reports**: Documentos em PDF com relatórios detalhados de análises e modelagem.
- **Src**: Código-fonte Python organizado por submódulos (gross para faturamento, imdb para IMDb).
- **Models**: Modelos treinados salvos como arquivos .pkl.
- **.gitignore**: Lista de arquivos e diretórios ignorados pelo controle de versão.
- **README.md**: Documentação principal com instruções de instalação e execução do projeto.
- **requirements.txt**: Dependências necessárias para executar o projeto.

## Instalação e Execução

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório:

   ```
   git clone https://github.com/Raul-Lemelle/lighthouse_desafio_ciencia_dados
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Execute o script principal para faturamento:

   ```
   python main_regressao_linear_gross.py
   ```

4. Execute o script principal para nota do IMDb:

   ```
   python main_regressao_linear_imdb.py
   ```
5. Execute o script principal para nota do IMDb:

   ```
   python main_random_forest_regressor_imdb.py
   ```

## Contribuição

Contribuições são bem-vindas! Para maiores detalhes, consulte o arquivo [CONTRIBUTING.md](https://github.com/Raul-Lemelle/lighthouse_desafio_ciencia_dados/blob/main/CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
```