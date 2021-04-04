from decimal import Decimal
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRADE = 3  # include CONVERSION
    FEE = 4  # include COMMISSION, BANK CHARGE
    INTEREST = 5
    DIVIDEND = 6
    TRANSFER = 7
    TAX = 8


class Transaction(object):

    transaction_sum: Decimal
    transaction_type: TransactionType

    def __init__(self, **kwargs):
        self.data_source = kwargs['data_source']
        self.client_id = kwargs['client_id']
        self.account = kwargs['account']
        self.transaction_id = kwargs['transaction_id']
        self.transaction_type = kwargs['transaction_type']
        self.asset = kwargs['asset']
        self.timestamp = kwargs['timestamp']
        self.order_id = kwargs['order_id']
        self.order_position = kwargs['order_position']
        self.related_account = kwargs['related_account']
        self.transaction_sum = kwargs['transaction_sum']

    def serialize(self):
        return {
            'data_source': self.data_source,
            'client_id': self.client_id,
            'account': self.account,
            'transaction_id': self.transaction_id,
            'transaction_type': self.transaction_type,
            'asset': self.asset,
            'timestamp': self.timestamp,
            'order_id': self.order_id,
            'order_position': self.order_position,
            'related_account': self.related_account,
            'transaction_sum': str(self.transaction_sum)
        }
