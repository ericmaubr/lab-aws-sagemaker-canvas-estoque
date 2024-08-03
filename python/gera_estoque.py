import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parâmetros do dataset
num_days = 30
num_products = 25
initial_stock = 2000

# Inicialização
date_range = [datetime(2023, 12, 31) + timedelta(days=i) for i in range(num_days)]
product_ids = list(range(1, num_products + 1))

# Criação de DataFrame vazio
data = []

# Gera os dados para cada dia e produto
for i in range(num_days):
    current_date = date_range[i]
    
    for product_id in product_ids:
        # Define a quantidade de estoque para o primeiro dia
        if i == 0:
            stock = initial_stock - np.random.randint(0, 100)
        else:
            # No dia seguinte, o estoque deve ser menor ou igual ao do dia anterior
            # Garante que o estoque não aumente
            prev_day_stock = [row[3] for row in data if row[0] == product_id and row[1] == date_range[i - 1].strftime('%Y/%m/%d')]
            prev_stock = prev_day_stock[0] if prev_day_stock else initial_stock
            stock = max(0, prev_stock - np.random.randint(0, 50))
        
        flag_promotion = np.random.choice([0, 1], p=[0.7, 0.3])  # 30% de chance de promoção
        
        data.append([product_id, current_date.strftime('%Y/%m/%d'), flag_promotion, stock])

# Criar DataFrame e salvar como CSV
df = pd.DataFrame(data, columns=['ID_PRODUTO', 'DIA', 'FLAG_PROMOCAO', 'QUANTIDADE_ESTOQUE'])
df.to_csv('historico_vendas.csv', index=False)

print("Arquivo CSV 'historico_vendas.csv' criado com sucesso.")
