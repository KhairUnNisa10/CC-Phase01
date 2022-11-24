#Ashar [EB20102021]
#Khair Un Nisa [EB20102048]
#Muhammad Mukarram Asad [EB20102085]
#Saad Ali Khan [EB20102115]

#--------------- Phase # 01: Lexical Analyzer -------------------#

#CONSTANT
RE_INTEGER = '^[-+]?[0-9]+$'
RE_FLOAT = '^[-+]?\d*\.\d+$'
RE_IMAGINARY = '^\d*\+?\d*(.\d)?im$'
RE_OPERATORS = '\-|\+|\^|\%|\/|\*'
RE_IDENTIFIER = '^[a-zA-Z_]\w*$'
RE_STRING = r'^".*"$'
RE_KEYWORDS_BOOLEAN = "^True$|^False$"

#KEYWORDS
RE_KEYWORDS_DT = "^str$|^int$|^flt$|^img$|^bool$|^Vect$|^Dict$|^Set$"
RE_KEYWORDS_AM = "^priv$|^pub$|^prot$"
RE_KEYWORDS_CS = "^this$"
RE_KEYWORDS_CONDITIONS = "^if$|^orif$|^until$"
RE_KEYWORDS_LOOPS = "^for$ | ^while$| ^interface$"
RE_KEYWORDS_IS = "^Is$"
RE_KEYWORDS_CATCH = "^catch$"
RE_KEYWORDS_OPERATORS = "^Incas$|^Decas$|^Inc$|^Dec$"
RE_KEYWORDS_WO_CONDITIONS = "^else$|^try$|^atlast$"
RE_KEYWORDS_CO = "^Gt$|^Lt$|^Eq$|^Neq$|^Gte$|^Lte$"
RE_KEYWORDS_CLASS = "^class$"

RE_ALL_KEYWORDS = RE_KEYWORDS_DT \
    +'|'+RE_KEYWORDS_AM+'|'+RE_KEYWORDS_CS \
    +'|'+RE_KEYWORDS_CONDITIONS \
    +'|'+RE_KEYWORDS_WO_CONDITIONS+'|'+RE_KEYWORDS_LOOPS+'|'+RE_KEYWORDS_IS \
    +'|'+RE_KEYWORDS_CATCH \
    +'|'+RE_KEYWORDS_OPERATORS \
    +'|'+RE_KEYWORDS_CO \
    +'|'+RE_KEYWORDS_CLASS \
    +'|'+"^with$"\
    +'|'+"^to$"\
    +'|'+"^in$"\
    +'|'+"^prog$"\
    +'|'+"^use$"\
    +'|'+"^return$"\
    +'|'+"^null$"\
    +'|'+RE_KEYWORDS_BOOLEAN\
    
    
        
# operators + separators
RE_OR = "^\|$"
RE_NOT = "^!$"
RE_AND = "^&$"
RE_MDM = "^/*|//|%$"
RE_SA = "^\-|\+$"
RE_EXPO = "^\^$"
RE_PAREN = r'\(|\)|\[|\]|\{|\}'
RE_COMMA = "^,$"
