#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


temp_db_params = {
    "username": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
}


def temp_db_connection():
    url = URL("postgresql", **temp_db_params)
    return create_engine(url)
