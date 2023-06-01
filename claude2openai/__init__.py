import os
import sys
sys.path.append("../..")

from claude2openai.api_resources import ChatCompletion
from claude2openai.version import VERSION

slack_api_token = os.environ.get('SLACK_API_TOKEN')
bot_id = os.environ['BOT_ID']
channel_id = os.environ['CHANNEL_ID']


__version__ = VERSION

