# Ecommerce

## Setup

On project root, do the following:

1. If you need to create your own local settings please create a copy of settings/local.py.example to settings/local.py
2. Create a copy of .env.example such as `cp.env.example .env`
3. `pip install -r requirements.txt`
4. Run the migrations with `python manage.py migrate`
5. `python manage.py runserver`


## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.