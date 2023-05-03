from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.blockchain import Block, Transactions, Transaction


class BlockchainMethod(TonapiClient):

    def get_block_data(self, block_id: str) -> Block:
        """
        Get block data.

        :param block_id: block ID (string), example: "(-1,8000000000000000,4234234)"
        :return: :class:`Block`
        """
        method = f"v2/blockchain/blocks/{block_id}"
        response = self._request(method=method)

        return Block(**response)

    def get_transaction_from_block(self, block_id: str) -> Transactions:
        """
        Get transactions from block.

        :param block_id: block ID (string), example: "(-1,8000000000000000,4234234)"
        :return: :class:`Block`
        """
        method = f"v2/blockchain/blocks/{block_id}/transactions"
        response = self._request(method=method)

        return Transactions(**response)

    def get_transaction_data(self, transaction_id: str) -> Transaction:
        """
        Get transaction data.

        :param transaction_id: Transaction_id ID (string),
         example: "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
        :return: :class:`Transaction`
        """
        method = f"v2/blockchain/transactions/{transaction_id}"
        response = self._request(method=method)

        return Transaction(**response)

    def get_account_transactions(self, account_id: str, after_lt: int = None,
                                 before_lt: int = 0, limit: int = 100) -> Transactions:
        """
        Get account transactions.

        :param account_id: account ID
        :param after_lt: omit this parameter to get last transactions
        :param before_lt: omit this parameter to get last transactions
        :param limit: Default value : 100
        :return: :class:`Transactions`
        """
        method = f"v2/blockchain/accounts/{account_id}/transactions"
        params = {'before_lt': before_lt, 'limit': limit}
        if after_lt: params['after_lt'] = after_lt  # noqa E701
        response = self._request(method=method, params=params)

        return Transactions(**response)
