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
│   ├── eda.ipynb             # Análise exploratória dos dados (EDA)
│   ├── analysis_gross.ipynb  # Insights e Predição de Faturamento com base no diretor e atores/atrizes
│   └── analysis_imdb.ipynb   # Insights e Predição de notas do IMDb para novos filmes
│
├── reports/
│   ├── eda_report.pdf       # Relatório da análise exploratória dos dados
│   ├── modeling_report.pdf  # Relatório da modelagem preditiva
│   └── final_report.pdf     # Relatório final do projeto
│
├── src/
│   ├── __init__.py
│   ├── gross/
│   │   ├── data_preparation_gross.py  # Scripts para preparação e transformação dos dados de faturamento
│   │   ├── model_training_gross.py    # Scripts para treinamento e avaliação do modelo de faturamento
│   │   └── prediction_gross.py        # Scripts para predição utilizando o modelo treinado de faturamento
│   │
│   └── imdb/
│       ├── data_preparation_imdb.py  # Scripts para preparação e transformação dos dados do IMDb
│       ├── model_training_imdb.py    # Scripts para treinamento e avaliação do modelo do IMDb
│       └── prediction_imdb.py        # Scripts para predição utilizando o modelo treinado do IMDb
│
├── models/
│   ├── model_gross.pkl       # Modelo treinado salvo para faturamento
│   └── model_imdb_rating.pkl       # Modelo treinado salvo para nota do IMDb
│
├── .gitignore               # Arquivos e diretórios a serem ignorados pelo Git
├── README.md                # Instruções de instalação e execução do projeto
├── requirements.txt         # Lista de dependências
└── main_gross.py            # Script principal para faturamento
└── main_imdb_rating.py      # Script principal para nota do IMDb
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
   python main_gross.py
   ```

4. Execute o script principal para nota do IMDb:

   ```
   python main_imdb_rating.py
   ```

## Contribuição

Contribuições são bem-vindas! Para maiores detalhes, consulte o arquivo CONTRIBUTING.md.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
```