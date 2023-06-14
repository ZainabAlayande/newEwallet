from data.model.transaction import Transaction
from data.model.transaction_type import TransactionType
from data.repository.transaction_repository import TransactionRepository


class TransactionRepositoryImpl(TransactionRepository):

    def __init__(self):
        self.__transactions: list[Transaction] = []
        self.__counter = 0

    def save(self, transaction: Transaction) -> Transaction:
        if transaction.get_id() == 0:
            transaction.set_id(self.generate_transaction_id())

        if transaction.get_transaction_type() == TransactionType.DEBIT:
            transaction.set_transfer_type(TransactionType.CREDIT)

        self.__transactions.append(transaction)
        self.__counter += 1
        return transaction

    def generate_transaction_id(self) -> int:
        return self.__counter + 1

    def count(self) -> int:
        return self.__counter

    def find_transaction_by_id(self, identity_number: int):
        transaction_list: list[Transaction] = []
        for transaction in self.__transactions:
            if transaction.get_id() == identity_number:
                return transaction

    def delete_transaction_by_id(self, identity_number: int):
        for transaction in self.__transactions:
            if transaction.get_id == identity_number:
                self.__transactions.remove(transaction)
            self.__counter -= 1
            break

    def view_all_transactions(self) -> list[Transaction]:
        return self.__transactions

    def find_all_credit_transaction(self, credit_type: TransactionType):
        pass

    def find_all_debit_transaction(self, debit_type: TransactionType):
        pass