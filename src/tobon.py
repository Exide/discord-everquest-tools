import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {} ({})'.format(client.user.name, client.user.id))
    # channel = client.get_channel('545382243309191232')
    # message = 'It is good to see the young show an interest in the ways of magic. Its circles can be used in tandem with our unique ways of tinkering.'
    # print('sending message to {}: {}'.format(channel, message))
    # await client.send_message(channel, message)

@client.event
async def on_message(message):
    print('message received from {}: {}'.format(message.channel, message.content))
    if client.user.mentioned_in(message):
        await client.add_reaction(message, u"\U0001F636")

def get_client():
    return client

async def start():
    yield client.start('NTQ2Mjc1MzUxMjc0MzIzOTY4.D0l7OA.8609bjmEWLIEFX49C0Klbe3SjS4')

async def stop():
    yield client.logout()
