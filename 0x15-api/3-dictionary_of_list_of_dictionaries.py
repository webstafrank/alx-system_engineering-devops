#!/usr/bin/python3
"""
Module for database operations.
"""

import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

def create_database(user, password, host, port, db_name):
    """
    Create a new MySQL database.
    """
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
    conn = engine.connect()
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    conn.close()

def create_table(user, password, host, port, db_name, table_name):
    """
    Creating a new table in the specified database.
    """
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
    metadata = MetaData()
    table = Table(table_name, metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(50)),
                  Column('description', String(200)))
    metadata.create_all(engine)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Database operations.")
    parser.add_argument("--user", required=True, help="Database user")
    parser.add_argument("--password", required=True, help="Database password")
    parser.add_argument("--host", required=True, help="Database host")
    parser.add_argument("--port", required=True, help="Database port")
    parser.add_argument("--db_name", required=True, help="Database name")
    parser.add_argument("--table_name", help="Table name")

    args = parser.parse_args()

    if args.table_name:
        create_table(args.user, args.password, args.host, args.port, args.db_name, args.table_name)
    else:
        create_database(args.user, args.password, args.host, args.port, args.db_name)
