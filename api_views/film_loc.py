from flask import request, jsonify, abort, Blueprint, current_app, render_template
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///movieData.db')
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

film_loc_blueprint = Blueprint('film_loc_blueprint', __name__)

@film_loc_blueprint.route('/', methods=["POST", "GET"])
def item_view():
    '''
    returns locations where movie was shot 
        Parameters:
            title (str) : title of the movie for which locations are to be returned
        Returns:
            locations.html
    '''

    title = request.form.getlist("fname")[0]

    conn = engine.connect()
    s = films.select().where(films.c.title==title)
    result = conn.execute(s)
    
    locations_list = list()
    for row in result:
        locations_list.append(row.locations)

    conn.close()

    return render_template('locations.html', l=set(locations_list), title=title) if locations_list else "Movie not found."