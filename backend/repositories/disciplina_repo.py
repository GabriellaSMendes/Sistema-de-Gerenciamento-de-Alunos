from database import conectar

class DisciplinaRepository:
    
    #função pra abrir conexão com o banco
    def abrirConexao(self):
        conexao = conectar()
        cursor = conexao.cursor()
        return conexao, cursor
    
    #criar disciplina
    def criarDisciplina(self, disciplina):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "INSERT INTO disciplina (nome, cod_disciplina, id_professor) VALUES (%s, %s, %s)",
            (disciplina.nome, disciplina.cod_disciplina, disciplina.id_professor)
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
    #listar disciplinas
    def listarDisciplina(self):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "SELECT * FROM disciplina"
        )
        
        
        resultados = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return resultados