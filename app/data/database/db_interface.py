# -*- coding:utf-8 -*-
from app.data.database import mysql_database

db = mysql_database.MyDB()


def upsert_table(table, columns, df):
    db.upsert_table(table_name=table, sql_columns=columns, sql_df=df)


def read_data(table, columns):
    db.read_data(table_name=table, sql_columns=columns)


def read_data_from_sql(sql):
    return db.read_data_from_sql(sql=sql)


def truncate_table(table):
    db.truncate_table(table_name=table)
