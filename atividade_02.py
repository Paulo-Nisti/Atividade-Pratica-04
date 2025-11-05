# Crie um programa que permita a um professor registrar as notas de uma turma. 
# O programa deve continuar solicitando notas até que o professor digite 'fim'. 
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
# No final, deve exibir a média da turma.



# Lista para armazenar apenas as notas que são válidas
notas_validas = []

print("--- Registro de Notas da Turma ---")
print("Digite as notas (0 a 10). Digite 'fim' para terminar e calcular a média.")
print("-" * 40)

# Inicia um loop infinito que só será interrompido pelo 'break'
while True:
    entrada = input("Digite uma nota (ou 'fim'): ")

    # 1. Verificar condição de saída
    # Usamos .lower() para aceitar 'fim', 'Fim', 'FIM', etc.
    if entrada.strip().lower() == 'fim':
        print("\nEncerrando a entrada de notas...")
        break  # Sai do loop while True

    # 2. Tentar converter a entrada para um número
    try:
        # Tenta converter a string de entrada para um número float
        nota = float(entrada)
        
        # 3. Verificar se o número está no intervalo válido (0 a 10)
        if 0 <= nota <= 10:
            # Se for válido, adiciona à lista
            notas_validas.append(nota)
            print(f"-> Nota {nota} registrada com sucesso.")
        else:
            # Se for um número, mas fora do intervalo
            print(f"[AVISO] Nota inválida: {nota}. As notas devem estar entre 0 e 10.")
            # O loop continua, ignorando esta nota

    except ValueError:
        # 4. Capturar erro se a conversão para float falhar (ex: 'abc')
        print(f"[AVISO] Entrada inválida: '{entrada}'. Por favor, digite um número ou 'fim'.")
        # O loop continua, ignorando esta entrada

# --- Fim do Loop ---

# 5. Calcular e exibir a média
print("-" * 40)
# Verifica se alguma nota válida foi digitada antes de calcular
if len(notas_validas) > 0:
    # Calcula a soma de todas as notas na lista
    soma_das_notas = sum(notas_validas)
    # Calcula a quantidade de notas na lista
    quantidade_de_notas = len(notas_validas)
    # Calcula a média
    media = soma_das_notas / quantidade_de_notas
    
    print(f"Total de notas válidas registradas: {quantidade_de_notas}")
    # Formata a média para exibir com 2 casas decimais
    print(f"A média da turma é: {media:.2f}")
else:
    # Caso o professor digite 'fim' sem inserir nenhuma nota
    print("Nenhuma nota válida foi registrada.")

print("--- Programa encerrado ---")