# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB


with LightDB.File('./light') as db:
    db - 'forkful:fatuity'
with open('./light.unl') as light:
    print(light.read())
# db = DB.LocalDB("./.Clever.unp")
# db.create()
