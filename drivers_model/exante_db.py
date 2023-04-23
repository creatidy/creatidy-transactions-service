import mysql.connector
import configparser

class ExanteDatabase:

    def __init__(self, cfg='../config/config.ini'):
        config = configparser.ConfigParser()
        config.read(cfg)

        user = config['CreatidyDB']['USER']
        password = config['CreatidyDB']['PASSWORD']
        host = config['CreatidyDB']['HOST']
        database = config['CreatidyDB']['DATABASE']
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

    def import_from_db(self) -> list:
        cursor = self.cnx.cursor()
        query = ("""SELECT `exante`.`symbolId`,
                        `exante`.`orderId`,
                        `exante`.`operationType`,
                        `exante`.`uuid`,
                        `exante`.`orderPos`,
                        `exante`.`accountId`,
                        `exante`.`id`,
                        UNIX_TIMESTAMP(`exante`.`when_ts`),
                        `exante`.`asset`,
                        `exante`.`sum_dec`
                    FROM `creatidy`.`exante`
                    ORDER BY `exante`.`when_ts` ASC""")
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
