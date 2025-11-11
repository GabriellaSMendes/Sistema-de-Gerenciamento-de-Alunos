from .enum import Situacao

class Relatorio():
    
    #construtor
    def __init__(self, id, aluno_id, media, situacao: Situacao):
        self.id = id
        self.aluno_id = aluno_id
        self.media = media
        self.situacao = situacao
        
"""    
# Bloco de teste
relatorio1 = Relatorio(
    id=1,
    aluno_id=1,
    media=8.2,
    situacao=Situacao.APROVADO
)

print("ID:", relatorio1.id)
print("Aluno ID:", relatorio1.aluno_id)
print("Média:", relatorio1.media)
print("Situação:", relatorio1.situacao.value)
"""