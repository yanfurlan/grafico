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
