from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.options import Options

class DriveSelenium:
    def __init__(self, window_size:str ="1840,1080", headless:bool =False):
        self.window_size = window_size
        self.headless = headless

    # @staticmethod
    def create_drive(self) -> WebDriver:
        """
        Classe que cria o Drive com o selenium
        """
        options = Options()

        if self.headless:
            options.add_argument(f"--window-size={self.window_size}") # aumentar o tamanho para deixar alguns elemento acessivel
            options.add_argument("--headless") # Roda o driver em background
            options.add_argument("--no-sandbox") # Precisa para rodar no linux
            options.add_argument("--disable-dev-shm-usage")  # Precisa para rodar no Docker 
            options.add_argument("--remote-debugging-port=9222")  # Precisa para rodar no linux
            ## TESTE
            # options.add_argument('--disable-gpu')
            # options.add_argument('--disable-software-rasterizer')
            # options.add_argument('--disable-extensions')

        if not self.headless:
            options.add_argument("--start-maximized")

        # Cria o driver com os options
        driver = WebDriver(options=options)

        # if self.headless:
        #     driver.set_page_load_timeout(60)

        return driver