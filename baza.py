from pony import orm
from uuid import uuid4
from datetime import datetime
import datetime as dt
import os

db =orm.Database()
db.bind(provider='sqlite',filename='baza.sqlite',create_db=True)


class Ormar(db.Entity):
	naziv = orm.Required(str)
	velicina = orm.Required(str)
	vlasnik = orm.Required(str)
	datum = orm.Required(datetime)

class Stalak_za_obucu(db.Entity):
	naziv = orm.Required(str)
	velicina = orm.Required(str)
	vlasnik = orm.Required(str)
	datum = orm.Required(datetime)



db.generate_mapping(create_tables=True, check_tables=True)

