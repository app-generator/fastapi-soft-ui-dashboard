# How to Migrate DB

The database migration tool we are using is `Alembic.` Alembic will help use manage various states of the database, including migrating the database strcuture from an sqlite database to a mysql database. We will go step by step, from beginning a fresh sqlite database, adding the base structure of the database, and finally migrating it over to mysql. All of the commands are to be run in the root folder. 

1. To create your first revision (database version): `alembic revision --autogenerate -m "some information about the update"`

2. A new entry will appear in the `/alembic/versions` folder.

3. The entry will have two functions, upgrade and downgrade. If you used the `--autogenerate` flag, Alembic will attempt to fill in these 2 functions. If Alembic can't autogenerate, you will have to write in the changes to your database manually. 

4. After the function is filled in with the proper set of changes. You will run the command: `alembic upgrade head` to upgrade your database to the latest revision. If you have issues,`alembic downgrade <revision number>` will set your database back to an older revision.


## Migrating to Mysql

5. After you have a revision created, it is fairly easy to switch over mysql. First, you will have to change what database Alembic is pointing to. This is done is the `alembic/env.py` file, line 14. Line 14 is the uri for sqllite, line 15 (commented out) is for mysql. Simply comment out 14, comment in 15. Now alembic is pointing to your database. 

6. Now that Alembic is pointing to your database, migrating your structure over to that database is as simple as running `alembic upgrade head`.




