# Import libraries
import os
import sys
import logging
import sqlite3 as sql

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

logger.debug('logging start')


def connect_to_database(database_name):
    """

    :param database_name:
    :return:
    """
    data_dir_path = os.path.join(os.getcwd(), 'database')
    database_path = os.path.join(data_dir_path, database_name)

    if os.path.exists(data_dir_path):
        logger.debug(f'directory {data_dir_path} is exists.')
    else:
        logger.debug(f'directory {data_dir_path} is NOT  exists.')
        try:
            os.mkdir(data_dir_path, mode=0o777)
            # sys.path.append(data_dir_path)
        except:
            logger.error(f'is not possible to create directory {data_dir_path}')
            return None

    if os.path.exists(database_path):
        logger.debug(f'DB {database_path} is exists.')

        try:
            connection = sql.connect(database_path)
            logger.debug(f'Connection to DB {database_path} is ok.')

            with connection:
                data = connection.execute("SELECT * FROM users")
                for row in data:
                    print('USERS:', row)
        except:
            logger.error(f'Connection to DB {database_path} failed.')
            return None
    else:
        logger.debug(f'DB {database_path} is NOT exists')

        try:
            connection = sql.connect(database_path)
            logger.debug(f'Inition connect to DB {database_path} is ok.')

            print(os.path.dirname(__file__))
            users_scheme_path = os.path.join(os.path.dirname(__file__), 'schemas', 'create_users_tables.sql')
            with open(users_scheme_path) as f:
                connection.executescript(f.read())

            cursor = connection.cursor()

            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                               ('root', 'root@gmail.ru'))
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                               ('kek', 'kotlapkovskij@gmail.ru'))

            connection.commit()
            # connection.close()
        except:
            logger.error(f'Inition connect to DB {database_path} failed.')
            return None

    return connection



