import re

class RegexPJE:
    def __init__(self):
        pass

    def regex_processo(self, string) -> str:
        processo = re.sub('[^0-9]', '', string)

        return processo
    
    def formata_comarca(self, string) -> str:
        # Definindo o padrão de regex para os campos a serem removidos
        padrao = r' - (?:regional|juizado especial).*'
        
        # Substituindo os campos encontrados pelo texto vazio
        comarca_formatado = re.sub(padrao, '', string)
        
        return comarca_formatado

    def regex_id_historia(self, string):
        regex = re.compile(r'1(?!.*1)')

        resultado = regex.sub('4', string)

        return resultado

    def regex_tagHTML(self, string):
        match = re.search(f'>(.*?)</', string)

        if match:
            conteudo = match.group(1).strip()
            return conteudo
        else:
            conteudo = None
            return conteudo

    def regex_capHTML(self, string):
        match = re.sub(r'<.*?>|</.*?>', '', string)

        return match

    def regex_dadoHTML(self, string):
        match = re.sub(r'&nbsp;|RÉU/RÉ:|INVESTIGADO\(A\):', '', string)

        return match

    ##REGEX para dividir a string se presenciar ','

    def extrair_nome_cpf(self, texto):
        padrao = r'(?P<Nome>.+?) - CPF:\s*(?P<CPF>\d{3}\.\d{3}\.\d{3}-\d{2})'
        correspondencias = re.search(padrao, texto)

        if correspondencias:
            nome = correspondencias.group('Nome').strip()
            cpf = correspondencias.group('CPF')
            return nome, cpf
        else:
            return None, None
