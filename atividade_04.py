# Crie um programa que solicite ao usuário que insira números inteiros. 
# O programa deve continuar solicitando números até que o usuário digite 'fim'. 
# Para cada número inserido, o programa deve informar se é par ou ímpar. 
# Se o usuário inserir algo que não seja um número inteiro, 
# o programa deve informar o erro e continuar. 
# No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.


# 1. Inicializa os contadores fora do loop
contador_pares = 0
contador_impares = 0

print("--- Contador de Números Pares e Ímpares ---")
print("Digite números inteiros. (Digite 'fim' para encerrar)")
print("-" * 45)

# 2. Inicia o loop infinito
while True:
    entrada = input("Digite um número (ou 'fim'): ")

    # 3. Verifica a condição de saída (de forma robusta)
    if entrada.strip().lower() == 'fim':
        print("\nEncerrando a entrada de números...")
        break  # Sai do loop while

    # 4. Tenta executar o bloco de código "perigoso"
    try:
        # Tenta converter a entrada para um NÚMERO INTEIRO
        numero = int(entrada)
        
        # Se a conversão for bem-sucedida, classifica o número
        if numero % 2 == 0:
            print(f"-> {numero} é PAR.")
            contador_pares += 1  # Incrementa o contador de pares
        else:
            print(f"-> {numero} é ÍMPAR.")
            contador_impares += 1 # Incrementa o contador de ímpares
            
    # 5. Se o 'try' falhar, captura o erro
    except ValueError:
        # Este bloco é executado se int(entrada) falhar
        # (ex: "abc", "1.5", "cinco")
        print(f"[ERRO] Entrada inválida: '{entrada}'. Por favor, digite um NÚMERO INTEIRO ou 'fim'.")
        # O loop continua automaticamente, pedindo nova entrada

# --- Fim do Loop ---

# 6. Exibe o relatório final
print("-" * 45)
print("--- Relatório Final ---")
print(f"Total de números PARES inseridos: {contador_pares}")
print(f"Total de números ÍMPARES inseridos: {contador_impares}")
print("--- Programa encerrado ---")