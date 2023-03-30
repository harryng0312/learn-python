import contextlib

from module.util.logger_conf import logger

import pyodbc

DB_HOST = "."
DB_PORT = 1433
DB_NAME = "test_db"
DB_UNAME = "sa"
DB_PASSWD = "123456"

DB_DRIVER = "DRIVER={SQL Server};"

@contextlib.contextmanager
def create_conn() -> pyodbc.Connection:
    logger.info(f"openning connection")
    # conn = pyodbc.connect("DRIVER={SQL Server};"
    #                       f"Server={DB_HOST};Port={DB_PORT};"
    #                       f"Database={DB_NAME};User ID={DB_UNAME};Password={DB_PASSWD}")
    conn = pyodbc.connect(DB_DRIVER,
                          server=DB_HOST, port=DB_PORT,
                          database=DB_NAME, user_id=DB_UNAME, password=DB_PASSWD)
    logger.info(f"openned connection")
    conn.autocommit = False
    try:
        yield conn
        pass
    finally:
        close_conn(conn)


def close_conn(conn: pyodbc.Connection) -> None:
    try:
        if not conn.autocommit and not conn.closed:
            conn.commit()
            logger.info(f"commit connection")
            pass
        pass
    except Exception as ex:
        if not conn.closed:
            conn.rollback()
            logger.info(f"rollback connection")
            pass
        raise ex
        pass
    finally:
        if not conn.closed:
            conn.close()
            logger.info(f"closed connection")
            pass
        pass
    pass
