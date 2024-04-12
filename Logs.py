import logging

class MyLogger:
    logger_initialized = False
    
    @classmethod
    def initialize_logger(cls, log_level=logging.INFO):
        if not cls.logger_initialized:
            cls.logger_initialized = True
            cls.logger = logging.getLogger()
            cls.logger.setLevel(log_level)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            console_handler.setFormatter(console_formatter)
            cls.logger.addHandler(console_handler)

    def __init__(self, log_name:str='LOG', log_level=logging.INFO):
        self.log_name = log_name
        self.initialize_logger(log_level)

    def log_debug(self, message):
        """Função que instancia o log_level a nível debug"""
        self.logger.debug(f'{message}')

    def log_info(self, message):
        """Função que instancia o log_level a nível info"""
        self.logger.info(f'{message}')

    def log_warning(self, message):
        """Função que instancia o log_level a nível warning"""
        self.logger.warning(f'{message}')

    def log_error(self, message):
        """Função que instancia o log_level a nível error"""
        self.logger.error(f'{message}')

    def log_critical(self, message):
        """Função que instancia o log_level a nível critical"""
        self.logger.critical(f'{message}')