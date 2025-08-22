def menu():
    menu = """

    ============== MENU =============

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair

    => """
    return input(menu)

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saque):# Essa função deve usar o nome para receber o valor da variável

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    else:
            print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):# Essa função deve usar somente a posição da variável
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):#
    
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(usuarios):
      cpf = input("Informe o CPF (Obs.: Sommente números) : ")
      usuario = filtrar_usuarios(cpf, usuarios)
      
      if usuario:
            print("\n Usuário já existente com este CPF!")
            return
      nome = input("Informe o nome completo:")
      data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
      endereco = input("informe o endereco (logradouro, n° - bairro - cidade/UF): ")

      usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": endereco})
      print("\n Usuário criado com sucesso!")
      
def filtrar_usuarios(cpf, usuarios):
    
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
      cpf = input("Informa o CPF (Obs.: Somente números) : ")
      usuario = filtrar_usuarios(cpf, usuarios)

      if usuario:
            print("\n Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
      
      print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []


    while True:
          opcao = menu()

          if opcao == "d":
                valor = float(input("Informe o valor de depósito: R$ "))

                saldo, extrato = deposito(saldo, valor, extrato)

          elif opcao == "s":
                valor = float(input("Informe o valor do saque: R$ "))

                saldo, extrato = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saque=LIMITE_SAQUES,
                )

          elif opcao == "e":
                exibir_extrato(saldo, extrato=extrato)
       
                
          elif opcao == "nu":
                criar_usuario(usuarios)

          elif opcao == "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                      contas.append(conta)


          elif opcao == "q":
             break

          else:
                print("\n Operação inválida, selecione novamente a opção desejada.")

main()

             

