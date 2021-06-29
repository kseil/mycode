#!/usr/bin/env python3

#create list1
list1=['cisco_nxos', 'arista_eos', 'cisco_ios']

#display list1
print(list1)
#display item 2 in list one
print(list1[1])

#create list2
list2=['juniper']
#extend list1 by list2
list1.extend(list2)
#display new list
print(list1)

#create list3, append to list 1, and display
list3=['10.1.0.1', '10.2.0.1', '10.3.0.1']
list1.append(list3)
print(list1)

#print item 5 in list 1
print(list1[4][0])

