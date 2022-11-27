import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "+", selfbot = True)

account_token = 'Токен вашего аккаунта Discord'
application_id = 1046339126133264475
large_image_id = 1046345753846632599

@bot.event
async def on_ready():
	await bot.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			details = "ваш текст",
			name = "ваш текст",
			assets = {
			  'large_image' : str(large_image_id),
			  'large_text':'ваш текст'
			},
			url = "ваша ссылка на Twitch"
			)
		)
	print('Успешный запуск!')

bot.run(account_token, bot = False)
