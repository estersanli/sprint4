quantidade = int(input("Quantos produtos deseja cadastrar? "))

nomes = [""] * quantidade
precos = [0.0] * quantidade
categorias = [""] * quantidade

for i in range(quantidade):
    print(f"\nProduto {i + 1}")

    nomes[i] = input("Nome: ")
    precos[i] = float(input("Preço: R$ "))
    categorias[i] = input("Categoria: ")

valor_filtro = float(
    input("\nDigite um valor para realizar o filtro: R$ ")
)

opcao = input(
    "Digite 1 para produtos acima do valor "
    "ou 2 para produtos abaixo: "
)

print("\nPRODUTOS FILTRADOS:")

encontrou = False

for i in range(quantidade):
    if opcao == "1" and precos[i] > valor_filtro:
        print(
            f"Nome: {nomes[i]} | "
            f"Preço: R$ {precos[i]:.2f} | "
            f"Categoria: {categorias[i]}"
        )
        encontrou = True

    elif opcao == "2" and precos[i] < valor_filtro:
        print(
            f"Nome: {nomes[i]} | "
            f"Preço: R$ {precos[i]:.2f} | "
            f"Categoria: {categorias[i]}"
        )
        encontrou = True

if not encontrou:
    print("Nenhum produto encontrado.")

nomes_crescente = nomes.copy()
precos_crescente = precos.copy()
categorias_crescente = categorias.copy()

for i in range(quantidade - 1):
    for j in range(quantidade - 1 - i):
        if precos_crescente[j] > precos_crescente[j + 1]:

            precos_crescente[j], precos_crescente[j + 1] = (
                precos_crescente[j + 1],
                precos_crescente[j]
            )

            nomes_crescente[j], nomes_crescente[j + 1] = (
                nomes_crescente[j + 1],
                nomes_crescente[j]
            )

            categorias_crescente[j], categorias_crescente[j + 1] = (
                categorias_crescente[j + 1],
                categorias_crescente[j]
            )

nomes_decrescente = nomes.copy()
precos_decrescente = precos.copy()
categorias_decrescente = categorias.copy()

for i in range(quantidade - 1):
    for j in range(quantidade - 1 - i):
        if precos_decrescente[j] < precos_decrescente[j + 1]:

            precos_decrescente[j], precos_decrescente[j + 1] = (
                precos_decrescente[j + 1],
                precos_decrescente[j]
            )

            nomes_decrescente[j], nomes_decrescente[j + 1] = (
                nomes_decrescente[j + 1],
                nomes_decrescente[j]
            )

            categorias_decrescente[j], categorias_decrescente[j + 1] = (
                categorias_decrescente[j + 1],
                categorias_decrescente[j]
            )

categorias_unicas = []

for i in range(quantidade):
    categoria_atual = categorias[i]
    repetida = False

    for j in range(len(categorias_unicas)):
        if categoria_atual == categorias_unicas[j]:
            repetida = True

    if not repetida:
        categorias_unicas.append(categoria_atual)

if quantidade > 0:
    menor_preco = precos[0]
    maior_preco = precos[0]
    soma_precos = 0

    for i in range(quantidade):
        if precos[i] < menor_preco:
            menor_preco = precos[i]

        if precos[i] > maior_preco:
            maior_preco = precos[i]

        soma_precos = soma_precos + precos[i]

    media_preco = soma_precos / quantidade

else:
    menor_preco = 0
    maior_preco = 0
    media_preco = 0

print("\n" + "=" * 50)
print("RELATÓRIO - VERSÃO PORTUGAL")
print("=" * 50)

print("\nPRODUTOS CADASTRADOS:")

for i in range(quantidade):
    print(
        f"Nome: {nomes[i]} | "
        f"Preço: R$ {precos[i]:.2f} | "
        f"Categoria: {categorias[i]}"
    )

print("\nORDEM CRESCENTE:")

for i in range(quantidade):
    print(
        f"{nomes_crescente[i]} - "
        f"R$ {precos_crescente[i]:.2f} - "
        f"{categorias_crescente[i]}"
    )

print("\nORDEM DECRESCENTE:")

for i in range(quantidade):
    print(
        f"{nomes_decrescente[i]} - "
        f"R$ {precos_decrescente[i]:.2f} - "
        f"{categorias_decrescente[i]}"
    )

print("\nCATEGORIAS ÚNICAS:")

for categoria in categorias_unicas:
    print(f"- {categoria}")

print("\nESTATÍSTICAS:")

print(f"Menor preço: R$ {menor_preco:.2f}")
print(f"Maior preço: R$ {maior_preco:.2f}")
print(f"Média dos preços: R$ {media_preco:.2f}")

print("\n" + "=" * 50)
print("FIM DO RELATÓRIO")
print("=" * 50)






