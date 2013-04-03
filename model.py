from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

# These are global constants?
engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
										autocommit = False,
										autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here

class User(Base):
	#this class will be stored in a table named users
	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable = True)
	zipcode = Column(String(15), nullable = True)

	# don't need __init__ if we are inheriting from Base
	# def __init__(self, age, zipcode, email = None, password = None):
	# 	self.email = email
	# 	self.password = password
	# 	self.age = age
	# 	self.zipcode = zipcode

class Movie(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key = True)
	name = Column(String(156))
	released_at = Column(Date())
	#released_at = Column(String(50))
	imdb_url = Column(String(156))

	# def __init__(self, name, released_at, imbd_url):
	# 	self.name = name
	# 	self.released_at = released_at
	# 	self.imbd_url = imbd_url

class Rating(Base):
	__tablename__= "ratings"

	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer, ForeignKey('movies.id'))
	user_id = Column(Integer, ForeignKey('users.id'))
	rating = Column(Integer)

	movie = relationship('Movie', backref=backref('ratings'))
	user = relationship('User', backref=backref('ratings', order_by=id))

	# def __init__(self, movie_id, user_id, rating):
	# 	self.movie_id = movie_id
	# 	self.user_id = user_id
	# 	self.rating = rating



### End class declarations
def connect():
	global ENGINE
	global Session

	ENGINE = create_engine("sqlite:///ratings.db", echo=True)
	Session = sessionmaker(bind=ENGINE)

	return Session()

def main():
    """In case we need this for something"""
    session = connect()

if __name__ == "__main__":
    main()
