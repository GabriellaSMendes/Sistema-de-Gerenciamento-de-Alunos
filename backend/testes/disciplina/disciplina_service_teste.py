from backend.services.disciplina_service import DisciplinaService

# cria instância da service
serv = DisciplinaService()

print("\n🧩 TESTE 1 — Criar disciplina válida")
serv.criarDisciplina(
    id=None,
    nome="Matemática Aplicada",
    cod_disciplina="MAT102",
    id_professor=1
)

print("\n🧩 TESTE 2 — Criar disciplina com mesmo código (deve dar erro)")
serv.criarDisciplina(
    id=None,
    nome="Matemática 2",
    cod_disciplina="MAT101",
    id_professor=1
)

print("\n🧩 TESTE 3 — Criar disciplina com campo obrigatório faltando (deve dar erro)")
serv.criarDisciplina(
    id=None,
    nome="",
    cod_disciplina="BIO102",
    id_professor=1
)

print("\n🧩 TESTE 4 — Listar disciplinas atuais no banco")
disciplinas = serv.repo.listarDisciplina()
for d in disciplinas:
    print(d)
