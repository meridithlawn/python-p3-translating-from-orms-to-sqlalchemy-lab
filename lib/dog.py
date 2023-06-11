from models import Dog
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer(), primary_key=True)
    breed = Column(String())
    name = Column(String())

if __name__ == '__main__':

    engine = create_engine('sqlite:///dogs.db')
    

    Session = sessionmaker(bind=engine)
    session = Session()


def create_table(base, engine):
    return base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    for dog in session.query(Dog):
        dog.breed = breed

    session.commit()

    # dog.breed = breed
    # session.add(dog)
    # session.commit()
