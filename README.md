# Get started

## How to run this project locally:

- Install virtualenv python package to create a virtual environment.

```
pip install virtualenv
```

- Make and start a virtual environment.

For Linux/MacOS:
```
python -m venv .venv
source .venv/bin/activate
```

For Windows:
```
py -m venv .venv
source .venv/Scripts/activate

```

- Install the necessary libraries.

```
pip install -r requirements/development.txt
```

- Migrate Django models.

```
python manage.py migrate
```

- Start the server.

```
python manage.py runserver
```

# Screenshots:
![2023-05-23 (6)](https://github.com/SAMAD101/ToDo-app/assets/71956678/982d4fdf-28ef-41bf-920d-2330309c667d)
![2023-05-23 (7)](https://github.com/SAMAD101/ToDo-app/assets/71956678/3a692bef-83bc-410c-901c-a12af3626e6f)
