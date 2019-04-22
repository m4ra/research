# Django blog for organizing research material (authors, books, images)

## Global Development Requirements

- Python 3.6
- Pip
- Virtualenv
- Postgresql

INSTALATION PREPS
-----------------
1. Create postgresql database:
   (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
   `sudo -u postgres createuser -P -d -r -e -N <username>`
   `createdb -U <username> --locale=en_US.utf-8 <database_name>`
    Try to login to see if new DB has been created and then exit it with CTRL+D or '\q'
    psql -U <username> -d <database_name>
2. Clone repo. Move file research/example_settings.ini to settings.ini and edit the database credentials.
3. Create virtualenv that points to the repo directory.
   Activate it.

Run:
`pip install requirements.txt`
`./manage.py migrate`
`./manage.py runserver`





