# setup and source virtual environment:
git clone https://github.com/rajeshagashe/Film-Locations.git <br />
virtualenv --python=python3 venv <br />
source venv/bin/activate <br />
pip install -r requirements.txt <br />
touch .env

# populate db:
python populate_db.py

# start app:
./run_api.sh development

# requirements:
SQLite Database <br />
Modules: Flask, SQLAlchemy 

# Film-Locations
