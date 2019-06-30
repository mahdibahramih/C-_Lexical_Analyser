# -*- coding: utf-8 -*-
key_file = open('./keywords.txt','r')
source_file = open("./code.cpp" , "r")
out_file = open('output.txt', 'w')                               
operator_file = open('operators.txt','r')
key_word = []
operator =[]
state = 0 
word =""
col = 0
row = 0 
blok = 0
token = {'type':'' , 'col':'' , 'row':'' , 'block':'' , 'text':''}

def write_to_file():
        out_file.write('     value    :   '+token['text']+'\n')
        out_file.write('     column   :   '+token['col']+'\n')
        out_file.write('     row      :   '+token['row']+'\n')
        out_file.write('     type     :   '+token['type']+'\n')
        out_file.write('     block    :   '+str(blok)+'\n')
        out_file.write('----------------------------------\n')
        token['text']=""
        token['type'] = "" 

def isoperator(word):
        if(word in operator):
                return True
        else:
                return False

def isdelimeter(word):
        deli = [':',';',',','.','(',')','{','}','[',']']
        if word in deli:
                return True
        else:
                return False

	


for i in key_file:
        for j in i.split():
                key_word.append(j)
for i in operator_file:
        for j in i.split():
                operator.append(j)

for kalame in source_file:
        for harf in kalame :
                if (state == 0 ):
                        if (harf == " " ):
                                col = col +1
                                continue
                        elif (harf == '\t'):
                                col += 6
                                continue
                        elif (harf == '\n'):
                                row +=1
                                col = 0
                         
                        elif(harf.isdigit() ):
                                state = 2
                                token['text'] = harf
                                token['col'] = str(col)
                                token['row'] = str(row)
                                col += 1
                                continue
                        elif(harf.isalpha() or harf == '_'):
                                state = 3
                                token['text'] = harf
                                token['col'] = str(col)
                                token['row'] = str(row)
                                col += 1
                                continue
                        elif(harf == "/"):
                                state = 5
                                token['text'] = harf
                                token['col'] = str(col)
                                token['row'] = str(row)
                                col += 1
                                continue
                        elif(isoperator(harf)):
                                state = 1
                                token['text'] = harf
                                token ['type'] = 'operator'
                                token['col'] = str(col)
                                token['row'] = str(row)
                                col += 1
                                continue
                        elif(harf in "\""):
                                state = 4
                                token['text'] = harf
                                token['col'] = str(col)
                                token['row'] = str(row)
                                col += 1
                                continue
                        elif(isdelimeter(harf)):
                                if harf == '{' :
                                        blok += 1 
                                if harf == '}' :
                                        blok -= 1 
                                token['text'] = harf
                                token['col'] = str(col)
                                token['row'] = str(row)
                                token['type'] = 'Delimeter'
                                col += 1
                                write_to_file()
                                state = 0
                                continue
                        
                                

                if(state == 1):
                        if(isoperator(harf)):
                                token['text'] += harf 
                                write_to_file()
                                state =0
                                col += 1
                        else:
                                write_to_file()
                                col += 1
                                state =0
                                


                if(state == 2):
                        if(harf.isdigit()):
                                token['text'] += harf
                                token['type'] = 'intiger'
                                col += 1
                                continue
                        elif(harf == '.'):
                                token['text'] += harf
                                token['type'] = 'double'
                                col += 1
                                state = 21
                                continue
                        else:
                                write_to_file()
                                state = 0
                if(state == 21 ):
                        if(harf.isdigit()):
                                col += 1
                                token['text'] += harf
                                continue
                        else:
                                write_to_file()
                                state=0

                if ( state == 3):
                        if (harf.isalpha() or harf == '_'):
                                col += 1
                                token['text'] += harf
                                continue
                        else:
                                col +=1
                                if ( token['text'] in key_word):
                                        token['type'] = 'key_word' 
                                else:
                                        token['type'] = 'identifier'
                                write_to_file()   
                                state = 0     
                if(state == 4 ):
                        col += 1
                        if(harf == "\""):
                                token['text'] += harf
                                token['type'] = 'string'
                                write_to_file()   
                                state = 0  
                        else:
                                token['text'] += harf
                                continue
                if(state == 5):
                        col += 1
                        if(harf == '*'):
                                state = 51
                                token['text'] += harf
                                token['type'] = 'comment'
                                continue
                        else:
                                state = 3
                                continue 
                if(state == 51):
                        col += 1
                        if(harf == '*'):
                                token['text'] += harf
                                state = 52
                                continue
                        else : 
                                token['text'] += harf
                if(state == 52):
                        col += 1
                        if(harf == "/"):
                                token['text'] += harf
                                write_to_file()
                                state =0

