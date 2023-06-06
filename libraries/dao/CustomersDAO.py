


from libraries.utilities.dbUtility import DBUtility
import random
import logging as logger

class CustomersDAO:

    def __init__(self):
        self.db_helper = DBUtility()
        self.database = self.db_helper.database
        self.table_prefix = self.db_helper.table_prefix

    def get_customer_by_email(self, email):
        sql = f"""SELECT * FROM {self.database}.{self.table_prefix}users 
                  WHERE user_email = '{email}';"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = f"SELECT user_email FROM {self.database}.{self.table_prefix}users order by id desc LIMIT 1000;"
        rs_sql = self.db_helper.execute_select(sql)
        logger.info(f"Found {len(rs_sql)} random users from db.")
        return random.sample(rs_sql, int(qty))