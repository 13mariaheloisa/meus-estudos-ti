"""
Projeto: Gerenciador de Filmes e Séries
Descrição: Script em Python para praticar manipulação de listas, 
laços de repetição e lógica de cadastro de itens.
Desenvolvido por: Maria Heloisa
"""

# 1. Criando uma lista inicial com alguns filmes/séries
lista_desejos = [
    "Interestelar", 
    "A Origem", 
    "Stranger Things", 
    "Homem-Aranha no Aranhaverso"
]

print("--- MINHA LISTA DE FILMES E SÉRIES ---")
print(f"Total de itens na lista: {len(lista_desejos)}")

# 2. Exibindo todos os itens usando um laço de repetição (for)
print("\nFilmes para assistir:")
for indice, filme in enumerate(lista_desejos, start=1):
    print(f"{indice}. {filme}")

# 3. Simulando a adição de um novo filme na lista
novo_filme = "Duna"
lista_desejos.append(novo_filme)

print(f"\n Novo filme adicionado: '{novo_filme}'!")
print(f"Nova quantidade de itens na lista: {len(lista_desejos)}")

# 4. Pequena mensagem motivacional baseada no tamanho da lista
if len(lista_desejos) > 5:
    print("\n Dica: Sua watchlist está enorme! Hora de fazer uma maratona de fim de semana!")
else:
    print("\n Dica: Lista organizada e pronta para o próximo filme!")
