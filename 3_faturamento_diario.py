import json

def analisar_faturamento():
    with open('dados.json', 'r') as file:
        dados = json.load(file)

    valores = [d['valor'] for d in dados if d['valor'] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = len([v for v in valores if v > media])

    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Dias acima da média: {dias_acima_media}")

analisar_faturamento()
