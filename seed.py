from app import app, db

from app.models import Sector

def create_example_data():
    with app.app_context():
        sector1 = Sector(
            name='Vale Perdido', 
            city='Quixadá', 
            state='Ceará', 
            description='Setor ótimo com vias de várias graduações', 
            how_to_get_there='O setor é de fácil acesso, ele fica do lado de fora da cidade')
        sector2 = Sector(
            name='Magé', 
            city='Quixadá', 
            state='Ceará', 
            description='Setor escola de Quixadá, as vias são simples, não é necessário fazer trilha', 
            how_to_get_there='Basta seguir pela rua X, a fazenda tem uma placa informando a entrada')

        db.session.add(sector1)
        db.session.add(sector2)
        db.session.commit()

if __name__ == '__main__':
    create_example_data()