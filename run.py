from application import app
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import cron

import secrets
# Configurar a chave secreta
app.secret_key = ''

# Registrar um manipulador de erro global para tratar exceções em todo o projeto
@app.errorhandler(Exception)
def handle_exception(e):
    # Renderizar uma página de erro personalizada
    print(e)

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(cron.meu_cron_job, 'interval', minutes=1)  # Agendar a tarefa para ser executada a cada minuto
    scheduler.start()

    app.run(debug=True, port=6009)