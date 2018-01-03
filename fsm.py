from transitions.extensions import GraphMachine
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_eat(self, update):
        text = update.message.text
        return text.lower() == 'hungry'
    
    def is_going_to_search(self, update):
        text = update.message.text
        return text.lower() == 'search'

    def is_going_to_google(self,update):
        text = update.message.text
        update.message.reply_text("https://www.google.com.tw/maps/search/"+text)
        return text.lower() == text.lower()

    def is_going_to_fastfood(self, update):
        text = update.message.text
        return text.lower() == 'fast food'
	
    def is_going_to_fried(self,update):
        text = update.message.text
        return text.lower() == 'fried'

    def is_going_to_nonfried(self,update):
        text = update.message.text
        return text.lower() == 'non-fried'
    
    def is_going_to_food(self,update):
        text = update.message.text
        return text.lower() == 'normal food'

    def is_going_to_expensive(self,update):
        text = update.message.text
        return text.lower() == 'expensive'

    def is_going_to_cheap(self,update):
        text = update.message.text
        return text.lower() == 'cheap'

    def on_enter_eat(self, update):
        update.message.reply_text("search restaurant? type:search")
        update.message.reply_text("want to eat fastfood? type:fast food");
        update.message.reply_text("want to eat normal food? type:normal food")
		#self.go_back(update)
    
    def on_exit_eat(self, update):
        print('Leaving eat')
    
    def on_enter_search(self, update):
        update.message.reply_text("Please type where do you want to find?")
        update.message.reply_text("輸入你想找的店")
        #self.go_back(update)
    
    def on_exit_search(self, update):
        print('Leaving search')
    
    def on_enter_google(self, update):
        update.message.reply_text("See you, guy.")
        self.go_back(update)
    
    def on_exit_google(self, update):
        print('Leaving google')
    
    def on_enter_fastfood(self, update):
        update.message.reply_text("fried or non-fried?")

    def on_exit_fastfood(self, update):
        print('Leaving fastfood')

    def on_enter_fried(self,update):
        i = random.randint(1,4)
        if i == 1:
            what="McDonald"
        elif i == 2:
            what="KFC"
        elif i == 3:
            what="Mos"
        elif i == 4:
            what="21Century"
        #print(what)
        update.message.reply_text(what)
        
        j = random.randint(1,2)
        if j == 1:
            where="for here"
        elif j == 2:
            where="to go"
        
        update.message.reply_text(where)
        update.message.reply_text("See you, guy.")
        self.go_back(update)

    def on_exit_fried(self,update):
        print("exit fried")

    def on_enter_nonfried(self,update):
        i = random.randint(1,3)
        if i == 1:
            what="PizzaHut"
        elif i == 2:
            what="Subway"
        elif i == 3:
            what="Dandan"
        #print(what)
        update.message.reply_text(what)
        
        j = random.randint(1,2)
        if j == 1:
            where="for here"
        elif j == 2:
            where="to go"
        
        update.message.reply_text(where)
        update.message.reply_text("See you, guy.")
        self.go_back(update)
    
    def on_exit_nonfried(self,update):
        print("leaving nonfried")

    def on_enter_food(self, update):
        update.message.reply_text("expensive or cheap?")
		#self.go_back(update)

    def on_exit_food(self, update):
        print('Leaving food')
    
    def on_enter_expensive(self,update):
        i = random.randint(1,5)
        if i == 1:
            what="哞王"
        elif i == 2:
            what="澄花"
        elif i == 3:
            what="西提"
        elif i == 4:
            what="陶板屋"
        elif i == 5:
            what="覺丸拉麵"
        #print(what)
        update.message.reply_text(what)
        
        j = random.randint(1,2)
        if j == 1:
            where="for here"
        elif j == 2:
            where="to go"
        
        update.message.reply_text(where)
        update.message.reply_text("See you, guy.")
        self.go_back(update)

    def on_exit_expensive(self,update):
        print("leaving expensive")

    def on_enter_cheap(self,update):
        i = random.randint(1,16)
        if i == 1:
            what="不倒翁"
        elif i == 2:
            what="7-11"
        elif i == 3:
            what="勝利早點"
        elif i == 4:
            what="四海遊龍"
        elif i == 5:
            what="甜麵屋"
        elif i == 6:
            what="煦悅"
        elif i == 7:
            what="活力小廚"
        elif i == 8:
            what="阿甘"
        elif i == 9:
            what="小妞"
        elif i == 10:
            what="原味屋"
        elif i == 11:
            what="甜麵屋"
        elif i == 12:
            what="阿閔"
        elif i == 13:
            what="紅樓小館"
        elif i == 14:
            what="雅味"
        elif i == 15:
            what="小廚師"
        elif i == 16:
            what="炒翻天"
        #print(what)
        update.message.reply_text(what)
        
        j = random.randint(1,2)
        if j == 1:
            where="for here"
        elif j == 2:
            where="to go"
        
        update.message.reply_text(where)
        update.message.reply_text("See you, guy.")
        self.go_back(update)

    def on_exit_cheap(self,update):
        print("leaving cheap")


