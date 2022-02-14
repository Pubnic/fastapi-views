class Database:
    database = {
        'usuarios': [{'id': 1, 'name': 'John', 'age': 30}, {'id': 2, 'name': 'Doe', 'age': 27}],
        'post': [
            {'id': 1, 'title': 'Hello', 'content': 'World', 'author_id': 1},
        ]
    }
    
    def get_usuarios(self):
        return self.database['usuarios']
    
    def get_usuario_por_id(self, id):
        for usuario in self.database['usuarios']:
            if usuario['id'] == id:
                return usuario
        return None
    
    def create_usuario(self, usuario):
        proximo_id = 1
        for usuario_do_banco in self.database['usuarios']:
            if usuario_do_banco['id'] == proximo_id:
                proximo_id += 1
        novo_usuario = {
            **usuario,
            'id': proximo_id
        }
        self.database['usuarios'].append(novo_usuario)
        return novo_usuario
    
    def update_usuario_por_id(self, id, usuario):
        for usuario_do_banco in self.database['usuarios']:
            if usuario_do_banco['id'] == id:
                usuario_do_banco['name'] = usuario.name
                usuario_do_banco['age'] = usuario.age
                return usuario_do_banco
    
    def delete_usuario_por_id(self, id):
        for usuario_do_banco in self.database['usuarios']:
            if usuario_do_banco['id'] == id:
                self.database['usuarios'].remove(usuario_do_banco)
                return None
