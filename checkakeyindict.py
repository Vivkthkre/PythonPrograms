mydict={'name':'Ken','course':'Python','roll':56,'Branch':'EC',1:2,2:4,3:9}
key=input("Enter key to check:")
if key in mydict.keys():
    print("Key exists")
else:
    print("Key does not exists")
