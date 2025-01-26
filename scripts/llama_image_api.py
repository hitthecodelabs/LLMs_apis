from meta_ai_api import MetaAI

ai = MetaAI(fb_email="your_fb_email", fb_password="your_fb_password")
resp = ai.prompt(message="Generate an image of a tech CEO")

print(resp)
