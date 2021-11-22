statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(sta):
    y = 0
    x = sta.values()
    #return x
    for num in x:
        if num == "online":
            y = y + 1
    print(y)        
    return y       
            
        
    
online_count(statuses)



