import re

class RegexProcessos:
    def __init__(self):
        pass

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
