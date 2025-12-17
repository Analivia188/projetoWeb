from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

Base = declarative_base()  # <<< Base vive aqui
engine = create_engine('sqlite:///usuarios.db', echo=True)
Session = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(engine)
