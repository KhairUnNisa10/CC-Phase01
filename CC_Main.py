#Ashar [EB20102021]
#Khair Un Nisa [EB20102048]
#Muhammad Mukarram Asad [EB20102085]
#Saad Ali Khan [EB20102115]

#--------------- Phase # 01: Lexical Analyzer -------------------#

from CC_Lexer import Lexer
from CC_Tokenizer  import Tokenizer
#import my_parser

def main():
    # Read the current flow source code test.lang and store it in variable
    content = ""
    with open('input.txt','r') as file:
        content = file.read()
    print("--------------- Phase # 01: Lexical Analyzer -------------------\n")
    print("Given Input:")
    print(content)    
    print("\nWord Split Function on the Given Input:")
    wor = Lexer(content)
    words = wor.word_splitter()
    print(words)

    print("\nTokenization on the Given Input:")
    tok = Tokenizer(words)
    tokensList = tok.tokenizer()
    print("\n")
    tok.tokensIterator(tokensList)
    # print(tokenslist)
main()
