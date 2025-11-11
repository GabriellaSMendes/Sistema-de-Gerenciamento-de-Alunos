from database import conectar

class RelatorioRepository:
    
    def abrirConexao(self):
        conexao = conectar()
        cursor = conexao.cursor()
        return conexao, cursor
    
    def gravarRelatorio(self, relatorio):
        conexao, cursor = self.abrirConexao()
        cursor.execute(
            "INSERT INTO relatorio (id_aluno, media, situacao) VALUES (%s, %s, %s)",
            (relatorio.aluno_id, relatorio.media, relatorio.situacao.value)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
