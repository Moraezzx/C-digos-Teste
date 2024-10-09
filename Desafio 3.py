import json

# Suponha que 'dados_faturamento' seja carregado a partir de um arquivo JSON
dados_faturamento = [100, 200, 0, 300, 400, 0, 500]  # Exemplo

valores = [dia for dia in dados_faturamento if dia > 0]  # Ignora dias sem faturamento
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for dia in valores if dia > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
