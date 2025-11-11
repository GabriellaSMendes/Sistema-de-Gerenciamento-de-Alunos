from backend.repositories.usuario_repo import UsuarioRepository
from backend.models.usuario import Usuario


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
  
        usuario = Usuario(
            id=None,
            nome=nome,
            matricula=matricula,
            email=email,
            senha=senha,
            tipo=tipo
        )
        self.repo.criarUsuario(usuario)
        print("Usuário criado!")

        
        
        
