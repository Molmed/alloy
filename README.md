# ALLoy :first_quarter_moon:

## About
ALLoy is a user-friendly web application that allows the rapid subtyping of ALL patients using ALLIUM.

[ALLIUM](https://github.com/Molmed/allium) (ALL subtype Identification Using Machine learning) is a multimodal classifier of molecular subtypes in pediatric acute lymphoblastic leukemia, using DNA methylation (DNAm) and gene expression (GEX) data.

## Pre-requisites
Docker. Alternatively, Python 3.11+ and Conda.

## Running with Docker
```
docker build --tag 'alloy' .
docker run -d -p 8000:8000 alloy
```

## Running with Conda

### Configure Conda env
You will need to activate the `alloy` conda environment before running any subsequent commands.

Install: `conda env create -f environment.yml`

Activate: `conda activate alloy`

Update (after changes to environment.yml): `conda env update --file environment.yml --prune`

### Configure app
Copy `.env.example` to `.env` and configure the latter with your own settings.

### Run
`python manage.py runserver`

