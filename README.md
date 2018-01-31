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

# Objectives
- Understand basic Django setup
- Create & update models
- Create endpoints using Django Rest Framework
- TDD an endpoint
- Deal with serializers and nested serializers

# [5] Basic Django Setup
1. Look through codebase
2. Discuss settings and app architecture
3. Commands to run (shell, runserver, migrate)

# [15] Create app and models
1. python manage.py startapp tag
2. create Tag model
3. add to settings
4. python manage.py makemigrations tag
5. python manage.py migrate tag

## Basic Migrations Exercise
1. Add a new field to tag, nullable True and blank True
2. Create the migration
3. Migrate
4. Add another field
5. Create the migration
6. Migrate

# [10] Rolling back, squashing & faking migrations 
1. Fixing erroneous migrations
2. Squashing - why squash?
3. Fake the migration

# [10] Create endpoint for Clients
1. Create some dummy data via the shell
2. Create Django Rest Framework View
3. Create Serializer
4. Add route
5. Check our work

## Notes
1. Do it with a normal API view with the `get` implemented
2. Then a generic ListAPIView

## Exercise
1. Add a field to our serializer
2. Check the result

# [5] Adding computed properties to our serializer
1. Define property on model
2. Expose it as read-only
3. Define property on serializer
4. Expose it as read-only

# [15] TDD a new endpoint
1. Write the test
2. Create the dummy data for the test
3. Write the assertions
4. Run the test
5. Create the endpoint
6. Test should pass

# [15] Nested Serializers
## Exercise
Create a new app and model called Team that just has a field `name` and then add a foreign key to `Team` called `team` on `Client`, nullable, and make the necessary migrations and migrate.

1. Create TeamSerializer
2. Update ClientSerializer to be nested
3. Check our work

## Exercise
Update the test to account for this change.

# [10] Open Q & A

# Next Time
- Optimization