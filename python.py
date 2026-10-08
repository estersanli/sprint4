
produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nProduto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produto = [nome, preco, categoria]
    produtos.append(produto)

valor_filtro = float(
    input("\nDigite um valor para realizar o filtro: R$ ")
)

opcao = input(
    "Digite 1 para produtos acima do valor "
    "ou 2 para produtos abaixo: "
)

produtos_filtrados = []

for produto in produtos:
    if opcao == "1" and produto[1] > valor_filtro:
        produtos_filtrados.append(produto)

    elif opcao == "2" and produto[1] < valor_filtro:
        produtos_filtrados.append(produto)

produtos_crescente = produtos.copy()
produtos_crescente.sort(key=lambda produto: produto[1])

produtos_decrescente = sorted(
    produtos,
    key=lambda produto: produto[1],
    reverse=True
)

categorias = []

for produto in produtos:
    categorias.append(produto[2])

categorias_unicas = set(categorias)

precos = []

for produto in produtos:
    precos.append(produto[1])

if len(precos) > 0:
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_preco = sum(precos) / len(precos)

    estatisticas = (
        menor_preco,
        maior_preco,
        media_preco
    )
else:
    estatisticas = (0, 0, 0)

print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

print("\nPRODUTOS CADASTRADOS:")

for produto in produtos:
    print(
        f"Nome: {produto[0]} | "
        f"Preço: R$ {produto[1]:.2f} | "
        f"Categoria: {produto[2]}"
    )

print("\nPRODUTOS FILTRADOS:")

if len(produtos_filtrados) > 0:
    for produto in produtos_filtrados:
        print(
            f"Nome: {produto[0]} | "
            f"Preço: R$