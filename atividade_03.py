# Crie um programa que verifique se uma senha é forte. 
# Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

def verificar_senha(senha):
    """
    Verifica uma senha com base em dois critérios:
    1. Pelo menos 8 caracteres.
    2. Pelo menos um número.
    Retorna dois booleanos: (comprimento_ok, numero_ok)
    """
    
    # Critério 1: Comprimento
    comprimento_ok = len(senha) >= 8
    
    # Critério 2: Pelo menos um número
    numero_ok = False # Começa assumindo que não tem número
    for char in senha:
        if char.isdigit():
            numero_ok = True
            break # Encontrou um número, pode parar de procurar
            
    return comprimento_ok, numero_ok

# --- Início do Programa Principal ---

print("--- Verificador de Senha Forte ---")
print("Regras: Mínimo 8 caracteres e pelo menos 1 número.")
print("Digite 'sair' a qualquer momento para Sair.")
print("-" * 36)

while True:
    senha_digitada = input("Digite uma senha: ")
    
    # 1. Verificar se o usuário quer sair
    if senha_digitada.lower() == 'sair':
        print("\nOperação cancelada pelo usuário.")
        break # Quebra o loop 'while True'

    # 2. Chamar a função de verificação
    comprimento_valido, numero_presente = verificar_senha(senha_digitada)
    
    # 3. Verificar se AMBAS as regras são verdadeiras
    if comprimento_valido and numero_presente:
        print(f"\n[SUCESSO] A senha '{senha_digitada}' é forte!")
        print("Programa encerrado.")
        break # Quebra o loop 'while True', pois a senha é válida
    else:
        # 4. Se a senha for fraca, dar feedback específico
        print("\n[SENHA FRACA]")
        if not comprimento_valido:
            print("- A senha é muito curta (precisa de 8+ caracteres).")
        if not numero_presente:
            print("- A senha não contém nenhum número.")
        print("Por favor, tente novamente.\n")