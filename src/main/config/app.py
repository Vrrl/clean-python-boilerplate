import os
from dotenv import load_dotenv

from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session, userroles
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python import get_all_cors_headers

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.main.routes.v1 import (
    user_routes,
)

from src.infra.db.sqlalchemy import create_database, DBConnectionHandler

load_dotenv()
create_database(DBConnectionHandler().get_engine())
init(
    app_info=InputAppInfo(
        app_name="oasys",
        api_domain="http://localhost:3567",
        website_domain="http://localhost:8000",
        api_base_path="/auth",
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=os.environ.get("SUPERTOKENS_CONNECTION_URI", "http://localhost:3567"),
        # api_key="key"
    ),
    framework="fastapi",
    recipe_list=[session.init(), emailpassword.init(), userroles.init()],  # initializes session features,
    mode="asgi",  # use wsgi if you are running using gunicorn
)
# TODO: add configure to Logging Level

# Core Application Instance
app = FastAPI(
    title="Oasys Plumber",
    version="v0.0.1",
)

app.add_middleware(get_middleware())

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

# Add Routers
app.include_router(user_routes.router)
