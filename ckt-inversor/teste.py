import pandas as pd

with open('cir.csv', 'r') as file:
    lines = file.readlines()

# Substituir espaços por vírgulas em cada linha
lines = [line.replace(' ', ';') for line in lines]

# Escrever de volta para o arquivo
with open('cir.csv', 'w') as file:
    file.writelines(lines)

print("Espaços substituídos por vírgulas no arquivo 'cir.csv'.")

