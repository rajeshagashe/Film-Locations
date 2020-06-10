# setup and source virtual environment:
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt

# requirements:
SQLite Database
Modules: Flask, SQLAlchemy 

# populate db:
python populate_db.py

# start app:
./run_api.sh development
# Film-Locations
