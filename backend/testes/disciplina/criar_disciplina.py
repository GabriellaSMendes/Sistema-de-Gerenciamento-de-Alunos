from backend.models.disciplina import Disciplina
from backend.repositories.disciplina_repo import DisciplinaRepository

repo = DisciplinaRepository()

disciplina1 = Disciplina(
    id=None,
    nome="Matemática",
    cod_disciplina="MAT101",
    id_professor=1
)

repo.criarDisciplina(disciplina1)

print("Disciplina criada")