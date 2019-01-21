# Flask API - Granter

## Setup

Before anything else, you need to install all needed packages. If you have not started an environment, please do that with the following commands:

```
$ python -m venv env
```

Now you need to start this isolated environment and also export some environment variables. You can do that just sourcing the `.env` file:

```
$ source .env
```

As you can see inside the `.env` file, the following variables were exported and now should be available in your terminal:

```
export FLASK_APP="run.py"
export SECRET="PruV*ut#DxM73BqrhL9JHjwnd"
export APP_SETTINGS="development"
export DATABASE_URL="postgresql://localhost/flask_api"
```

Let's install all the needed packages with the following command:

```
(env) $ pip install -r requirements.txt
```

Type the following commands in your Terminal in order to migrate the models to our PostgreSQL database:

```
(env) $ python manage.py db init
(env) $ python manage.py db migrate
(env) $ python manage.py db upgrade
```

Now you should be able to run the code without any problems.

## How to Use

In order to run the server:

```
python manage.py runserver
```

In order to test the code:
```
python test_estabelecimento.py
python test_produtor.py
python test_unidade_exploracao.py
```
