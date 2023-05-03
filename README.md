# ALLoy :first_quarter_moon:

## About
ALLoy is a user-friendly web application that allows the rapid subtyping of ALL patients using ALLIUM.

ALLIUM (ALL subtype Identification Using Machine learning) is a multimodal classifier of molecular subtypes in pediatric acute lymphoblastic leukemia, using DNA methylation (DNAm) and gene expression (GEX) data.

## Pre-requisites
Python 3.11+ and Conda

## Conda environment

You will need to activate the `alloy` conda environment before running any subsequent commands.

Install: `conda env create -f environment.yml`

Activate: `conda activate alloy`

Update (after changes to environment.yml): `conda env update --file environment.yml --prune`

## Configure app
Copy `.env.example` to `.env` and configure the latter with your own settings.

## Run
`python manage.py runserver`

