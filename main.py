import discord
import random
import asyncio
import os

TOKEN = 'ваш токен'

sound_files = [
    'sound1.mp3',
    'sound2.mp3',
    'sound3.mp3',
    'sound4.mp3',
    'sound5.mp3',
    'sound6.mp3',
    'sound7.mp3',
    'sound8.mp3',
    'sound9.mp3',
    'sound10.mp3',
    'sound11.mp3',
    'sound12.mp3',
    'sound13.mp3',
    'sound14.mp3',
    'sound15.mp3',
    'sound16.mp3',
    'sound17.mp3',
    'sound18.mp3',
    'sound19.mp3',
    'sound20.mp3',
]

intents = discord.Intents.default()
intents.voice_states = True

client = discord.AutoShardedClient(intents=intents)


@client.event
async def on_ready():
    print(f'Бот успешно подключился как {client.user.name}')
    await play_random_sound()  # Запускаем функцию воспроизведения случайного звука после подключения бота


async def play_random_sound():
    while True:
        # Выбираем случайный голосовой канал с активными пользователями
        voice_channel = None
        for guild in client.guilds:
            voice_channels = [vc for vc in guild.voice_channels if len(vc.members) > 0]
            if voice_channels:
                voice_channel = random.choice(voice_channels)
                break

        if voice_channel:
            # Выбираем случайный звуковой файл
            sound_file = random.choice(sound_files)

            # Присоединяемся к голосовому каналу
            voice_client = await voice_channel.connect()

            # Воспроизводим звуковой файл
            voice_client.play(discord.FFmpegPCMAudio(sound_file))

            # Ждем, пока звуковой файл полностью воспроизведется
            while voice_client.is_playing():
                await asyncio.sleep(1)

            # Отключаемся от голосового канала
            await voice_client.disconnect()

        # Задержка в 5 минут перед следующим вызовом функции
        await asyncio.sleep(600)


client.run(TOKEN)
