s = ['CP2105 Dual USB to UART Bridge Controller - STANDARD Com Port ttyUSB1' , 'CP2105 Dual USB to UART Bridge Controller - ENHANCED Com Port ttyUSB0' ]

for i in s:
    if 'CP2105'.lower () in i.lower () and 'Enhanced'.lower () in i.lower ():
        print ('Enhanced found')
    if 'CP2105'.lower () in i.lower () and 'Standard'.lower () in i.lower ():
        print ('Standard found')