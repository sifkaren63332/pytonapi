"""Get account transactions."""
from pytonapi import AsyncTonapi
from pytonapi.utils import to_amount

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa


async def main() -> None:
    tonapi = AsyncTonapi(api_key=API_KEY)
    result = await tonapi.blockchain.get_account_transactions(account_id=ACCOUNT_ID, limit=1000)

    for transaction in result.transactions:
        print(f"Value nanoton: {transaction.in_msg.value}")
        # output: 1000000000

        print(f"Value TON: {to_amount(transaction.in_msg.value)}")
        # output: 1.0

        if transaction.in_msg.decoded_op_name == "text_comment":
            print(f"Comment: {transaction.in_msg.decoded_body['text']}")
            # output: Hello, World!


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
