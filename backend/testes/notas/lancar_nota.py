from backend.models.notas import Notas
from backend.repositories.notas_repo import NotasRepository
from datetime import date

repo = NotasRepository()

nota1 = Notas(
    id=None,
    id_disciplina=2,
    aluno_id=1,
    turma_id=1,
    avaliacao="P1",
    nota=9.5,
    data_lancamento=date.today()
)

repo.lancarNotas(nota1)

print("Nota lançada")