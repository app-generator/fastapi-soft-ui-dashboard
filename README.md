# [FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html) Soft Dashboard

Open-source [FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html) built on top of a modern `Bootstrap 5` design. Designed for those who like bold elements and beautiful websites, **[Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/)** is ready to help you create stunning websites and web apps. 

> 👉 For more [FastAPI Resources](https://app-generator.dev/docs/technologies/fastapi.html) please access:

- [Getting Started with FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html)
- [FastAPI Cheatsheet](https://app-generator.dev/docs/technologies/fastapi/cheatsheet.html)

<br />

> Product Roadmap 

| Status | Item | info | 
| --- | --- | --- |
| ✅ | **Up-to-date Dependencies** | - |
| ✅ | **[Soft Dashboard Design](https://app-generator.dev/product/soft-ui-dashboard/)** | Designed by **[Creative-Tim(https://app-generator.dev/agency/creative-tim/)** |
| ✅ | **UI Kit** | `Bootstrap 5`, `Dark-Mode` (persistent) |
| ✅ | **Persistence** | `SQLite`, `MySql` |
| ✅ | **Basic Authentication** | classic user/password |
| ✅ | **API** | Products & Sales (linked tables) |
|     |         | GET Requests (public), `get/`, `get/id`  |
|     |         | Mutating requests (Create, UPD, DEL) (reserved for authenticated users) |
| ❌ | **Docker** | Simple Setup (local usage) |
| ❌ | **OAuth** | `Github` & `Twitter` providers |
| ❌ | Unitary tests | - |

<br />

![Soft UI Dashboard - Open-source FastAPI starter provided by by AppSeed.](https://user-images.githubusercontent.com/51070104/175773323-3345d618-0e78-4c85-83fc-f495dc3f0bb0.png)

<br />

## Project Structure

> This application is composed of `3 basic parts` in the root folder.

- `src` provides the codebase for the main application.
- `alembic` manages the DB database migration layer
- `tests` stores the unit testing library.

<br />

## Manual Build

> Download the code 

```bash
$ git clone https://github.com/app-generator/fastapi-soft-ui-dashboard.git
$ cd fastapi-soft-ui-dashboard
```

<br />

> Install modules via `VENV`

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> Create `.env` from `env.sample` - here is a sample 

**Note:** Setting the `debugging` config to `1` will start the app with `SQLite`, setting it to `0` will start the app with `MySql`. 

```env
DEBUGGING=1

DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=somepassword
DATABASE_NAME=somedbname
DATABASE_USERNAME=mayberoot

SECRET_KEY=SUPER_SECRET_HERE
ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

<br />

> Migrate the database (`create tables`)

```bash
$ alembic upgrade head
```

<br />

> Start the app

```bash
$ uvicorn src.app:app --reload
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## ✨ Codebase structure

The project is coded using a modular, intuitive structure as presented below:

```bash
< PROJECT ROOT >
   |
   |-- src/
   |    |
   |    |-- helpers/                        # A simple app that serve HTML files
   |    |    |-- database.py                # Define app routes
   |    |    |-- utils.py                   # Define app routes
   |    |
   |    |-- routers/                        # Handles routes (all sections)
   |    |    |-- auth/                      # Implements authentication routes  
   |    |    |-- ui_routes.py                 
   |    |    |-- user_routes.py
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  models.py                             # Defines the models
   |  config.py                             # Holds APP Configuration
   |  __init__.py                           # Builds the FastAPI object
   |  app.py                                # Bundles ALL resources
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |
   |-- ************************************************************************
```

<br /> 

---
[FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html) Soft Dashboard - Open-source eCommerce Starter provided by [App-Generator](https://app-generator.dev/).
