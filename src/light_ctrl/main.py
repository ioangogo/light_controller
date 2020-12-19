import asyncio
from contextlib import AsyncExitStack, asynccontextmanager
from network import mqtt
from classes.state import state_class
from light_loop import light_loop
from asyncio_mqtt import MqttError
import src.light_ctrl.loader


async def cancel_tasks(tasks):
    # * This is borrowed from the example code of the mqtt libary
    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


async def async_main(state: state_class):
    numAttempts = 3
    while numAttempts > 0:
        try:
            async with AsyncExitStack as mainStack:
                mainTasks = set()
                mainStack.push_async_callback(cancel_tasks, mainTasks)

                mainTasks.add(asyncio.create_task(mqtt(state)))
                mainTasks.add(asyncio.create_task(light_loop(state)))

                await asyncio.gather(*mainTasks)
        except MqttError as error:
            print(f'Error "{error}". Reconnecting. Attempts Remaining {numAttempts}')
        finally:
            await asyncio.sleep(3)

def main():
    state = state_class()
