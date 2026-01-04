from bson import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://"

# Conexão com o MongoDB
mongo = PyMongo(app)
db = mongo.db

db_name = 'fundos'

try:
    # Tente buscar um documento na coleção "fundos". Não importa se ele existe ou não.
    db[db_name].find_one()
    print("Conexão bem sucedida com o banco de dados!")
except (ServerSelectionTimeoutError, OperationFailure):
    # A conexão falhou. Imprima uma mensagem de erro mais amigável e termine a execução do programa.
    print("\nHouve um erro ao tentar conectar com o banco de dados.")
    print("Por favor, verifique se a URI de conexão está correta e se o serviço MongoDB está em execução e acessível.")
    print("Se o problema persistir, entre em contato com o administrador do sistema.\n")
    exit()

taxas = db['taxas']  # Coleção taxas

from application import routes
