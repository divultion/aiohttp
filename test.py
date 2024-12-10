import aiohttp
import asyncio
import pathlib

async def main():
  async with aiohttp.ClientSession() as session:
    file_path = pathlib.Path(__file__).parent / "aiohttp.png"

    async with session.post("https://jsonplaceholder.typicode.com/posts", cookies={"dilbo": "123"}, json={
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
  }) as response:
      response.raise_for_status()
      print(await response.text())

if __name__ == "__main__":
  asyncio.run(main())