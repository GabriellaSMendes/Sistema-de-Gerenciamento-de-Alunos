from backend.models.usuario import Usuario
from backend.repositories.usuario_repo import UsuarioRepository
from backend.models.enum import Tipo

repo = UsuarioRepository()

usuario = Usuario(
    id=None, 
    nome="Roberta Carvalho", 
    matricula="SPO209", 
    email="roberta@email.com", 
    senha="123456", 
    tipo=Tipo.PROFESSOR)

repo.criarUsuario(usuario)

print("Usuário criado.")