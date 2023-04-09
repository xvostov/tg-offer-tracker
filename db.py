import pymysql

from typing import List
from settings import db_host, db_port, db_user, db_password, db_name
from loguru import logger


class DataBaseHandler:
    def __init__(self):
        logger.debug('Сonnecting to a remote database')
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        # Проверка и создание отсутствующих таблицы
        logger.debug('Checking the om "viewed_links" table')
        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS viewed_links (
        url	VARCHAR(200) NOT NULL UNIQUE)""")

        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
        name VARCHAR(50),
        value VARCHAR(30) NOT NULL,
        PRIMARY KEY(name))""")

        logger.debug('Checking the om "stopwords" table')
        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS stopwords (
        word VARCHAR(200) NOT NULL)""")

        # self.mysql_cursor.execute("""
        # CREATE TABLE IF NOT EXISTS watchlist (
        # url	VARCHAR(200) NOT NULL UNIQUE,
        # price NUMERIC)""")

        logger.debug('Checking the om "categories" table')
        mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_1 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "categories" table')
        mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_2 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "categories" table')
        mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS сategories_avito_3 (
        url	VARCHAR(255) NOT NULL UNIQUE)""")

        logger.debug('Checking the om "users" table')
        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        chat_id	VARCHAR(50) NOT NULL,
        PRIMARY KEY(chat_id))""")

        logger.debug('Checking the om "blacklist" table')
        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS blacklist (
        seller_id	VARCHAR(200) NOT NULL,
        PRIMARY KEY(seller_id))""")

        logger.debug('Checking the om "stopwords_lalafo" table')
        mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS stopwords_lalafo (
        word VARCHAR(200) NOT NULL)""")

        logger.debug('Checking the om "min_prices" table')
        mysql_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS min_prices (
        url	VARCHAR(255) NOT NULL UNIQUE,
        min_price INT,
        PRIMARY KEY(url))""")

        logger.debug('Initialization of settings')
        try:
            mysql_cursor.execute("INSERT INTO settings (name, value) VALUES ('delay', '1')")
            mysql_cursor.execute("INSERT INTO settings (name, value) VALUES ('interval', '600')")

        except pymysql.err.IntegrityError:
            pass

        logger.info('DataBaseHandler - ready!')


    def _get_connection_and_cursor(self):
        logger.debug('Сonnecting to a remote database')
        mysql_connection = pymysql.connect(host=db_host,
                                           port=db_port,
                                           user=db_user,
                                           password=db_password,
                                           database=db_name,
                                           charset='utf8mb4')
        mysql_cursor = mysql_connection.cursor()
        mysql_connection.autocommit(True)

        return mysql_connection, mysql_cursor

    def get_viewed_links(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting viewed links')
        mysql_cursor.execute("SELECT url FROM viewed_links")
        resp = mysql_cursor.fetchall()
        logger.debug('Viewed links received')
        return [d[0] for d in resp]

    def add_to_viewed_links(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to viewed links - {url}')
        mysql_cursor.execute("INSERT INTO viewed_links VALUES(%s)", (url,))

        logger.debug('The url has been added to viewed links')

    def update_delay(self, delay):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Updating the delay')
        try:
            float(delay)
        except ValueError:
            raise ValueError

        else:
            delay = str(delay)

        mysql_cursor.execute('UPDATE settings SET value = ? WHERE name = "delay"', (delay,))

        logger.debug('The delay has been updated')

    def get_categories_from_avito_1(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM сategories_avito_1")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def get_categories_from_avito_2(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM сategories_avito_2")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def get_categories_from_avito_3(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM сategories_avito_3")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def add_category_to_avito_1(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO сategories_avito_1 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            logger.debug('The url has been added to categories')

    def add_category_to_avito_2(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO сategories_avito_2 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            logger.debug('The url has been added to categories')

    def add_category_to_avito_3(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO сategories_avito_3 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:

            logger.debug('The url has been added to categories')

    def remove_category_from_avito_1(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM сategories_avito_1 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def remove_category_from_avito_2(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM сategories_avito_2 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def remove_category_from_avito_3(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM сategories_avito_3 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def add_to_blacklist(self, seller_id: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        print(seller_id)
        logger.debug(f'Adding to blacklist - {seller_id}')
        try:
            mysql_cursor.execute("INSERT INTO blacklist VALUES(%s)", (seller_id,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        logger.debug('The seller_id has been added to blacklist')

    def remove_from_blacklist(self, seller_id: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from blacklist - {seller_id}')
        mysql_cursor.execute("DELETE FROM blacklist WHERE seller_id = %s", (seller_id,))
        logger.debug('The seller_id has been deleted from blacklist')

    def get_blacklist(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting blacklist')
        mysql_cursor.execute("SELECT seller_id FROM blacklist")
        resp = mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_stopword(self, word: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()
        logger.debug(f'Adding to stopwords - {word}')

        try:
            mysql_cursor.execute("INSERT INTO stopwords VALUES(%s)", (word,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        logger.debug('The word has been added to stopwords')

    def remove_stopword(self, word: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from stopwords - {word}')
        mysql_cursor.execute("DELETE FROM stopwords WHERE word = %s", (word,))

        logger.debug('The word has been deleted from stopwords')

    def get_stopwords(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting stopwords')
        mysql_cursor.execute("SELECT word FROM stopwords")
        resp = mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_user(self, chat_id: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding user - {chat_id}')
        try:
            mysql_cursor.execute("INSERT INTO users VALUES(%s)", (chat_id,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        logger.debug('The user has been added')

    def remove_user(self, chat_id: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()
        logger.debug(f'Deleting user - {chat_id}')
        mysql_cursor.execute("DELETE FROM users WHERE chat_id = %s", (chat_id,))

        logger.debug('The user has been deleted')

    def get_users(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting users')
        mysql_cursor.execute("SELECT chat_id FROM users")
        resp = mysql_cursor.fetchall()
        return [d[0] for d in resp]

    def add_category_to_watch(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO watch_cat_1 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            logger.debug('The url has been added to categories')

    def remove_category_from_watch(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM watch_cat_1 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def get_categories_from_watch(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM watch_cat_1")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    # =============================

    def add_category_to_lalafo(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO lalafo_cat_1 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:

            logger.debug('The url has been added to categories')

    def remove_category_from_lalafo(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM lalafo_cat_1 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def get_categories_from_lalafo(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM lalafo_cat_1")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def add_stopword_lalafo(self, word: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to stopwords - {word}')

        try:
            mysql_cursor.execute("INSERT INTO stopwords_lalafo VALUES(%s)", (word,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')
        else:
            logger.debug('The word has been added to stopwords')

    def remove_stopword_lalafo(self, word: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from stopwords - {word}')
        mysql_cursor.execute("DELETE FROM stopwords_lalafo WHERE word = %s", (word,))

        logger.debug('The word has been deleted from stopwords')

    def get_stopwords_lalafo(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting stopwords')
        mysql_cursor.execute("SELECT word FROM stopwords_lalafo")
        resp = mysql_cursor.fetchall()
        return [d[0] for d in resp]

    # ==================

    def add_category_to_youla(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO сategories_youla_1 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:

            logger.debug('The url has been added to categories')

    def remove_category_from_youla(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM сategories_youla_1 WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def get_categories_from_youla(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM сategories_youla_1")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    def add_category_to_watch2(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()
        logger.debug(f'Adding to categories - {url}')
        try:
            mysql_cursor.execute(f"INSERT INTO watch_cat_2 VALUES(%s)", (url,))
        except pymysql.err.IntegrityError:
            logger.error('Failed to add to the database')

        else:
            logger.debug('The url has been added to categories')

    def remove_category_from_watch2(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting from categories - {url}')
        mysql_cursor.execute(f"DELETE FROM watch_cat_2 WHERE url = %s", (url,))
        logger.debug('The record was deleted from the database')

    def get_categories_from_watch2(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting categories')
        mysql_cursor.execute(f"SELECT url FROM watch_cat_2")
        resp = mysql_cursor.fetchall()
        logger.debug('Categories received')
        return [d for d in resp]

    # =============================

    def add_min_price_for_category(self, url: str, min_price: int):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()
        logger.debug(f'Adding min price ({min_price}) for {url}')
        while True:
            try:
                mysql_cursor.execute("INSERT INTO min_prices(url, min_price) VALUES(%s, %s)", (url, min_price))
                mysql_connection.commit()
            except pymysql.err.OperationalError:
                mysql_connection.ping(True)

            except pymysql.err.IntegrityError:
                break
            else:
                break
        logger.debug('The min price has been added for category')

    def remove_min_price_for_category(self, url: str):
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug(f'Deleting min price for category {url}')

        mysql_cursor.execute(f"DELETE FROM min_prices WHERE url = %s", (url,))

        logger.debug('The record was deleted from the database')

    def get_min_prices(self) -> List:
        mysql_connection, mysql_cursor = self._get_connection_and_cursor()

        logger.debug('Getting min prices')
        mysql_cursor.execute("SELECT url, min_price FROM min_prices")
        resp = mysql_cursor.fetchall()
        return [d for d in resp]
