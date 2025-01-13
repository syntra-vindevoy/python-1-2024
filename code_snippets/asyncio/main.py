import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}")

async def main():
    # Schedule multiple coroutines to run concurrently
    await asyncio.gather(
        # laat alles tegelijk beginnen, 
        # maar wacht tot alles klaar is
        say_hello("Charlie", 3),
        say_hello("Alice", 3),
        say_hello("Bob", 4)
    )
    print("All done!")


    '''
    don't wait for any, just run all
    task1 = asyncio.create_task(say_hello("Charlie", 3))
    task2 = asyncio.create_task(say_hello("Alice", 3))
    task3 = asyncio.create_task(say_hello("Bob", 4))
    print('all tasks started')
    await asyncio.gather(task1, task2, task3)
    '''


asyncio.run(main())