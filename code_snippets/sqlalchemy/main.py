from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import os


# Create the engine
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'example.db')
if os.path.exists(db_path):
    os.remove(db_path)
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# TABLES

def create_table():
    Base.metadata.create_all(engine)

def show_tables():
    print(Base.metadata.tables)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    zip = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))


# CRUD

def create(id,name):
    new_entry = Person(id=id, name=name)
    session.add(new_entry)
    session.commit()


def read_all(class_name:str):
    entries = session.query(class_name).all()
    for entry in entries:
        print(entry.id, entry.name)


def update(id:int, new_name:str):
    entry_to_update = session.query(Person).filter_by(id=id).first()
    entry_to_update.name = new_name
    session.commit()


def delete(id):
    session \
        .delete(session.query(Person).filter_by(id=id).first())
    session.commit()


def delete_multiple(*ids):
    for id in ids:
        session \
            .delete(session.query(Person).filter_by(id=id).first())
    session.commit()
    

def main():

    #SETUP

    create_table()
    
    #CRUD
    
    create(5, 'john')
    create(6, 'Jane')
    create(7, 'Joe')

    update(5, 'John Doe')
    
    delete(6)

    #READ
    read_all(Person)
    read_all(Address)


if __name__ == '__main__':
    main()