#Pdf2csv('\\Users\\Clay\\Desktop\\PyChron\\sample3.txt')
def pdf2csv():
    import os
    location = raw_input('Which file would you like to convert?: \n')
    location = location +'.txt'
    source = open(location,'r')
    input = source.read()
    charCount = 0
    genericCount = 0
    genericCount2 = 0
    switchVar = 0               
    pagecheckVar = 0
    pagecheckVar2 = 0
    findstartVar = 0
    binaryCheck = 0
    binaryCheck2 = 0
    endCheck = 0
    lastDate = ''
    dateCheck = 'aaa'
    lasDate = ''
    lastDate = ''
    findStart = 'aaa'
    dateAbb = 'aaa'
    outputFind = ''
    pageCheck = 'aaaaaaaaaaaaaaaaaaa'
    pageCheck2 = 'aaaaaaaaaaaaaaaaaaa'
    sectionCheck = 'aaaaaaaa'
    text = '" '
    titlestring = ''

    for p in input:
        findstartVar = findstartVar + 1
        if p == ':':
            if input[findstartVar-2] == '1' or input[findstartVar-2] == '2' or input[findstartVar-2] == '3' or input[findstartVar-2] == '4' or input[findstartVar-2] == '5' or input[findstartVar-2] == '6' or input[findstartVar-2] == '7' or input[findstartVar-2] == '8' or input[findstartVar-2] == '9' or input[findstartVar-2] == '0':
                input = input[(findstartVar - 8):]
                break
            
    for s in input:
        dateCheck =dateCheck[1:] + s
        genericCount2 = genericCount2 + 1
        sectionCheck = sectionCheck[1:] + s
        if s == ']':
            endCheck = genericCount2
        elif sectionCheck == 'See also' and endCheck != 0:
            binaryCheck = 1
        elif dateCheck == 'Jan' or dateCheck =='Feb' or dateCheck =='Mar' or dateCheck =='Apr' or dateCheck =='May' or dateCheck =='Jun' or dateCheck =='Jul' or dateCheck =='Aug' or dateCheck =='Sep' or dateCheck =='Oct' or dateCheck =='Nov' or dateCheck =='Dec':
            if binaryCheck == 1:
                input = input[:endCheck]+ dateCheck + input[genericCount2:]
                genericCount2 = genericCount2+3-(genericCount2-endCheck)
        elif s == ':':
            binaryCheck = 0
            endCheck = 0
            dateCheck = 'aaa'

    for x in input:
        genericCount = 0
        binaryCheck = 0
        charCount = charCount + 1

        if switchVar == 1 and x != '\n':
            if x ==':':
                lastDate  = lastDate +'|'
            else:
                lastDate = lastDate + x
        
        if x == '\n' or x == '^M':
            text = text + ' '
            if switchVar == 2:
                titlestring =titlestring + ' '
                
        elif x == ']':
            text = text + '|"\n'+'"'
            titlestring = ''
            for l in input[charCount:(charCount + 8)]:
                dateCheck = dateCheck[1:]+l
                if dateCheck == 'Jan' or dateCheck =='Feb' or dateCheck =='Mar' or dateCheck =='Apr' or dateCheck =='May' or dateCheck =='Jun' or dateCheck =='Jul' or dateCheck =='Aug' or dateCheck =='Sep' or dateCheck =='Oct' or dateCheck =='Nov' or dateCheck =='Dec':
                    binaryCheck = 1
                    switchVar = 1
                    lastDate = ''

                
            if binaryCheck != 1:
                genericCount = 0
                for w in lastDate:
                    genericCount = genericCount + 1
                text = text + ' ' + lastDate
                switchVar = 0
                
            
        elif x == ':':
            text = text+'|'
            switchVar = 2
            
        elif x == '.' and switchVar == 2:
            titlestring = titlestring + x
            text = text + x +'|' + titlestring
            switchVar = 3
            
        elif x == '[':
            text = text+'|'
            switchVar = 4
            
        elif switchVar == 2:
            titlestring = titlestring + x
            text = text + x
            
        else:
            text = text + x

    
    for n in text:
        pageCheck = pageCheck[1:] + n
        pagecheckVar = pagecheckVar + 1
        if pageCheck == 'MIDDLE EAST JOURNAL':
            text = text[:(pagecheckVar-25)]+ text[pagecheckVar:]
            pageCheck = 'aaaaaaaaaaaaaaaaaaa'
            pagecheckVar = pagecheckVar - 25

    for q in text:
        pageCheck2 = pageCheck2[1:] + q
        pagecheckVar2 = pagecheckVar2 + 1
        if pageCheck2 == 'middle east journal':
            text = text[:(pagecheckVar2-19)]+ text[(pagecheckVar2+6):]
            pageCheck2 = 'aaaaaaaaaaaaaaaaaaa'
            pagecheckVar2 = pagecheckVar2 - 25
    test = os.getcwd()
#    newLocation = raw_input('What would you like to call this? \n')
    file = open(test+ '\\output\\' + location, 'w')
    file.write(text[:-10])
    file.close()

            
