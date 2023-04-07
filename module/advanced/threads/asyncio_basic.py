import asyncio
import asyncio.events as evt

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(delay=0.6)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

# asyncio.run(main())
# loop: evt.AbstractEventLoop = asyncio.new_event_loop()
loop: evt.AbstractEventLoop = asyncio.get_event_loop()
loop.run_until_complete(main())