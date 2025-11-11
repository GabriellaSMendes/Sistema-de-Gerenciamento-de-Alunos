from backend.services.usuario_service import UsuarioService
from backend.models.enum import Tipo

# cria uma instância da service
serv = UsuarioService()

"""
print("\n🧩 TESTE 1 — Criar usuário válido")
serv.criarUsuario(
    nome="Julia Maciel",
    email="julia@email.com",
    senha="123456",
    tipo=Tipo.ALUNO,
    matricula="ALU001"
)

print("\n🧩 TESTE 2 — Criar outro usuário com o mesmo e-mail (deve dar erro)")
serv.criarUsuario(
    nome="Julia do Carmo",
    email="julia@email.com",   # mesmo e-mail
    senha="123456",
    tipo=Tipo.ALUNO,
    matricula="ALU002"
)

print("\n🧩 TESTE 3 — Criar outro usuário com a mesma matrícula (deve dar erro)")
serv.criarUsuario(
    nome="Carlos Andrade",
    email="carlos@email.com",
    senha="123456",
    tipo=Tipo.ALUNO,
    matricula="ALU001"        # mesma matrícula da Julia
)
"""

print("\n🧩 TESTE 4 — Tentar criar usuário sem nome (deve dar erro de campo obrigatório)")
serv.criarUsuario(
    nome="",
    email="teste@email.com",
    senha="123456",
    tipo=Tipo.ALUNO,
    matricula="ALU003"
)

print("\n🧩 TESTE 5 — Listar todos os usuários atuais no banco")
usuarios = serv.repo.listarUsuario()
for u in usuarios:
    print(u)
