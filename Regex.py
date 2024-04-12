import re
from datetime import datetime

class Regex:
    def __init__(self):
        pass

    def convertendo_data(self, data_string:str) -> str:
        """"""
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})', data_string)
        ano, mes, dia = match.groups()

        data_formatada = f'{dia}/{mes}/{ano}'

        return data_formatada
    
    def formatar_data(self, string:str) -> str:
        """"""
        if string != None:
            # Converter a string em formato datetime
            data = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')
            # Formatar a data para exibir apenas o dia
            data_formatada = data.strftime('%Y-%m-%d')
        else:
            data_formatada = string
        
        return data_formatada

    def obtendo_string_sprint(self, string:str) -> str:
        """"""
        padrao = r'(?<=nome=\[)(.*?)(?=\])'

        resultado = re.search(padrao, string)

        if resultado:
            sprint = resultado.group(1)
            return sprint
        else:
            print("Padrão não encontrado.")
            return None

    def inverter_data(self, data:str):
        """"""
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})', data)

        if match:
            ano, mes, dia = match.groups()

            data_invertida = f"{dia}/{mes}/{ano}"
            return data_invertida
        else:
            return None

    def validar_cpf(self, cpf:str)-> bool:
        """"""
        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def regex_limpar_espacos(self, string:str):
        """"""
        # Remove espaços em branco do início e do final da string
        texto_limpo = string.strip()
        return texto_limpo

    def formatar_nome(self, nome: str) -> str:
        """"""
        palavras = nome.split()
        primeira_palavra = palavras[0].capitalize()
        restante_palavras = ' '.join(palavras[1:]).title()
        resultado = primeira_palavra + ' ' + restante_palavras

        return resultado

    def converte_str_list_ponto(self, string:str) -> list:
        """Descricao: Converte string para lista"""
        # Remove espaços inicial e final
        string_formatado = self.regex_limpar_espacos(string)

        # Transforma a frase em uma lista, separada por vírgula e espaço
        lista_palavras = re.split(r',\s*', string_formatado)
        
        # Converte todas as palavras para minúsculas
        lista_palavras = [palavra.lower() for palavra in lista_palavras]
        
        # Mantém apenas os pontos e remove caracteres especiais e acentuação
        lista_palavras_formatadas = [re.sub(r'[^\w.]+', '', unidecode(palavra)) for palavra in lista_palavras]
        
        return lista_palavras_formatadas
    
    def converte_str_list_traco(self, string:str) -> list:
        """Descricao: Converte string para lista"""
        # Remove espaços inicial e final
        string_formatado = self.regex_limpar_espacos(string)

        # Transforma a frase em uma lista, separada por vírgula e espaço
        lista_palavras = re.split(r',\s*', string_formatado)
        
        # Converte todas as palavras para minúsculas
        lista_palavras = [palavra.lower() for palavra in lista_palavras]
        
        # Mantém apenas os traços e remove caracteres especiais e acentuação
        lista_palavras_formatadas = [re.sub(r'[^\w-]+', '', unidecode(palavra)) for palavra in lista_palavras]
        
        return lista_palavras_formatadas

    def converte_str_list(self, string:str) -> list:
        """Descricao: Converte string para lista"""
        # Remove espaços inicial e final
        string_formatado = self.regex_limpar_espacos(string)

        # Transforma a frase em uma lista, separada por vírgula e espaço
        lista_palavras = re.split(r',\s*', string_formatado)
        
        # Converte todas as palavras para minúsculas
        lista_palavras = [palavra.lower() for palavra in lista_palavras]
        
        # Remove caracteres especiais e acentuação
        lista_palavras_formatadas = [re.sub(r'\W+', '', unidecode(palavra)) for palavra in lista_palavras]
        
        return lista_palavras_formatadas
