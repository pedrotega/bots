import discord
import asyncio
import util

TOKEN = 'YOUR_BOT_TOKEN'

def run_discord_bot():
    # Create an instance of the spam_bot
    spam_bot = discord.Client(intents=discord.Intents.default())

    # Event triggered when the spam_bot has connected to Discord
    @spam_bot.event
    async def on_ready():
        print(f'spam_bot connected as {spam_bot.user.name}')

        # Start sending a message every week
        while True:
            channel = spam_bot.get_channel(YOUR_CHANNEL_ID)  
            
            # Call to make the photo of the webpage that is going to be spam
            util.make_photo()

            # Read and send the photo to the channel
            with open(util.IM_NAME, 'rb') as f:
                img = discord.File(f)

                await channel.send(file=img)

            # Send the webpage link to the channel
            await channel.send('https://www.eneba.com/es/collection/juegos-en-oferta')

            week_secs = 7*24*60*60
            await asyncio.sleep(week_secs)  # Wait for a week

    # Run the spam_bot
    spam_bot.run(TOKEN)

