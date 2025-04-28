from drivers_model.tx_db import TxDatabase
from decimal import Decimal
from dto.transaction import Transaction, TransactionType


class Exante:

    def __init__(self):
        pass

    def import_from_external_source(self) -> list:
        db = TxDatabase()
        transactions = db.import_from_db()
        result = []
        for item in transactions:
            operation_type = item['operationType']
            transaction_sum = item['sum_dec']
            split = None
            if operation_type == 'TRADE':
                transaction_type = TransactionType.TRADE
            elif operation_type == 'AUTOCONVERSION' and transaction_sum > 0:
                transaction_type = TransactionType.DEPOSIT
            elif operation_type == 'AUTOCONVERSION' and transaction_sum < 0:
                transaction_type = TransactionType.WITHDRAWAL
            elif operation_type == 'BANK CHARGE':
                transaction_type = TransactionType.FEE
            elif operation_type == 'COMMISSION':
                transaction_type = TransactionType.COMMISSION
            elif operation_type == 'DIVIDEND':
                transaction_type = TransactionType.DIVIDEND
            elif operation_type == 'FUNDING/WITHDRAWAL' and transaction_sum > 0:
                transaction_type = TransactionType.DEPOSIT
            elif operation_type == 'FUNDING/WITHDRAWAL' and transaction_sum < 0:
                transaction_type = TransactionType.WITHDRAWAL
            elif operation_type == 'INTEREST':
                transaction_type = TransactionType.FEE
            elif operation_type == 'SUBACCOUNT TRANSFER':
                transaction_type = TransactionType.TRANSFER
            elif operation_type == 'TAX':
                transaction_type = TransactionType.TAX
            elif str(operation_type).startswith('STOCK SPLIT'):
                transaction_type = TransactionType.STOCK_SPLIT
                split = str(operation_type).split(' ')[-1]
            else:
                raise Exception(f"Unknown transaction type {operation_type}")

            kwargs = {
                'data_source': 'ExanteDB',
                'client_id': 'local',
                'account': item['accountId'],
                'transaction_id': item['id'],
                'related_asset': item['symbolId'],
                'transaction_type': transaction_type.name,
                'asset': item['asset'],
                'timestamp': item['when_ts'],
                'order_id': item['orderId'],
                'order_position': item['orderPos'],
                'related_account': '',
                'transaction_sum': Decimal(transaction_sum),
                'split': split
            }
            transaction = Transaction(**kwargs)
            result.append(transaction)
        return result
