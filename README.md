# Telegram chatbot  
bot name:@HungerBot
This is a chatbot of telegram which can search the shop in googlemap and help us do the decision of what we eat later.

### Run Locally  
You can either setup https server or using `ngrok` as a proxy.  

**`ngrok` would be used in the following instruction**  

```sh  
./ngrok http 5000  
```  

After that, `ngrok` would generate a https URL.  

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.  

#### Run the sever  

```sh  
python3 app.py  
```  

## Finite State Machine  
  ![fsm](https://i.imgur.com/MccyeeQ.png)


## Usage  
The initial state is set to `user`.  

Every time `user` state is triggered to `advance` to `eat` state, and go next state by triggering `advance`. At the last state, they will `go_back` to `user` state after the bot replies corresponding message.  

* user  
    * Input: "hungry"  
        *   Output: 
            "search restaurant? type:search
            want to eat fastfood? type:fast food 
            want to eat normal food? type:normal food  "
                     -> go to eat 
    * Input: "fried" -> go to fried
    * Input: "cheap" -> go to cheap
        * 
    
* eat
    * Input: "search" -> go to search state
    * Input: "fast food" -> go to fast food state
    * Input: "normal food" -> go to food state

* search    
    * Output: "Please type where do you want to find? 輸入你想找的店" 
        * Input: "711"(anywhere) -> go to google state

* google    
    * Output: "https://www.google.com.tw/maps/search/711"
        ->return user state

* fast food
    * Output: "fried or non-fried"
        * Input: "fried" -> go to fried state
        * Input: "non-fried" -> go to non-fried state

* fried
    * Output:"KFC"(random produce the restaurant)
        "to go"(random produce for here or to go)    
        -> return user state

* non-fried
    * Ouput:"subway"(random produce the restaurant)
        "to go"(random produce for here or to go)    
        -> return user state
        
* food
    * Output: "expensive or cheap"
        * Input: "expensive" -> go to expensive state
        * Input: "cheap" -> go to cheap state

* expensive
    * Output: "西提"(random produce the restaurant)
        "to go"(random produce for here or to go)    
        -> return user state
        
* cheap
    * Output: "煦悅"(random produce the restaurant)
        "for here"(random produce for here or to go)    
        -> return user state