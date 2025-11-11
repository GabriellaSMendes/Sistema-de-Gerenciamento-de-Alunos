from backend.models.usuario import Usuario
from backend.repositories.usuario_repo import UsuarioRepository

repo = UsuarioRepository()

usuario = repo.listarUsuario()
for user in usuario:
    print(user)
    