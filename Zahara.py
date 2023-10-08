import os, datetime, pyperclip, openai
from PIL import Image
from pytesseract import pytesseract

path_to_tesseract =  r'C:\Users\x-admiller\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

print(f'-------------------------------------------------------------------------------- \n **Welcome Back {datetime.date.today()} **\n -------------------------------------------------------------------------------- ')

class zoox_tools:
    def __init__(self):
        openai.api_key = "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"
        return

    def scrape_image(self):
       try:
        dirname = "C:/Users/x-admiller/Desktop/tsimage"
        files = os.listdir(dirname)
        
        file = "/" +  files[0]
        image_path = dirname + file
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print(f' \nThe text detected from your image:\n -------------------------------------------\n{text}\n------------------------------------------ \nit has also been copied to your clipboard\n')
        pyperclip.copy(text)
       except IndexError:
         print(f' IndexError: No Image File detected, remember to save directly to {dirname}')  
        
       for file in files:
            f = os.path.join(dirname, file)
            os.remove(f)
       return
        
    
    def chat_wgpt(self,prompt='', model="gpt-3.5-turbo"):
        if prompt == "":
           prompt = input('x-admiller>>: ')
        if prompt == 'exit': return 
        response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role':'system', 'content': prompt}],
         )
        message = response.choices[0].message.content
        print(f'\n\n ChatGPT: {message}\n\n')
       
        self.chat_wgpt()
       

app = zoox_tools()
program = { 'image': app.scrape_image,
            '//chatgpt': app.chat_wgpt}

choice = input('\n #What would you like to do Mr Miller?>>: ')

while choice != 'exit':
    if choice[-1] == '?':
        app.chat_wgpt(prompt=choice)
        choice = input('\n ##What else would you like to do Mr Miller?>>: ')
        
    if not program.get(choice):
        print('I do not recognize that command\n*Here is a list of keys*\n')
        for key in program.keys():
             print('--' + key)    
        choice = input('\n ##What else would you like to do Mr Miller?>>: ')
        continue
    

    program[choice]()
    choice = input('\n ##What else would you like to do Mr Miller?>>: ')
   