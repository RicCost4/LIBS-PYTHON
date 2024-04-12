import random
import string

class GerarSenha:
    def __init__(self):
        pass
    
    def gerar_pass(self) -> str:
        # Define os caracteres permitidos para a senha
        caracteres_permitidos = string.ascii_letters + string.digits + '/*-+@#$%&'
        
        # Primeira letra é maiúscula
        senha = random.choice(string.ascii_uppercase)
        
        # Gera os caracteres restantes
        for _ in range(14):
            caracter = random.choice(caracteres_permitidos)
            senha += caracter
        
        # Garante que não haja caracteres especiais em sequência
        while any(car1 in senha[i:i+2] for i, car1 in enumerate('/*-+@#$%&')):
            senha = ''.join(random.sample(senha, len(senha)))
        
        return senha