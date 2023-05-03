from pytonapi.async_tonapi.client import AsyncTonapiClient

from pytonapi.schema.nft import NftCollections, NftCollection, NftItems, NftItem


class NftMethod(AsyncTonapiClient):

    async def get_collections(self, limit: int = 15, offset: int = 0) -> NftCollections:
        """
        Get NFT collections.

        :param limit: Default value : 15
        :param offset: Default value : 0
        :return: :class:`NftCollections`
        """
        method = "v2/nfts/collections"
        params = {'limit': limit, 'offset': offset}
        response = await self._request(method=method, params=params)

        return NftCollections(**response)

    async def get_collection_by_collection_address(self, account_id: str) -> NftCollection:
        """
        Get NFT collection by collection address.

        :param account_id: Account ID
        :return: :class:`NftCollection`
        """
        method = f"v2/nfts/collections/{account_id}"
        response = await self._request(method=method)

        return NftCollection(**response)

    async def get_items_by_collection_address(self, account_id: str, limit: int = 1000,
                                              offset: int = 0) -> NftItems:
        """
        Get NFT items from collection by collection address.

        :param account_id: Account ID
        :param limit: Default value : 1000
        :param offset: Default value : 0
        :return: :class:`NftItems`
        """
        method = f"v2/nfts/collections/{account_id}/items"
        params = {'limit': limit, 'offset': offset}
        response = await self._request(method=method, params=params)

        return NftItems(**response)

    async def get_all_items_by_collection_address(self, account_id: str) -> NftItems:
        """
        Get all NFT items from collection by collection address.

        :param account_id: Account ID
        :return: :class:NftItems
        """
        nft_items = []
        offset, limit = 0, 1000

        while True:
            result = await self.get_items_by_collection_address(
                account_id=account_id, limit=limit, offset=offset,
            )
            nft_items += result.nft_items
            offset += limit

            if len(result.nft_items) != limit:
                break

        return NftItems(nft_items=nft_items)

    async def get_item_by_address(self, account_id: str) -> NftItem:
        """
        Get NFT item by its address.

        :param account_id: account ID
        :return: :class:`NftItem`
        """
        method = f"v2/nfts/{account_id}"
        response = await self._request(method=method)

        return NftItem(**response)
