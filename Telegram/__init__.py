import json
import os

secrets = os.environ if os.environ.get('is_production') else json.load(open(os.path.join("secrets")))

api_key = secrets["bot_api_key"]
