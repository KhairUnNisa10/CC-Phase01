#Ashar [EB20102021]
#Khair Un Nisa [EB20102048]
#Muhammad Mukarram Asad [EB20102085]
#Saad Ali Khan [EB20102115]

#--------------- Phase # 01: Lexical Analyzer -------------------#

from CC_RE import *
import re


class Token:
    def __init__(self):
        self.classPart = ''
        self.valuePart = ''
        self.lineNumber = None

class Tokenizer:
    def __init__(self,words):
        self.words = words

    def validateIndentifierForKeyword(self,i):
        if re.findall(RE_KEYWORDS_DT,self.words[i]):
            curClassPart = "DType"
            
        elif re.findall(RE_KEYWORDS_CO,self.words[i]):
            curClassPart = "COperators"

        elif re.findall(RE_KEYWORDS_WO_CONDITIONS,self.words[i]):
            curClassPart = "WoConditons"

        elif re.findall(RE_KEYWORDS_CONDITIONS,self.words[i]):
            curClassPart = "Conditions"
        

        elif re.findall(RE_KEYWORDS_CS,self.words[i]):
            curClassPart = "Class"
            
        elif re.findall(RE_KEYWORDS_OPERATORS,self.words[i]):
            curClassPart = "ROperators"

        elif re.findall(RE_KEYWORDS_AM,self.words[i]):
            curClassPart = "AccessModifier"

        elif re.findall(RE_KEYWORDS_BOOLEAN,self.words[i]):
            curClassPart = "BOOLEAN"

        else:
            curClassPart = self.words[i]
        
        return curClassPart

    def tokensIterator(self, tokens):
        for token in tokens:
            print(f"Line # '{token.lineNumber}'\nClassPart: '{token.classPart}'\nValuePart: '{token.valuePart}' \n")


    def tokenizer(self):
        
        tokensList = []
        curLine = 1

        i = 0
        while i<len(self.words):
            token = Token()
            curClassPart = ''

            if(self.words[i] == '\n'):
                curLine += 1

            elif re.match(RE_INTEGER,self.words[i]):
                curClassPart = "INTEGER"

            elif re.match(RE_FLOAT,self.words[i]):
                curClassPart = "FLOAT"

            # imaginary            
            elif re.match(RE_IMAGINARY,self.words[i]):
                curClassPart = "IMAGINARY"
            
            elif re.match(RE_STRING,self.words[i]):
                curClassPart = "STRING"

            elif re.match(RE_OPERATORS,self.words[i]):

                if re.match(RE_SA,self.words[i]):

                    if not re.match(RE_INTEGER+"|"+RE_FLOAT+"|"+RE_IMAGINARY,self.words[i-1]):
                        
                        if re.match(RE_INTEGER,self.words[i]+self.words[i+1]):
                            curClassPart = "INTEGER"
                            token.valuePart = self.words[i]
                            i += 1

                        elif re.match(RE_FLOAT,self.words[i]+self.words[i+1]):
                            curClassPart = "FLOAT"
                            token.valuePart = self.words[i]
                            i += 1

                        elif re.match(RE_IMAGINARY,self.words[i]+self.words[i+1]):
                            curClassPart = "IMAGINARY"
                            token.valuePart = self.words[i]
                            i += 1
                        else:
                            curClassPart = "SA"

                    else:
                         curClassPart = "SA"
                         
                elif re.match(RE_MDM,self.words[i]):
                    curClassPart = "MDM"

                elif re.match(RE_EXPO,self.words[i]):
                    curClassPart = "EXPO"
                
                # identifier 
            elif re.match(RE_IDENTIFIER,self.words[i]):
                

                if re.match(RE_ALL_KEYWORDS,self.words[i]):
                    res = self.validateIndentifierForKeyword(i)
                    curClassPart = res
        
                elif self.words[i+1] == "(":
                    curClassPart = "Function"
        
                else:
                    curClassPart = "IDENTIFIER"
                
                
            elif re.findall(RE_OR,self.words[i]):
                curClassPart = "OR"


            elif re.findall(RE_AND,self.words[i]):
                curClassPart = "AND"

            elif re.findall(RE_NOT,self.words[i]):
                curClassPart = "NOT"


            elif re.search(RE_PAREN,self.words[i]):
                curClassPart = "Parenthesis"

            elif re.search(RE_COMMA,self.words[i]):
                curClassPart = "Comma"

            else:
                curClassPart = "Invalid Token!"

            token.classPart = curClassPart
            token.valuePart += self.words[i]
            token.lineNumber = curLine
            tokensList.append(token) if(curClassPart) else None

            i+=1

        return tokensList
