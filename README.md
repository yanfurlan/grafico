
# Projeto de Visualização de Dados com Python

Este projeto demonstra como criar vários tipos de gráficos usando a biblioteca `matplotlib` em Python. Inclui gráficos de linha, barras, pizza e dispersão, além de anotações e interatividade.

## Requisitos

- Python 3.x
- matplotlib
- numpy
- mplcursors

## Instalação

1. Clone o repositório ou baixe os arquivos.
2. Instale as bibliotecas necessárias usando pip:

```bash
pip install matplotlib numpy mplcursors
```

## Uso

Execute o script `main.py` para visualizar os gráficos.

```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: Script principal que gera os gráficos.
- `README.md`: Arquivo de documentação.

## Funcionalidades

1. **Gráfico de Linha**: Mostra as vendas mensais em 2024.
2. **Gráfico de Barras**: Exibe a quantidade vendida por produto.
3. **Gráfico de Pizza**: Mostra a distribuição de vendas por produto.
4. **Gráfico de Dispersão**: Demonstra uma distribuição aleatória de pontos.
5. **Anotações**: Inclui anotações nos gráficos.
6. **Interatividade**: Permite interatividade com `mplcursors`.

## Exemplo de Código

```python
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# Dados
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
vendas = [1500, 1600, 1700, 1400, 1800, 2000, 2100, 2300, 2200, 2400, 2500, 2600]

produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
quantidade_vendida = [300, 150, 200, 100]

fatias = [40, 30, 20, 10]
labels = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
cores = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico de Linha
axs[0, 0].plot(meses, vendas, marker='o', linestyle='-', color='b')
axs[0, 0].set_title('Vendas Mensais em 2024')
axs[0, 0].set_xlabel('Meses')
axs[0, 0].set_ylabel('Vendas (em dólares)')
axs[0, 0].grid(True)

# Gráfico de Barras
axs[0, 1].bar(produtos, quantidade_vendida, color='green')
axs[0, 1].set_title('Quantidade Vendida por Produto')
axs[0, 1].set_xlabel('Produtos')
axs[0, 1].set_ylabel('Quantidade Vendida')

# Gráfico de Pizza
axs[1, 0].pie(fatias, labels=labels, colors=cores, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Distribuição de Vendas por Produto')

# Gráfico de Dispersão
x = np.random.rand(50)
y = np.random.rand(50)
tamanho = 50 * np.random.rand(50)
cores_disp = np.random.rand(50)

scatter = axs[1, 1].scatter(x, y, s=tamanho, c=cores_disp, alpha=0.5)
axs[1, 1].set_title('Gráfico de Dispersão')
axs[1, 1].set_xlabel('Eixo X')
axs[1, 1].set_ylabel('Eixo Y')

# Anotações
axs[0, 0].annotate('Melhor mês', xy=('Dec', 2600), xytext=('Oct', 2500),
                   arrowprops=dict(facecolor='black', shrink=0.05))

# Interatividade
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target}"))

plt.tight_layout()
plt.show()
```

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
