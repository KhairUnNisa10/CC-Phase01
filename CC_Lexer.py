#Ashar [EB20102021]
#Khair Un Nisa [EB20102048]
#Muhammad Mukarram Asad [EB20102085]
#Saad Ali Khan [EB20102115]

#--------------- Phase # 01: Lexical Analyzer -------------------#

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
    
    def __EOF(self,index):
        return index == len(self.source_code)
            
    def word_splitter(self):
        
      
        lexem = ""
        words = []
        i = 0
        code = self.source_code
        curLine = 1
        #Operators
        while i<len(code):           
            if code[i] in ["|","!","(",")","[","]","{","}","-","+","^","%","/","*",",",":","&","="]:
                words.append(lexem)
                lexem = ""
                words.append(code[i])
            elif code[i] in ['"']:
                words.append(lexem)
                lexem = ""
                lexem +=code[i]
                i+=1

            #Single Line Comment    
            elif code[i] in ["~"]:
                words.append(lexem)
                lexem = ""
                while True:
                    if self.__EOF(i):
                        break
                    elif code[i] == "\n" :
                        words.append(code[i])
                        break
                    else:
                        i+=1
                curLine += 1
            
            elif code[i] in ['`']: 
                words.append(lexem)
                lexem = ""
                i+=1
                tempLineCounts = 0
                try:
                    while True:
                        if(code[i] == '\\'):
                            if(code[i+1] == '`'):  
                                i+=2
                        elif(code[i] == '`'):
                            break
                        
                        elif(code[i]=='\n'):
                            words.append(code[i])
                            tempLineCounts += 1
                        i+=1
                except:
                    errMsg = "Comment Error on line {curLine}."
                    raise Exception(errMsg)
                curLine += tempLineCounts

            #End of Statement/Line
            elif code[i] in [" ",";"]:
                words.append(lexem)
                lexem = ""
            #New Line
            elif(code[i]=='\n'):
                    curLine += 1
                    words.append(lexem)
                    lexem = ""
                    words.append(code[i])
                    
            #Period
            elif code[i] == ".":
                
                if code[i-1].isdigit() or code[i+1].isdigit():
                    lexem+=code[i]
                else:
                    words.append(lexem)
                    lexem = ''
                    words.append(code[i])
                    
            else:
                lexem += code[i]
            i+=1

        words.append(lexem) if lexem else None
        words = [i for i in words if i]

        return words
