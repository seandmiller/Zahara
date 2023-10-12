import openai, config, context
from PIL import Image



class ai_body:
    def __init__(self):
        openai.api_key = config.API_KEY
        
        self.behavior = context.digital_personal
        return

    def prompt_input(self):
        _input = input('aseanidmiller: ')
        return _input    
    
    def chat_wgpt(self, model="gpt-3.5-turbo"):
        
        prompt = self.prompt_input()
        if prompt == 'exit': return 
        response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role':'system', 'content': self.behavior.context()},
            {'role':'user', 'content': prompt}])
        message = response.choices[0].message.content
        print(f'\n\n Zahara: {message}\n\n')
        
        self.chat_wgpt()
       

app = ai_body()

app.chat_wgpt()
   