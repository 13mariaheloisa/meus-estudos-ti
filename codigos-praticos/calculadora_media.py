"""
Projeto: Calculadora de Média Escolar Básica
Descrição: Script em Python para praticar lógica, 
variáveis, operadores aritméticos e condicionais (if/elif/else).
Desenvolvido por: Maria Heloisa
"""

# 1. Definindo as notas do aluno
nota1 = 7.5
nota2 = 8.0
nota3 = 6.0

# 2. Calculando a média aritmética
media = (nota1 + nota2 + nota3) / 3

print(f"Sua média final é: {media:.2f}")

# 3. Estrutura condicional para verificar a situação acadêmica
if media >= 7.0:
    print("Status: Aprovado(a)! Parabéns!")
elif media >= 5.0:
    print("Status: Em recuperação.")
else:
    print("Status: Reprovado(a).")
