import json
import os

# Função que le os arquivos json com os dados
class LerJson:
    def __init__(self, nome_arquivo:str, path:str = None):
        self.__arquivo = f'{nome_arquivo}.json'
        self.__path = f'./{path}/' if path != None else None
        self.file = self.__path+self.__arquivo if path != None else self.__arquivo
        self.list_path_files = os.listdir(self.__path)

    def ler_conteudo(self) -> dict:
        """
        Função que ira obter o arquivo que esta sendo manipulado para quarda os status salvos do processo.
        """
        for file in self.list_path_files:
            if self.__arquivo == file:
                with open(self.file, 'r', encoding='utf-8') as file:
                    conteudo = file.read()
                    data = json.loads(conteudo)
                return data

    def quarda_conteudo(self, dicionario: dict):
        """
        Função que ira guarda os dados no arquivo que esta sendo manipulado para salvar.
        """
        with open(self.file, mode='w', encoding='utf-8') as file:
            json.dump(dicionario, file)

    def create_arquivo(self, dicionario: dict):
        """"""
        contador = 1
        for file in self.list_path_files:
            if self.__arquivo == file:
                print("Arquivo encontrado")
                break

            if contador == len(self.list_path_files):
                with open(self.file, 'w', encoding='utf-8') as file:
                    file.write(dicionario)
                    file.close()
            contador += 1
