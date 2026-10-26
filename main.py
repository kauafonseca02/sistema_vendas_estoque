print("\n   SISTEMA DE VENDAS E ESTOQUE     ")

produtos = []
vendas = []

x = 0

while x != 5:
    print("\n     1 - Cadastrar produto       ")
    print("     2 - Listar produtos     ")
    print("     3 - Registrar venda     ")
    print("     4 - Consultar histórico de vendas       ")
    print("     5 - Sair    ")

    try:
        x = int(input("\nQual opção você deseja escolher (1, 2, 3, 4 ou 5)? "))


        if x == 1:
            nome = input("\nNome do produto: ").strip()

            if not nome:
                print("\nO nome do produto não pode ficar vazio. ")

            else:
                duplicado = False

                for produto in produtos:
                    if nome.lower() == produto['nome'].lower():
                        duplicado = True
                        break

                if duplicado:
                    print("\nProduto já cadastrado! ")

                else:
                    while True:
                        try:
                            preco = float(input("Preço do produto: "))

                            if preco <= 0:
                                print("\nO preço deve ser maior que zero. ")
                            else:
                                break

                        except ValueError:
                            print("\nPreço inválido! Digite novamente. ")
                        

                    while True:
                        try:
                            quantidade = int(input("Quantidade em estoque: "))

                            if quantidade < 0:
                                print("\nA quantidade não pode ser negativa.")
                            else:
                                break

                        except ValueError:
                            print("\nQuantidade inválida! Digite novamente.")

                    produto = {
                        "nome": nome,
                        "preco": preco,
                        "quantidade": quantidade
                    }

                    produtos.append(produto)

                    print("\nProduto cadastrado com sucesso!")
                    print(f"Nome: {produto['nome']}")
                    print(f"Preço: R$ {produto['preco']:.2f}")
                    print(f"Estoque: {produto['quantidade']} unidades\n")


        elif x == 2:
            if not produtos:
                print("\nNenhum produto cadastrado. \n")
            else:
                print("\n   PRODUTOS CADASTRADOS    \n")

                for produto in produtos:
                    print(
                        f"Produto: {produto['nome']} - "
                        f"Preço: R$ {produto['preco']:.2f} - "
                        f"Estoque: {produto['quantidade']} unidades "
                    )


        elif x == 3:
            if not produtos:
                print("\nNão há produtos cadastrados para vender. ")
            else:
                nome_venda =  input("Produto à venda: ").strip()

                produto_encontrado = None

                for produto in produtos:
                    if produto['nome'].lower() == nome_venda.lower():
                        produto_encontrado = produto
                        break

                if produto_encontrado is None:
                    print("\nProduto não encontrado. ")

                else:
                    while True:
                        try:
                            quantidade_venda = int(input("Quantidade vendida: "))

                            if quantidade_venda <= 0:
                                print("A quantidade deve ser maior que zero. \n")

                            elif quantidade_venda > produto_encontrado['quantidade']:
                                print("Estoque insuficiente. \n")

                            else:
                                produto_encontrado['quantidade'] -= quantidade_venda
        
                                total = produto_encontrado['preco'] * quantidade_venda
        
        
                                venda = {
                                    "nome": produto_encontrado['nome'],
                                    "quantidade": quantidade_venda,
                                    "total": total
                                }
        
                                vendas.append(venda)
        
                                print("\nVenda realizada com sucesso! ")
                                print(f"Produto: {produto_encontrado['nome']}")
                                print(f"Quantidade vendida: {quantidade_venda}")
                                print(f"Valor total: R$ {total:.2f}")
                                print(f"Estoque restante: {produto_encontrado['quantidade']} unidades ")
                                break

                        except ValueError:
                            print("Você precisa digitar um número inteiro. \n")


        elif x == 4:
            if not vendas:
                print("\nNenhuma venda registrada. ")
            else:
                print("\n   VENDAS REALIZADAS    \n")

                for venda in vendas:
                    print(f"Nome: {venda['nome']}")
                    print(f"Quantidade: {venda['quantidade']}")
                    print(f"Total: R$ {venda['total']:.2f}\n")

                totais = [venda["total"] for venda in vendas]
                faturamento = sum(totais)

                print(f"\nFaturamento total das vendas: R$ {faturamento:.2f}\n")


        elif x == 5:
            print("\nPrograma encerrado. \n")
        else:
            print("\nOpção inválida. \n")

    except ValueError: 
        print("\nDigite um número inteiro valido. \n")
