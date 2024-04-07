import pandas as pd
import matplotlib.pyplot as plt

# Supondo que as colunas corretas são 'OUT' e 'IN'
# Se os nomes das colunas forem diferentes, ajuste-os conforme necessário
df = pd.read_csv('cir.csv')  # Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV

# Verifique se as colunas estão presentes no DataFrame
#print(df.columns)

plt.plot(df['IN'], df['OUT'], marker='o', linestyle='-')
plt.xlabel('ENTRADA')
plt.ylabel('SAÍDA')
plt.title('Gráfico de Entrada x Saída')
plt.grid(True)
plt.show()