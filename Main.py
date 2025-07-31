import discord
from discord.ext import tasks
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()

client = discord.Client(intents=intents)


#code that retrieves the album and posts it to the proper channel in discord@tasks.loop(hours=24)
async def album():
    if datetime.weekday(datetime.today()) != 6 and datetime.weekday(datetime.today()) != 5:
        # connects to the page to hopefully prevent the project from getting paused        print('Getting album')
        url = 'https://1001albumsgenerator.com/onthewalla2'        message_channel = client.get_channel(int(CHANNEL))
        webbrowser.open(url, new=1)
        time.sleep(10)
        keyboard.press_and_release('ctrl+w')
        response = requests.get('https://1001albumsgenerator.com/api/v1/projects/onthewalla2')
        current = json.loads(response.text)['currentAlbum']
        current_artist_name = current['artist']
        current_album_name = current['name']
        spotify_link = 'https://open.spotify.com/album/' + current['spotifyId']
        print(current_artist_name)
        print(current_album_name)
        await message_channel.send(current_artist_name
                                   + '\n'                                   + current_album_name
                                   + '\n'                                   + spotify_link)


#auto starts the album-of-the-day process and reruns it every 24 hours@client.eventasync def on_ready():
    print('Album-of-the-day client running')
    album.start()


client.run(TOKEN)
