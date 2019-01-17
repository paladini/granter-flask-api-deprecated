# Flask API - Granter

## Description

TODO

## How to Setup

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

Now you should be able to run the code without any problems.

## How to Use

TODO.