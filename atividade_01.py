# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. 
# A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida

# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.



# Inicia um loop infinito que só será interrompido por um 'break'
while True:
    try:
        # 1. Solicitar e converter o primeiro número
        # O float() tentará converter a entrada. 
        # Se falhar (ex: "abc"), ele levantará um ValueError.
        num1_str = input("Digite o primeiro número: ")
        num1 = float(num1_str)
        
        # 2. Solicitar e converter o segundo número
        num2_str = input("Digite o segundo número: ")
        num2 = float(num2_str)
        
        # 3. Solicitar a operação
        operacao = input("Digite a operação (+, -, *, /): ").strip() # .strip() remove espaços em branco

        # 4. Realizar o cálculo
        resultado = None # Inicializa a variável de resultado
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            # 4a. Tratamento específico para divisão por zero
            if num2 == 0:
                # Levantamos um ZeroDivisionError manualmente para ser pego abaixo
                raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            # 4b. Tratamento para operação inválida
            # Levantamos um ValueError para ser pego abaixo
            raise ValueError(f"Erro: Operação '{operacao}' inválida. Use +, -, * ou /.")
            
        # 5. Se tudo correu bem, exibir o resultado e sair do loop
        print("---------------------------------")
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        print("---------------------------------")
        break # Encerra o loop 'while True'

    # --- Bloco de Tratamento de Erros ---

    except ValueError as e:
        # Pega erros de conversão (float("abc")) E operações inválidas (que levantamos acima)
        print(f"\n[ERRO DE ENTRADA]: {e}")
        print("Por favor, tente novamente.\n")

    except ZeroDivisionError as e:
        # Pega a divisão por zero (que levantamos acima)
        print(f"\n[ERRO DE CÁLCULO]: {e}")
        print("Por favor, tente novamente.\n")
        
    except Exception as e:
        # Pega qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO]: {e}")
        print("Por favor, tente novamente.\n")

print("Calculadora encerrada.")