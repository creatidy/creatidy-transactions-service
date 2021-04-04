from drivers_model.exante_db import ExanteDatabase
from decimal import Decimal
from dto.transaction import Transaction, TransactionType


class Exante:

    def __init__(self):
        pass

    def import_from_external_source(self) -> list:
        db = ExanteDatabase()
        transactions = db.import_from_db()
        result = []
        for item in transactions:
            transaction_type = item['operationType']
            transaction_sum = item['sum_dec']
            if transaction_type == 'TRADE':
                transaction_type = TransactionType.TRADE
            elif transaction_type == 'AUTOCONVERSION':
                transaction_type = TransactionType.TRADE
            elif transaction_type == 'BANK CHARGE':
                transaction_type = TransactionType.FEE
            elif transaction_type == 'COMMISSION':
                transaction_type = TransactionType.FEE
            elif transaction_type == 'DIVIDEND':
                transaction_type = TransactionType.DIVIDEND
            elif transaction_type == 'FUNDING/WITHDRAWAL' and transaction_sum > 0:
                transaction_type = TransactionType.DEPOSIT
            elif transaction_type == 'FUNDING/WITHDRAWAL' and transaction_sum < 0:
                transaction_type = TransactionType.WITHDRAWAL
            elif transaction_type == 'INTEREST':
                transaction_type = TransactionType.INTEREST
            elif transaction_type == 'SUBACCOUNT TRANSFER':
                transaction_type = TransactionType.TRANSFER
            elif transaction_type == 'TAX':
                transaction_type = TransactionType.TAX
            else:
                raise Exception(f"Unknown transaction type {transaction_type}")

            kwargs = {
                'data_source': 'ExanteDB',
                'client_id': 'local',
                'account': item['accountId'],
                'transaction_id': item['id'],
                'transaction_type': str(transaction_type),
                'asset': item['asset'],
                'timestamp': item['when_ts'],
                'order_id': item['orderId'],
                'order_position': item['orderPos'],
                'related_account': '',
                'transaction_sum': Decimal(transaction_sum)
            }
            transaction = Transaction(**kwargs)
            result.append(transaction)
        return result
