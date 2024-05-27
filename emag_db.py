import base64
import json
import psycopg2 as ps


def read_config(path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())

    return config


def read_admins(config: dict, table: str = "emag.emag_admin"):

    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"select * from {table}"
            cursor.execute(sql_query)
            admins = cursor.fetchone()
            return admins


def read_products(config: dict, table: str = "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"select name, store, price from {table}"
            cursor.execute(sql_query)
            products = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            products_list = []
            for item in products:
                products_list.append(dict(zip(columns, item)))

            return products_list


def execute_query(sql_query: str, config: dict):
    try:
        with ps.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                print("Successfully executed")
                return cursor.statusmessage

    except Exception as e:
        print(f"Failure on reading on database. Error : {e}")
        return False


if __name__ == '__main__':
    config = read_config()
    admins = read_admins(config)
    products = read_products(config)