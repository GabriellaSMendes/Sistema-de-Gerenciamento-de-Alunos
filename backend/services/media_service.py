from backend.repositories.notas_repo import NotasRepository
from backend.repositories.usuario_repo import UsuarioRepository
from backend.repositories.relatorio_repo import RelatorioRepository
from backend.models.relatorio import Relatorio
from backend.models.enum import Situacao

class MediaService:
    
    #construtor
    def  __init__(self):
        self.notas_repo = NotasRepository()
        self.usuario_repo = UsuarioRepository()
        self.relatorio_repo = RelatorioRepository()
        
    #função para calcular média por aluno    
    def calcularMedia(self, id_aluno):
        
        #default
        situacao = Situacao.EM_ANDAMENTO
        media = 0
        
        #verifica se o aluno existe
        usuario = self.usuario_repo.buscarPorID(id_aluno)
        if not usuario:
            print("Aluno não encontrado no sistema.")
            return 0
        
        notas = self.notas_repo.buscarNota(id_aluno)
        if not notas or len(notas) == 0:
            print(f"Nenhuma nota encontrada para o aluno. — Situação: {situacao.value}")
            # grava no relatório mesmo assim
            relatorio = Relatorio(None, id_aluno, 0, Situacao.EM_ANDAMENTO)
            self.relatorio_repo.gravarRelatorio(relatorio)
            return 0 
            
        #cálculo da média
        soma = 0
        for n in notas:
            soma += float(n[5])  # coluna 'nota'
        media = round(soma / len(notas), 2)
        
        #define situação
        if media >= 6:
            situacao = Situacao.APROVADO
        elif 0 < media < 6:
            situacao = Situacao.REPROVADO
        else:
            situacao = Situacao.EM_ANDAMENTO
            
        # grava no relatório
        relatorio = Relatorio(None, id_aluno, media, situacao)
        self.relatorio_repo.gravarRelatorio(relatorio)

        print(f"Média calculada: {media} — Situação: {situacao.value}")
        return media
    