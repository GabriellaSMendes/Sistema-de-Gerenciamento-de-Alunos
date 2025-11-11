from backend.models.turma import Turma
from backend.repositories.turma_repo import TurmaRepository

repo = TurmaRepository()

turma2 = Turma(
    id=None,
    cod_turma = "TURI2501",
    id_disciplina=2,
    id_professor=1,
    ano=2025,
    semestre=1
)

repo.criarTurma(turma2)

print("Turma criada")