rooms = ['on', 'off', 'off', 'on', 'off', 'on', 'off', 'on', 'on', 'on' , 'off', 'off', 'off']

wallet = int(20)

for i in rooms:
    
    if i =='on':
        wallet -= int(1)


print(f"You have ${wallet} remaining")
