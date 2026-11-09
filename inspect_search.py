import asyncio
import json
from urllib.parse import quote

from chizhik_api import ChizhikAPI


async def main():
    async with ChizhikAPI(proxy=None, headless=False) as api:
        response = await api.Catalog.delivery_search(
            store_id="HBBN",
            query=quote("Апельсины", safe=""),
            limit=12,
            mode="delivery",
            include_restrict=True,
        )

        data = response.json()

        with open("search-response.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print("Ответ сохранён в search-response.json")


asyncio.run(main())
