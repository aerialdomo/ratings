import model
from model import User
import csv

def load_users(session):
    # use u.user
    # open a file
    f = open("user_test.txt")
    fields = ["id", "age", "gender", "occupation", "zipcode"]
    # read a line
    for lines in f:
        # parse a line
        newline = lines.strip("\n").split("|")
        # create an object
        new_object = dict(zip(fields, newline))
        print new_object
        # add the object to a session
        add_object = User(age=new_object['age'], zipcode=new_object['zipcode'])
        session.add(add_object)
        session.commit()
        # commit

    # repeat until done
def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)

# def open_file(filename):
#     f = open(filename).read()


if __name__ == "__main__":
    s= model.connect()
    main(s)
