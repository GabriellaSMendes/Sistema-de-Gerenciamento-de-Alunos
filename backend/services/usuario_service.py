from backend.repositories.usuario_repo import UsuarioRepository
from backend.models.usuario import Usuario
from backend.models.enum import Tipo

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()
         
    #criar usuario
    def criarUsuario(self, nome, matricula, email, senha, tipo):
        usuarios = self.repo.listarUsuario()

        #campos obrigatórios
        if not nome or not email or not senha or not tipo or not matricula:
            print ("Existem campos obrigatórios.")
            return
        
        for u in usuarios:
            if u[3] == email:
                print("Já existe um usuário com esse email.")
                return
            
            elif u[2] == matricula:
                print("Já existe um usuário com essa matrícula.")
                return
            
        # transforma string em Enum-- feito com chat pois nao estava conseguindo resolver o erro
        if isinstance(tipo, str):
            try:
                tipo = Tipo(tipo.upper())   # "aluno" → Tipo.ALUNO
            except:
                print("Tipo inválido.")
                return
  
        usuario = Usuario(
            id=None,
            nome=nome,
            matricula=matricula,
            email=email,
            senha=senha,
            tipo=Tipo(tipo)
        )
        self.repo.criarUsuario(usuario)
        print("Usuário criado!")
