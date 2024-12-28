from sqlalchemy import create_engine, Column, Integer, String
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


def create_the_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# TABLES

def create_the_table():
    Base.metadata.create_all(engine)

def show_the_table():
    print(Base.metadata.tables)

class Try(Base):
    __tablename__ = 'try'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# CRUD
## CREATE

def create(session):
    new_entry = Try(id=5, name='one')
    session.add(new_entry)
    session.commit()

## READ
def read(session):
    entries = session.query(Try).all()
    for entry in entries:
        print(entry.id, entry.name)

## UPDATE
def update(session):
    entry_to_update = session.query(Try).filter_by(id=5).first()
    entry_to_update.name = 'updated_name'
    session.commit()

## DELETE
def delete(session):
    entry_to_delete = session.query(Try).filter_by(id=5).first()
    session.delete(entry_to_delete)
    session.commit()



def main():
    create_the_table()
    session = create_the_session()

    create(session)
    read(session)
    update(session)
    delete(session)


if __name__ == '__main__':
    main()