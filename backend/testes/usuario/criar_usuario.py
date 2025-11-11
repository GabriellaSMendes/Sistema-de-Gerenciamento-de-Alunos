from backend.models.usuario import Usuario
from backend.repositories.usuario_repo import UsuarioRepository
from backend.models.enum import Tipo

repo = UsuarioRepository()

usuario = Usuario(
    id=None, 
    nome="Gabriella Mendes", 
    matricula="SPO315", 
    email="gabriella@email.com", 
    senha="123456", 
    tipo=Tipo.ALUNO)

repo.criarUsuario(usuario)