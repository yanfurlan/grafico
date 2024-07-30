## Ideia base

import matplotlib.pyplot as plt

# Dados para o gráfico de linha
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
vendas = [1500, 1600, 1700, 1400, 1800, 2000, 2100, 2300, 2200, 2400, 2500, 2600]

# Criando o gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='b')
plt.title('Vendas Mensais em 2024')
plt.xlabel('Meses')
plt.ylabel('Vendas (em dólares)')
plt.grid(True)
plt.show()

# Dados para o gráfico de barras
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
quantidade_vendida = [300, 150, 200, 100]

# Criando o gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(produtos, quantidade_vendida, color='green')
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.show()
