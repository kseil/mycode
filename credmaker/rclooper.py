#!/usr/bin/env python3

#stdlib import
import csv

#open csv data
with open('csv_users.txt','r') as csvfile:
    #counter for UIDs
    i=0
    #loop across by line
    for row in csv.reader(csvfile):
        i += 1 #increase counter by 1
        filename=f"admin.rc{i}" #fstring to fill in value of i

        #use with to open file and print data
        with open (filename, 'w') as rcfile:
            #use stdlib print fuction
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
            print('export OS_PROJECT_NAME=' + row[1], file=rcfile)
            print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile)
            print('export OS_USERNAME=' + row[3], file=rcfile)
            print('OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)
            print('export OS_PASSWORD=' + row[5], file=rcfile)

            #end indentation and close files


#display to show shen loops are done
print('admin.rc files created!')

