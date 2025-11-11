"""
Agenda de Contatos - Versão 1.0
Sistema simples para gerenciamento de contatos
"""

contatos = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    
    print("\n--- LISTA DE CONTATOS ---")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def buscar_contato():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    
    nome_busca = input("Digite o nome para buscar: ")
    encontrados = []
    
    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            encontrados.append(contato)
    
    if encontrados:
        print("\n--- CONTATOS ENCONTRADOS ---")
        for i, contato in enumerate(encontrados, 1):
            print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    else:
        print("Nenhum contato encontrado.")

def main():
    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
