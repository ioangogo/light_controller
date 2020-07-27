import asyncio
from contextlib import AsyncExitStack, asynccontextmanager
from random import randrange
from asyncio_mqtt import Client, MqttError
from classes.state import state_class


async def mqtt(state: state_class):
    async with AsyncExitStack as stack:

        tasks = set()

        stack.push_async_callback(cancel_tasks, tasks)

        client = Client(state.mqtt_configuration["hostname"])
        await stack.enter_async_context(client)


async def process_message(messages, template, state: state_class):
    async for message in messages:
        print(message)
        # signal to the light loop that there is a new state for it
        # to act on
        state.new_message_event.set()

        # Wait for the updated state to be processed
        await state.state_processed_event.wait()


async def cancel_tasks(tasks):
    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
