from backend.models.notas import Notas
from backend.repositories.notas_repo import NotasRepository

repo = NotasRepository()

id_aluno = 1  

notas = repo.buscarNota(id_aluno)

print(f"Notas do aluno {id_aluno}:")
print(notas)

