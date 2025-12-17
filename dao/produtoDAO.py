from modelos.modelos import Produto

class ProdutoDAO:
    def __init__(self, session):
        self.session = session

    def criar(self, produto):
        self.session.add(produto)
        self.session.commit()

    def listar_todos(self):
        return self.session.query(Produto).all()