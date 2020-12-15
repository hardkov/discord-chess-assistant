import discord 
import berserk
import modules.detection as detection
import modules.settings as settings
import modules.lichess as lichess
import modules.settings as settings

# install data
settings.install_data("./nltk_data")
#####

# load setting
settings.config_filename = "settings/config.json"
config = settings.load_config()
DISCORD_TOKEN = config['DISCORD_TOKEN']
LICHESS_TOKEN = config['LICHESS_TOKEN']
intents_filename = config['intentsFilename']
#####

# configuring lichess module
session = berserk.TokenSession(LICHESS_TOKEN)
lichess.client = berserk.Client(session=session)
#####

# configuring detection module
detection.load_intents(intents_filename)
detection.extend_keywords()
detection.build_regex_dict()
#####

client = discord.Client()
currently_processed_intent = None

@client.event
async def on_message(message):
    global currently_processed_intent

    message.content = message.content.lower()
    
    if not message.author == client.user:
        intent_name = ""

        if currently_processed_intent:
            intent_name = currently_processed_intent
        else:
            intent_name = detection.match_intent(message.content)[0]
            currently_processed_intent = intent_name

        intent_handler = detection.get_intent_handler(intent_name)
        result = intent_handler(message)

        if result['finished_talking']:
            currently_processed_intent = None
        
        if result["message"]:
            await message.channel.send(result["message"])

@client.event
async def on_ready():
    print("bot is ready")

client.run(DISCORD_TOKEN)
