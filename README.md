# Discord-Album-of-the-day-bot
 A bot that posts an album of the day based on the 1001 albums you need to listen to before you die site. 

To use you will need a .env file to store your Discord_Guild name, Guild_ID, Discord_Token, and Channel_ID. You will also need to create a profile on the Discord developer site so that the bot is able to connect to Discord. 

Required libraries:
 discord
 discord.ext
 requests
 json
 os
 time
 datetime
 webbrowser
 keyboard
 dotenv


The code to open the browser is required because the site auto pauses the album generation if you have not visited the site in 4 days. If someone sees this repo and has a better solution than literally opening a page, please let me know!
