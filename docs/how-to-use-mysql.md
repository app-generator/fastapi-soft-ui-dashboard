# How to Use Mysql DB

Switching the application over from SQLITE to Mysql is as simple as changing the projects environment variable `DEBUGGING` to 0, which means false. The application will automatically look for a mysql server with the proper authentication. However, it's very important that you already have mysql installed and an empty schema.

Furthermore, the Alembic configuration should be changed so that it is pointing to the correct url. The config for alembic is `/alembic/env.py`.