from enum import Enum


class Tipo(Enum):
    ALUNO = "ALUNO"
    PROFESSOR = "PROFESSOR"
    ADMIN = "ADMIN"
    
class Situacao(Enum):
    APROVADO = "APROVADO"
    REPROVADO = "REPROVADO"
    EM_ANDAMENTO = "EM ANDAMENTO"