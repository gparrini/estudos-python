from django.db import models


# Cliente
    # nome
    # email
    # telefone
    # usuario

# Produto
    # imagem
    # nome
    # preco
    # ativo
    # categoria
    # tipo

# Categorias (Masculino, Feminino, Infantil)
    # nome

# Tipos (Camisa, Camiseta, Bermuda, Calça)
    # nome

# itemestoque
    # produto (ex: camisa)
    # cor (ex: azul, laranja, verde)
    # tamanho (ex: P, M, G)
    # quantidade

# ItensPedido
    # itemestoque (camisa, laranja, M)
    # quantidade (10 itens)

# Pedido
    # cliente
    # data_finalizacao
    # finalizado
    # id_transacao
    # endereco
    # itenspedido

# Endereco
    # rua
    # numero
    # complemento
    # cep
    # cidade
    # estado
    # cliente