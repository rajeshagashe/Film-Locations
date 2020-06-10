import csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///movieData.db', echo=False)
meta = MetaData()
conn = engine.connect()

films = Table(
   'films', meta, 
   Column('id', Integer, primary_key = True), 
   Column('title', String),
   Column('release_yr', Integer),
   Column('locations', String),
   Column('production_company', String),
   Column('distributor', String),
   Column('director', String),
   Column('writer', String),
   Column('actor1', String),
   Column('actor2', String),
   Column('actor3', String),
)
meta.create_all(engine)

with open("source_files/Film_Locations_in_San_Francisco.csv") as f:
    film_details = csv.DictReader(f)
    for film in film_details:
        title = film.get('Title','')
        release_yr = film.get('Release Year','')
        locations = film.get('Locations','')
        production_company = film.get('Production Company','')
        director = film.get('Director','')
        distributor = film.get('Distributor','')
        writer = film.get('Writer','')
        actor1 = film.get('Actor 1','')
        actor2 = film.get('Actor 2','')
        actor3 = film.get('Actor 3','')
        
        ins = films.insert().values(
            title = title,
            release_yr = release_yr,
            locations = locations,
            production_company = production_company,
            director = director,
            distributor = distributor,
            writer = writer,
            actor1 = actor1,
            actor2 = actor2,
            actor3 = actor3,
        )
        conn.execute(ins)