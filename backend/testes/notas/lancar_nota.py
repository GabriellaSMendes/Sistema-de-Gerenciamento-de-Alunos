from backend.models.notas import Notas
from backend.repositories.notas_repo import NotasRepository
from datetime import date

repo = NotasRepository()

nota1 = Notas(
    id=None,
    id_disciplina=2,
    aluno_id=2,
    turma_id=1,
    avaliacao="P2",
    nota=1,
    data_lancamento=date.today()
)

repo.lancarNotas(nota1)

print("Nota lançada")