from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import os



# Create the engine
def setup(db_name:str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, db_name)
    if os.path.exists(db_path):
        os.remove(db_path)
    engine = create_engine(f'sqlite:///{db_path}')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, Base, session
engine, Base, session = setup('db.db')


# TABLES

def create_table():
    Base.metadata.create_all(engine)


def show_tables():
    print(Base.metadata.tables)


def obsolete(cls):
    cls.is_obsolete = Column(Boolean, default=False)
    return cls


def change_obsolete_status(class_name,id, status:bool):
    entry = session.query(class_name).filter_by(id=id).first()
    entry.is_obsolete = status
    session.commit()


# CLASSES

@obsolete
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # is_obsolete attribute is added by the decorator


@obsolete
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    zip = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    # is_obsolete attribute is added by the decorator


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