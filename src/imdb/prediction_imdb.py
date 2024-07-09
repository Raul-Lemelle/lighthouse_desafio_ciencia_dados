import matplotlib.pyplot as plt
import pandas as pd

def print_top_coefficients(model, X):
    # Obtendo os coeficientes do modelo
    coef = pd.Series(model.coef_, index=X.columns)

    # Selecionando os coeficientes mais significativos
    top_coef = coef.sort_values(ascending=False).head(10)
    
    # Exibindo os diretores e atores com maior impacto
    print("Diretores e atores com coeficientes maiores têm um impacto mais significativo no faturamento do filme:")
    for index, value in top_coef.items():
        print(f'{index}: {value:.2f}')

    return top_coef

def plot_top_coefficients(top_coef):
    # Plotando os coeficientes dos diretores e atores mais significativos
    plt.figure(figsize=(10, 6))
    top_coef.plot(kind='bar')
    plt.title('Top 10 Diretores e Atores com Maior Impacto no Faturamento')
    plt.xlabel('Diretor/Atores')
    plt.ylabel('Coeficiente')
    plt.show()