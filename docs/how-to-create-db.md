# How to create initial DB

The application can run 2 types of databases by simply changing your `DEBUGGING` environment variable.

If you have followed instructions for a manual build in the `README.md` doc,
then you will already have already created a `.env` file. Make sure that DEBUGGING is set 1 (which means True). When the application is run, an empty sqlite `sql_app.db` file will automatically be created in the `/src` folder. 
