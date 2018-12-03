import string

# print stored 
def print_stored(wew):
    global stored

    wew = str(wew)
    print(  '\n\n\n\n -------------\n',
            "Hex ",
            stored[wew]['h'],
            "\nIP: ",
            stored[wew]['i'], 
            '\n -------------\n'
        )

    input("ENTER TO CONTINE ....")

# convert hex to ip
def iptohex():
    pass

# convert hex to an ip 
def hextoip():
    global levelofitems 
    global printtext
    global item
    h = input('Enter hex 0x format: ')

    # contailer for the individual item
    item = {  
                'h':'',
                'i':''
            }

    
    # set the hex in the item
    item['h'] = h

    if '0x' in h:
        h = h.split('0x')[1]

    # converting 
    lispth = []
    aa = True
    for x in h:
        if aa:
            lispth.append(x)
            aa = False
        else: 
            lispth[-1] += x
            aa = True
    ip = ''

    # putting in ip format 
    for x in lispth:

        # if its the last one
        if x == lispth[-1]:
            x = '0x' + x
            ip += str(int(x, 0))
        else:
            x = '0x' + x
            ip += str(int(x, 0)) + '.'
    
    # set its ip
    item['i'] = ip
    printtext +=  str(levelofitems) + '> Print this numbers info\n'
    return item




# globals 
stored = {}
levelofitems = 3
printtext = "1> IP to Hexidecimal \n2> Hexidecimal to IP\n"
item = {}


    # so that other things can be appened to it later 
    
while True:
    # print the string for it
    a = input(printtext)


    if a == '1':
        iptohex()
    elif a == '2':
        stored[str(levelofitems)] = hextoip()
        levelofitems+=1
    elif int(a) >= 3:
        print_stored(a)

    else:
        print("bye ")
        exit()