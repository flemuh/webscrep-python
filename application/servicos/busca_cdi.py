from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def busca_cdi_dados(url):
    dados_cdi = {}

    # Configuração do WebDriver do Chrome (certifique-se de ter o chromedriver instalado)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")  # Tamanho da janela virtual
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Acessa a página
        driver.get(url)

        # Aguarda até que a página esteja totalmente carregada (pode ajustar o tempo conforme necessário)
        driver.implicitly_wait(10)

        # Obtém o conteúdo da página carregada pelo WebDriver
        page_source = driver.page_source

        # Cria o objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        valor_atual = '0%'
        # Valor Atual
        valor_atual_element = soup.find('div', id='taxaPct')

        if valor_atual_element:
            valor_atual = valor_atual_element.get_text(strip=True)
            print("Valor atual:", valor_atual)
        else:
            print("Elemento não encontrado. A estrutura do HTML pode ter sido alterada.")

        dados_cdi['cdi'] = {
            'ativo_nome': 'cdi',
            'ativo_porcentagem': valor_atual,
        }

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # Fecha o navegador após a extração dos dados (verifica se o driver foi inicializado)
        if driver:
            driver.quit()

    return dados_cdi
