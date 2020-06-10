# setup and source virtual environment:
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
touch .env

# populate db:
python populate_db.py

# start app:
./run_api.sh development

# requirements:
SQLite Database
Modules: Flask, SQLAlchemy 

# Film-Locations
