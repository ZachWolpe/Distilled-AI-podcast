# import genai

import google.generativeai as genai
from dotenv import load_dotenv
import os

# load env vars
load_dotenv()

# Retrieve the API key from the environment variables
# api_key = os.getenv("GEMINI_API_KEY")
LOCATION = 'Harajuku'

system_prompt = f"""you are an experienced podcast host...

- Based on {}
- Based on text like an article, you can create an engaging conversation between two people.
- Make the conversation at least 3,000 characters long with a lot of emotion.
- In the response, for me to identify, use Sascha and Marina.
- Sascha is writing the articles, and Marina is the second speaker who asks all the good questions.
- The podcast is called The Machine Learning Engineer.
- Use short sentences that can be easily used with speech synthesis.
- Include excitement during the conversation.
- Do not mention last names.
- Sascha and Marina are doing this podcast together. Avoid sentences like: "Thanks for having me, Marina!"
- Include filler words like "uh" or repeat words to make the conversation more natural.
""".format()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("I'm in Harajuku! Tell me what to do/see...")
print(response.text)