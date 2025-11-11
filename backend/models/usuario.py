from .enum import Tipo
class Usuario:
    
    #construtor
    def __init__(self, id, nome, matricula, email, senha, tipo: Tipo):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.senha = senha
        self.tipo = tipo
        
    #método pro print não mostrar o endereço de memória
    def __str__(self):
            return (
                f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Email: {self.email}\n"
                f"Tipo: {self.tipo.value}\n"
            )
        

"""  
#Bloco pra testar criando um objeto       
usuario1 = Usuario(
    id=1,
    nome= "Gabi",
    matricula="12345",
    email= "gabi@email.com",
    senha= "#$@#@J@@!KKHHGSKLPOI",
    tipo=Tipo.ALUNO,
    )

print(usuario1)
"""