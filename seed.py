import model
from model import User, Movies, Ratings
import csv
from datetime import datetime #, date
import time

def load_users(session):
    # use u.user
    # open a file
    f = open("user_test.txt")
    fields = ["id", "age", "gender", "occupation", "zipcode"]
    # read a line
    for lines in f:
        # parse a line
        newline = lines.strip("\n").split("|")
        #also can do newline[0]...
        # create an object
        new_object = dict(zip(fields, newline))
        # print new_object
        # add the object to a session
        add_object = User(id= new_object['id'], age=new_object['age'], zipcode=new_object['zipcode'])
        session.add(add_object)
    session.commit()
        # commit

    # repeat until done
def load_movies(session):
    # use u.item
    f = open("movie_test.txt")
    fields = ['id', 'name', 'released_at','video_release' ,'imdb_url' ]
    for lines in f:
        newline = lines.strip("\n").split('|')
        new_object = dict(zip(fields,newline))
        #sqlite3 cant properly display special chars even if it decoded properly, FLask will display it correctly
        name=new_object['name'].decode('latin-1')
        released_at = new_object['released_at']
        struct_time = datetime.strptime(released_at, "%d-%b-%Y").date()
        #decode needs to return to a variable
        add_object = Movies(name=name, released_at=struct_time, imdb_url=new_object['imdb_url'])
        session.add(add_object)
    session.commit()


def load_ratings(session):
    # use u.data
    # user id | item id | rating | timestamp
    f = open("seed_data/u.data")
    fields = ["user_id", "movie_id", "rating", "timestamp"]
    for lines in f:
        newline = lines.strip("\n").split()
        #print newline
        new_object = dict(zip(fields,newline))
        add_object = Ratings(user_id=new_object['user_id'], movie_id=new_object['movie_id'],
            rating=new_object['rating'])
        session.add(add_object)
    session.commit()


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    #load_ratings(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)
