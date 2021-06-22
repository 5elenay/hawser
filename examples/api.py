# Simple API example.
import hawser
import asyncio

async def main():
    # Fetch an User with ID.
    result = await hawser.fetch_user(793467584820281346)
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())