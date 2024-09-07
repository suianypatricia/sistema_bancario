menu = """

Olá, seja bem vindo(a) ao Banco Digital!
Digite o número da operação que deseja realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


# Inicializando as principais variáveis: saldo, limite, extrato, número de saques e o limite de saques
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
# Constante LIMITE_SAQUES (valor fixo que não deve ser alterado)
LIMITE_SAQUES = 3

# Loop que apresenta o menu e espera a operação desejada pelo usuário
while True:
   # Exibe o menu e recebe a operação escolhida pelo usuário
    operacao = input(menu)

    # Se a operação for "1", será depósito
    if operacao == "1":
        valor = float(input(" Digite o valor que deseja realizar o depósito: "))
        # Verifica se o valor do depósito é positivo
        if valor > 0:
           saldo += valor # Atualiza o saldo com o valor do depósito ( o += significa "saldo = saldo + valor").
           extrato += f"Depósito: R$ {valor:.2f}\n" # Adiciona a transação no extrato
           print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")  # Mensagem de sucesso 

        # Informa falha se o valor for inválido
        else:
            print("Operação falhou devido ao valor informado ser inválido.")

    # Se a operação for "2", será saque
    elif operacao == "2":
        valor = float(input("Digite o valor que você deseja realizar o saque: "))
        # Verifica se o saque excede o saldo disponível
        excedeu_saldo = valor > saldo
        #Verifica se o saque excede o limite diário permitido 
        excedeu_limite = valor > limite
        # Verifica se o número de saques diários permitidos foi ultrapassado de acordo com a constante (3)
        excedeu_saques = numero_saques >= LIMITE_SAQUES


       # Condições para falhas
        if excedeu_saldo:
            print("Operação falhou pois você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"Operação falhou: o valor máximo para saque é R$ {limite:.2f} por vez.")

        elif excedeu_saques:
            print("Operação falhou devido ao número máximo de saques diários excedidos.")

    # Se o valor do saque for válido e não exceder as restrições, realiza a operação
        elif valor > 0:
            saldo -= valor   # Deduz o valor sacado do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona a transação de saque no extrato
            numero_saques += 1  # Incrementa o número de saques realizados
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")  # Mensagem de sucesso
        # Informa falha se o valor for inválido
        else:
            print("Operação falhou pois o valor informado é inválido.")

    # Se a operação for "3", o extrato será exibido
    elif operacao == "3":
        print("\n --------------- EXTRATO BANCÁRIO -------------------")
        # Exibe uma mensagem informando se não houve movimentações ou imprime o extrato completo
        print("Não foram realizadas movimentações." if not extrato else extrato)
        # Mostra o saldo atual após as operações
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------------------")

    # Operação 4: Sair
    elif operacao == "4":
        print("Obrigado(a) por usar nosso sistema bancário! Até a próxima.")
        break

    # Se o usuário digitar uma opção inválida, será mostrada uma mensagem de erro.
    else:
        print("Operação inválida. Por favor, digite novamente um número válido correspondente a operação desejada.")