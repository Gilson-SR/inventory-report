from inventory_report.inventory.product import Product


def test_cria_produto():
    MESSAGE = "Mantenha em local seco e arejado"
    product = Product(
        id=1,
        nome_do_produto="Produto Teste 1",
        nome_da_empresa="Empresa Teste",
        data_de_fabricacao="2023-01-01",
        data_de_validade="2024-01-01",
        numero_de_serie="0102030405",
        instrucoes_de_armazenamento="Mantenha em local seco e arejado"
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto Teste 1"
    assert product.nome_da_empresa == "Empresa Teste"
    assert product.data_de_fabricacao == "2023-01-01"
    assert product.data_de_validade == "2024-01-01"
    assert product.numero_de_serie == "0102030405"
    assert product.instrucoes_de_armazenamento == MESSAGE
