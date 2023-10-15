import openai, config, context, gtts, playsound
from PIL import Image



class ai_body:
    def __init__(self):
        openai.api_key = config.API_KEY
        
        self.behavior = context.digital_personal
        self.history = [{'role':'system', 'content': self.behavior.context()},
            {'role':'system', 'content': self.behavior.society()},
            {'role':'system', 'content': self.behavior.client()}]
        return

    def prompt_input(self):
        _input = input('aseanidmiller: ')
        return _input    
    def audio_output(self, text):
        tts = gtts.gTTS(text, lang='en-gh')
        tts.save('Zahara.mp3')
        playsound.playsound('Zahara.mp3')
        return

    def chat_wgpt(self, model="gpt-3.5-turbo"):
        
        prompt = self.prompt_input()
        if prompt == 'exit': return 
        self.history.append({'role':'user', 'content': prompt})
        response = openai.ChatCompletion.create(
        model=model,
        messages=self.history)
        message = response.choices[0].message.content
        print(f'\n\n Zahara: {message}\n\n')
        self.history.append({'role':'assistant','content':message})
        self.audio_output(message)
        self.chat_wgpt()
       

app = ai_body()

app.chat_wgpt()
   