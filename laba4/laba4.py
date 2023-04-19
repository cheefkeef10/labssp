import os
import aiohttp
import asyncio


from bs4 import BeautifulSoup


def save_text_to_file(filename, text):
    with open(filename, 'w', encoding="utf-8") as file_object:
         file_object.write(text)

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="http://biik.ru/raspcg109.htm")as response:
            soup = BeautifulSoup(await response.read(), "lxml")
            elems = soup.find("table", {"class": "inf"})
            trs_list = elems.find_all("tr")[3☺
            res_data = []
            for (inx, i) in enumerate(trs_list, 0):
                for i in i.find_all("td"):
                    if i.get("class") != "nul":
                        res_data.append(i.text)

            save_text_to_file("XD.txt", "\n".join([i for i in res_data]))


if __name__ == "__main__":
    os.system("cls")
    asyncio.run(main())
