import time
from apscheduler.schedulers.background import BackgroundScheduler


def limpa_tudo_roda_script():



def limpa_ativos_roda_todos_busca():
    busca_dados.busca_dados()

def meu_cron_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(limpa_tudo_roda_script, 'interval', minutes=2)
    scheduler.add_job(limpa_ativos_roda_todos_busca, 'interval', minutes=2)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(limpa_tudo_roda_script, 'interval', minutes=1)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
