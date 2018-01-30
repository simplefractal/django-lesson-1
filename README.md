# Installation
1. `mkvirtualenv lesson -p {{ path to python3, which you can get by running `which python3`}}`
2. `pip3 install -r requirements.txt`
3. `createdb lesson_db`
4. `cd collage`
5. `python manage.py migrate`

If you have issues with postgres, for example `django.db.utils.OperationalError: FATAL:  role "root" does not exist`, then go through the following:

1. Enter `psql` to get into the postgres shell.
2. Then inside the postgres shell, run `create user root with superuser;`
3. Then Ctrl+D to quit the shell

