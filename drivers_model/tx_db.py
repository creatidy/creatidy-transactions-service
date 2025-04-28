import mysql.connector
import configparser

TRANSACTIONS_TABLE = 'ib_migr'

class TxDatabase:

    def __init__(self, cfg='./config/config.ini'):
        config = configparser.ConfigParser()
        config.read(cfg)

        user = config['CreatidyDB']['USER']
        password = config['CreatidyDB']['PASSWORD']
        host = config['CreatidyDB']['HOST']
        database = config['CreatidyDB']['DATABASE']
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

    def import_from_db(self) -> list:
        cursor = self.cnx.cursor()
        query = (f"""SELECT {TRANSACTIONS_TABLE}.`symbolId`,
                        {TRANSACTIONS_TABLE}.`orderId`,
                        {TRANSACTIONS_TABLE}.`operationType`,
                        {TRANSACTIONS_TABLE}.`uuid`,
                        {TRANSACTIONS_TABLE}.`orderPos`,
                        {TRANSACTIONS_TABLE}.`accountId`,
                        {TRANSACTIONS_TABLE}.`id`,
                        UNIX_TIMESTAMP({TRANSACTIONS_TABLE}.`when_ts`),
                        {TRANSACTIONS_TABLE}.`asset`,
                        {TRANSACTIONS_TABLE}.`sum_dec`
                    FROM `creatidy`.{TRANSACTIONS_TABLE}
                    ORDER BY {TRANSACTIONS_TABLE}.`when_ts` ASC""")
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        result = []
        for item in data:
            row = {
                'symbolId': item[0],
                'orderId': item[1],
                'operationType': item[2],
                'uuid': item[3],
                'orderPos': item[4],
                'accountId': item[5],
                'id': item[6],
                'when_ts': item[7],
                'asset': item[8],
                'sum_dec': item[9]
            }
            result.append(row)
        return result
