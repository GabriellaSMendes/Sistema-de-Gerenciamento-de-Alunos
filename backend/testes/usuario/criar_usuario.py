from backend.models.usuario import Usuario
from backend.repositories.usuario_repo import UsuarioRepository
from backend.models.enum import Tipo

repo = UsuarioRepository()

usuario = Usuario(
    id=None, 
    nome="Jade Picao", 
    matricula="SPO210", 
    email="jade@email.com", 
    senha="123456", 
    tipo=Tipo.ALUNO)

repo.criarUsuario(usuario)

print("Usuário criado.")