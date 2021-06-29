#!/usr/bin/env python3

#create dictionary

switch = {'hostname': 'sw1', 'IP':'10.0.1.1', "version":'1.2', 'vendor': 'cisco'}

print(switch['hostname'])
print(switch['IP'])


##request a fake key

#print(switch['lynx'])


#request a fake key with .get method

print('first test - .get()')
print( switch.get('lynx'))

print( 'second test -.get()')
print(switch.get ('lynx', 'the key is in another castle'))

print('third test - .get()')
print(switch.get('version'))

print('fourth test- .keys()')
print (switch.keys())

print('fifth test -.values()')
print(switch.values())

print( "Sixth test - .pop()" )
switch.pop("version") # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

