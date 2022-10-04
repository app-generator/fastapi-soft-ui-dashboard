# FastAPI Soft Dashboard

Open-source starter powered by FastAPI on top of **[Soft UI Dashboard](https://github.com/app-generator/ct-soft-ui-dashboard-enh)** (free version). 

> UI Kit: [Soft UI Dashboard](https://github.com/app-generator/ct-soft-ui-dashboard-enh) **v1.0.6-enh1**

<br />

> Product Roadmap 

| Status | Item | info | 
| --- | --- | --- |
| ❌ | **Up-to-date Dependencies** | - |
| ❌ | **Best Practices** | This [guide](https://github.com/zhanymkanov/fastapi-best-practices) used as reference |
| ❌ | **Simple, Intuitive Codebase** | [More info](https://github.com/app-generator/fastapi-soft-ui-dashboard/issues/1) |
| ❌ | **UI Kit** | `Bootstrap 5`, `Dark-Mode` (persistent) |
| ❌ | **Persistence** | `SQLite`, `MySql` |
| ❌ | **Basic Authentication** | classic user/password |
| ❌ | **OAuth** | `Github` & `Twitter` providers |
| ❌ | **API** | Products & Sales (linked tables) |
|     |        | GET Requests (public), `get/`, `get/id`  |
|     |        | Mutating requests (Create, UPD, DEL) (reserved for authenticated users) |
| ❌ | **Docker** | Simple Setup (local usage) |

> Something is missing? Submit a new `product feature request` using the [issues tracker](https://github.com/app-generator/fastapi-soft-ui-dashboard/issues).

<br />

## How to used in `Docker`
> Production Docker
   - The default docker-compose.yaml file is to be used for production.
   - This particular docker-compose houses the `mysql configuration`.
   - in the root folder, enter the following command (without the quotes): `docker-compose up`.

> Developerment Docker
   - The docker-compose-dev.yaml file is to be used for Developerment.
   - This particular docker-compose houses the `sqlite configuration`.
   - in the root folder, enter the following command (without the quotes): `docker-compose -f docker-compose-dev.yaml`.

@ToDo

<br />

## The manual build
> This application is composed of `3 basic parts` in the root folder.
   1. src store the codebase for the main application.
   2. alembic stores the database migration library.
   3. tests stores the unit testing library.

> The following are `steps on how to manually build the fastapi app`. All of the commands are to be entered in the root directory.
   1. create a virtual environment with the following command (always without the quotes): `python -m venv venv`
   2. activate the virtual environment, for linux/ubuntu: `source/bin/activate`, for windows `source/Scripts/activate`
   3. install the dependencies: `pip install -r requirements.txt`
   4. create a `.env` file, then copy and paste-in the contents of `.env.dist`, and fill in the configuration with your credentials.
      > setting the `debugging` config to `1` will start the app with sqlite, setting it to `0` will start the app with mysql.  
   5. run the application: `uvicorn src.app:app --reload`

@ToDo


```bash
$ # All steps below
```

Access the `app` section in the browser: `http://127.0.0.1:5000/`

<br />

## ✨ Code-base structure

@ToDo - The project structure (to be updated) 


```bash
< PROJECT ROOT >
   |-- .github/                         # Folder having github configurations
   |   |-- workflows/                   # Folder having github workflow configurations
   |       |-- main.yml                 # Main workflow for automated unit testing/syntax check
   |       |-- release.yml              # Release workflow to release code when PR merged in main
   |   |-- CODEOWNERS                   # List of codeonwers, special check can be made in repo settings
   |   |-- PULL_REQUEST_TEMPLATE.md     # PR template
   |   |-- dependabot.yml               # Dependabot configurations (optional)
   |-- docs/                            # Folder to contain any helping docs
   |   |-- api_examples.json            # Example doc
   |-- scripts/                         # Folder to contain any SQL scripts
   |   |-- scripts.sql                  # Example script
   |-- src/                             # Folder having all the python code
   |    |-- models                      # Folder having all models
   |       |-- custom/                  # Folder for custom models
   |       |-- db/                      # Folder for database models
   |           |-- product.py           # Example file for product model
   |           |-- sales.py             # Example file for sales model
   |       |-- request.py               # File containing all request models
   |       |-- response.py              # File containing all response models
   |    |-- routers/                    # Folder for all FastAPI routes
   |        |-- v1/                     # Folder for v1 version
   |            |-- auth/               # Folder for authentication routes
   |                |-- auth_routes.py  # File containing authentication routes for v1
   |            |-- product_routes.py   # File containing product routes for v1
   |            |-- sales_routes.py     # File containing sales routes for v1
   |        |-- healthcheck.py          # Base file for healthcheck for FastAPI
   |    |-- helpers/                    # Folder containing helper methods
   |        |-- product_helpers.py      # File having product related helper methods
   |        |-- sales_helpers.py        # File having sales related helper methods
   |        |-- common_helpers.py       # File having common helper methods
   |        |-- database.py             # File having database connection and methods
   |        |-- cache.py                # File having cache connection and methods
   |        |-- decorators.py           # File having decorators
   |    |-- static/
   |         |-- <css, JS, images>      # CSS files, Javascripts files
   |    |-- templates/                  # Templates used to render pages
   |         |-- includes/              # HTML chunks and components
   |              |-- navigation.html   # Top menu component
   |              |-- sidebar.html      # Sidebar component
   |              |-- footer.html       # App Footer
   |              |-- scripts.html      # Scripts common to all pages
   |         |-- layouts/               # Master pages
   |              |-- base-fullscreen.html  # Used by Authentication pages
   |              |-- base.html         # Used by common pages
   |         |-- accounts/              # Authentication pages
   |              |-- login.html        # Login page
   |              |-- register.html     # Register page
   |         |-- home/                  # UI Kit Pages
   |              |-- index.html        # Index page
   |              |-- 404-page.html     # 404 page
   |              |-- *.html            # All other pages
   |    |-- app.py                      # Containing main method, project startup
   |    |-- config.py                   # Containing Settings class for fetching configurations
   |    |-- constants.py                # Global constants
   |    |-- exception_handlers.py       # Global exception handling
   |
   |-- tests/                           # Folder having tests
   |    |-- __init__.py                 # Containing test startup
   |    |-- v1/                         # Tests for version v1
   |        |-- __init__.py
   |        |-- test_v1.py              # Containing tests for version v1
   |
   |-- .env.dist                        # Template for environment variables
   |-- .env                             # Actual environment variables file
   |-- .gitignore                       # File containing git ignore configurations                           
   |-- CHANGELOG.md                     # File containing change logs
   |-- LICENSE                          # File containing license information
   |-- Dockerfile                       # Docker file
   |-- Makefile                         # File containing make commands
   |-- README.md                        # README file
   |-- docker-compose.yaml              # File to run docker along with other dependencies
   |-- requirements.txt                 # Python packages dependencies
   |-- package-lock.json                # npm packages information
   |-- package.json                     # npm packages dependencies
   |
   |-- ************************************************************************
```

<br /> 

---
**FastAPI Soft Dashboard** - Open-source Starter provided by **[AppSeed](https://appseed.us/)**
