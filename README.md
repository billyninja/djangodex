# djangodex
A small project based on [Pokéapi](https://pokeapi.co/) to assist a tutorial series


## Setup

- git clone
- `cd djangodex`
- Create a virtual env, vary on your machine and tool (in my case: `python -m venv ../venvs/djangodex`)
- Enter the venv (in my case: `source ../venv/bin/activate`)
- `pip install -r requirements.txt`  # install project dependencies
- `python manage.py migrate`  # this will create the sqlite dbase for your
- `python manage.py populate`

