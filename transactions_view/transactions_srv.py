import grpc
from concurrent import futures
import time

# import the generated classes
import protobufs.transactions_pb2
import protobufs.transactions_pb2_grpc

# import the original calculator.py
from import_controller.exante_controller import Exante
from dto.transaction import Transaction

class TransactionsServicer(protobufs.transactions_pb2_grpc.TransactionsServicer):

    def GetList(self, request, context):
        account = Exante()
        transactions = account.import_from_external_source()
        response = protobufs.transactions_pb2.TransactionsList()
        t: Transaction
        for t in transactions:
            transaction = protobufs.transactions_pb2.Transaction()
            for key in t.fields():
                transaction.__setattr__(key, str(t.__getattribute__(key)))
            response.transaction.append(transaction)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
protobufs.transactions_pb2_grpc.add_TransactionsServicer_to_server(
        TransactionsServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
