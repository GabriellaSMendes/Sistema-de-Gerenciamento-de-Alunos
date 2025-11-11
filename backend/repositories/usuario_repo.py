from database import conectar


class UsuarioRepository:
    
    #função pra abrir conexão mais fácil
    def abrirConexao(self):
        conexao = conectar()
        cursor = conexao.cursor()
        return(conexao, cursor)
    
    #busca por ID
    def buscarPorID(self, id):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "SELECT * FROM usuario WHERE id = %s",
            (id,)
        )
        
        resultado = cursor.fetchone()
        
        cursor.close()
        conexao.close()
        
        return resultado
    
    #Criar usuário
    def criarUsuario(self, usuario):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "INSERT INTO usuario (nome, matricula, email, senha_hash, tipo) VALUES (%s, %s, %s, %s, %s)",
            (usuario.nome, usuario.matricula, usuario.email, usuario.senha, usuario.tipo.value) 
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        
    #listar usuario
    def listarUsuario(self):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "SELECT * FROM usuario"
        )
        
        resultados = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return resultados