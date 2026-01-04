import importlib

import numpy as np

from busca_acao import busca_acao_dados
from busca_usd import busca_usd_dados
from busca_cripto import busca_cripto_dados
from busca_cdi import busca_cdi_dados
from busca_selic import busca_selic_dados
from busca_ipca import busca_ipca_dados
from busca_etf import busca_etf_dados
from busca_fii import busca_fii_dados
from busca_fundo import busca_fundo_dados
from application import taxas


def busca_dados():
    urls = [
        # ('cdi', 'https://www.b3.com.br/pt_br/'),

    ]

    for tipo, url in urls:
        try:
            if tipo == 'cdi':
                dados = busca_cdi_dados(url)
                # salvar_campos_no_banco(dados, tipo)

        except ModuleNotFoundError:
            print(f'Módulo busca_{tipo} não encontrado.')
        except AttributeError:
            print(f'Função busca_{tipo} não encontrada no módulo.')


def salvar_campos_no_banco(ativo, tipo):
    for key, value in ativo.items():
        new_dict = {chave: item for chave, item in value.items()}
        taxas.insert_one(new_dict)

busca_dados()
