from Chrome import Chrome

class WhatsBot(Chrome):
    
    def __init__(self, cookies=True, hidden=False):
        super().__init__(cookies, hidden)
        self.url = "https://web.whatsapp.com/"
        
        self.get(self.url)

    