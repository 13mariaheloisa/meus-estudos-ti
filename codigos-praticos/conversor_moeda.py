"""
Projeto: Conversor de moedas simples
Descrição: Script em Python para praticar operações matemáticas básicas 
e formatação de valores monetários.
Desenvolvido por: Maria Heloisa
"""

# 1. Definindo o valor em Reais e a cotação atual do Dólar (exemplo fixo)
valor_em_reais = 150.00
cotacao_dolar = 5.25

# 2. Realizando o cálculo de conversão (Divisão)
valor_em_dolares = valor_em_reais / cotacao_dolar

# 3. Exibindo os resultados formatados bonitinhos com f-strings
print("--- CONVERSOR DE MOEDAS ---")
print(f"Valor original em Reais: R$ {valor_em_reais:.2f}")
print(f"Cotação do Dólar: R$ {cotacao_dolar:.2f}")
print(f"---------------------------")
print(f"Valor convertido: US$ {valor_em_dolares:.2f}")

# 4. Pequena mensagem condicional de incentivo baseada no valor
if valor_em_reais >= 100.00:
    print("\n Dica: Ótimo valor guardado para investimento ou economia!")
else:
    print("\n Dica: Continue juntando para alcançar suas metas financeiras!")
