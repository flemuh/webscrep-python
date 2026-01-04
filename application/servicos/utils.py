from application import db, tipos
from bson import ObjectId
from unidecode import unidecode

def get_tipo_nome_desc(tipo_id):
    tipo = tipos.find_one({"_id": ObjectId(tipo_id)})
    if tipo:
        return tipo.get("tipo_nome_desc", "")
    return ""


def find_tipo_nomes(nomesTipos):
    if not isinstance(nomesTipos, list):
        nomesTipos = [nomesTipos]

    tipos_array = []
    tipos_encontrados = tipos.find({"tipo_nome": {"$in": nomesTipos}})
    for tipo in tipos_encontrados:
        tipo_info = {
            "_id": str(tipo["_id"]),
            "tipo_nome": tipo["tipo_nome"]
        }
        tipos_array.append(tipo_info)
    return tipos_array

def tipo_nomes_limpar(item):
    item = item.strip()  # Remove espaços em branco no início e no final
    item = item.lower()  # Converte para letras minúsculas
    item = unidecode(item)  # Remove acentuação
    item = item.replace(' ', '')  # Remove espaços em branco dentro da string
    item = item.replace('-', '')  # Remove hífens
    item = item.replace('_', '')  # Remove underscores
    return item


def convertBrltoFloat(brl_value):
    # Remover o símbolo de "R$" e espaços em branco
    value_str = brl_value.replace("R$", "").strip()
    # Substituir a vírgula decimal por um ponto
    value_str = value_str.replace(",", ".")
    # Converter para float
    value_float = float(value_str)
    return value_float

def convertUsdtoFloat(usd_value):
    # Remover o símbolo de "$" e espaços em branco
    value_str = usd_value.replace("$", "").strip()
    # Converter para float
    value_float = float(value_str)
    return value_float
