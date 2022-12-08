import os
import pymysql

from typing import List
from settings import db_host, db_port,db_user, db_password, db_name
from loguru import logger


class DataBaseHandler:
    def __init__(self):
        logger.debug('Сonnecting to a remote database')
        self.mysql_connection = pymysql.connect(host=db_host,
                                                port=db_port,
                                                user=db_user,
                                                password=db_password,
                                                database=db_name,
                                                charset='utf8mb4',
                                                autocommit=True)

        self.mysql_connection.autocommit(True)
        self.mysql_cursor = self.mysql_connection.cursor()

        # Проверка и создание отсутствующих таблицы
        logger.debug('Checking the om "viewed_links" table')
        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS viewed_links (
        url	VARCHAR(200) NOT NULL UNIQUE)""")



        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
        name VARCHAR(50),
        value VARCHAR(30) NOT NULL,
        PRIMARY KEY(name))""")

        logger.debug('Checking the om "stopwords" table')
        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS stopwords (
        word VARCHAR(200) NOT NULL)""")

        # self.mysql_cursor.execute("""
        # CREATE TABLE IF NOT EXISTS watchlist (
        # url	VARCHAR(200) NOT NULL UNIQUE,
        # price NUMERIC)""")


        logger.debug('Checking the om "categories" table')
        self.mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_1 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "categories" table')
        self.mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_2 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "categories" table')
        self.mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_3 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "users" table')
        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        chat_id	VARCHAR(50) NOT NULL,
        PRIMARY KEY(chat_id))""")

        logger.debug('Checking the om "blacklist" table')
        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS blacklist (
        seller_id	VARCHAR(200) NOT NULL,
        PRIMARY KEY(seller_id))""")


        logger.debug('Checking the om "stopwords_lalafo" table')
        self.mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS stopwords_lalafo (
        word VARCHAR(200) NOT NULL)""")


        logger.debug('Initialization of settings')
        try:
            self.mysql_cursor.execute("INSERT INTO settings (name, value) VALUES ('delay', '1')")
            self.mysql_cursor.execute("INSERT INTO settings (name, value) VALUES ('interval', '600')")
            self.mysql_connection.commit()

        except pymysql.err.IntegrityError:
            pass

        logger.info('DataBaseHandler - ready!')



    def get_viewed_links(self) -> List:
        self.mysql_connection.ping(reconnect=True)
        logger.debug('Getting viewed links')
        self.mysql_cursor.execute("SELECT url FROM viewed_links")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Viewed links received')
        return [d[0] for d in resp]

    def add_to_viewed_links(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to viewed links - {url}')
        self.mysql_cursor.execute("INSERT INTO viewed_links VALUES(%s)", (url,))
        self.mysql_connection.commit()
        logger.debug('The url has been added to viewed links')

    def update_delay(self, delay):
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Updating the delay')
        try:
            float(delay)
        except ValueError:
            raise ValueError

        else:
            delay = str(delay)

        self.mysql_cursor.execute('UPDATE settings SET value = ? WHERE name = "delay"', (delay, ))
        self.mysql_connection.commit()
        logger.debug('The delay has been updated')

    def get_categories_from_avito_1(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM сategories_avito_1")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def get_categories_from_avito_2(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM сategories_avito_2")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def get_categories_from_avito_3(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM сategories_avito_3")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def add_category_to_avito_1(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO сategories_avito_1 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def add_category_to_avito_2(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO сategories_avito_2 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def add_category_to_avito_3(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO сategories_avito_3 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def remove_category_from_avito_1(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM сategories_avito_1 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def remove_category_from_avito_2(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM сategories_avito_2 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def remove_category_from_avito_3(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM сategories_avito_3 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def add_to_blacklist(self, seller_id: str):
        self.mysql_connection.ping(reconnect=True)

        print(seller_id)
        logger.debug(f'Adding to blacklist - {seller_id}')
        try:
            self.mysql_cursor.execute("INSERT INTO blacklist VALUES(%s)", (seller_id, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')
        else:
            self.mysql_connection.commit()
        logger.debug('The seller_id has been added to blacklist')

    def remove_from_blacklist(self, seller_id: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from blacklist - {seller_id}')
        self.mysql_cursor.execute("DELETE FROM blacklist WHERE seller_id = %s", (seller_id, ))
        self.mysql_connection.commit()
        logger.debug('The seller_id has been deleted from blacklist')

    def get_blacklist(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting blacklist')
        self.mysql_cursor.execute("SELECT seller_id FROM blacklist")
        resp = self.mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_stopword(self, word: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to stopwords - {word}')

        try:
            self.mysql_cursor.execute("INSERT INTO stopwords VALUES(%s)", (word, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')
        else:
            self.mysql_connection.commit()
        logger.debug('The word has been added to stopwords')

    def remove_stopword(self, word: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from stopwords - {word}')
        self.mysql_cursor.execute("DELETE FROM stopwords WHERE word = %s", (word, ))
        self.mysql_connection.commit()
        logger.debug('The word has been deleted from stopwords')

    def get_stopwords(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting stopwords')
        self.mysql_cursor.execute("SELECT word FROM stopwords")
        resp = self.mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_user(self, chat_id: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding user - {chat_id}')
        try:
            self.mysql_cursor.execute("INSERT INTO users VALUES(%s)", (chat_id,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')
        else:
            self.mysql_connection.commit()
        logger.debug('The user has been added')

    def remove_user(self, chat_id: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting user - {chat_id}')
        self.mysql_cursor.execute("DELETE FROM users WHERE chat_id == %s", (chat_id,))
        self.mysql_connection.commit()
        logger.debug('The user has been deleted')

    def get_users(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting users')
        self.mysql_cursor.execute("SELECT chat_id FROM users")
        resp = self.mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_category_to_watch(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO watch_cat_1 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def remove_category_from_watch(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM watch_cat_1 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def get_categories_from_watch(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM watch_cat_1")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    # =============================

    def add_category_to_lalafo(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO lalafo_cat_1 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def remove_category_from_lalafo(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM lalafo_cat_1 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def get_categories_from_lalafo(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM lalafo_cat_1")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def add_stopword_lalafo(self, word: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to stopwords - {word}')

        try:
            self.mysql_cursor.execute("INSERT INTO stopwords_lalafo VALUES(%s)", (word, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')
        else:
            self.mysql_connection.commit()
        logger.debug('The word has been added to stopwords')

    def remove_stopword_lalafo(self, word: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from stopwords - {word}')
        self.mysql_cursor.execute("DELETE FROM stopwords_lalafo WHERE word = %s", (word, ))
        self.mysql_connection.commit()
        logger.debug('The word has been deleted from stopwords')

    def get_stopwords_lalafo(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting stopwords')
        self.mysql_cursor.execute("SELECT word FROM stopwords_lalafo")
        resp = self.mysql_cursor.fetchall()
        return [d[0] for d in resp]

    # ==================

    def add_category_to_youla(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Adding to categories - {url}')
        try:
            self.mysql_cursor.execute(f"INSERT INTO сategories_youla_1 VALUES(%s)", (url, ))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            self.mysql_connection.commit()
            logger.debug('The url has been added to categories')

    def remove_category_from_youla(self, url: str):
        self.mysql_connection.ping(reconnect=True)

        logger.debug(f'Deleting from categories - {url}')
        self.mysql_cursor.execute(f"DELETE FROM сategories_youla_1 WHERE url = %s", (url, ))
        self.mysql_connection.commit()
        logger.debug('The record was deleted from the database')

    def get_categories_from_youla(self) -> List:
        self.mysql_connection.ping(reconnect=True)

        logger.debug('Getting categories')
        self.mysql_cursor.execute(f"SELECT url FROM сategories_youla_1")
        resp = self.mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]