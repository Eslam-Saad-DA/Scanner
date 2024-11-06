''' This programm with python act like scanner for C/C++ '''
import re

# Define token types with additional patterns for comments
Token_type = {
    'KEYWORD': r'\b(if|else|switch|case|default|for|while|do|break|continue|return|goto|int|float|double|char|bool|void|wchar_t|signed|unsigned|long|short|const|volatile|new|delete|sizeof|class|struct|union|enum|public|private|protected|this|virtual|friend|namespace|using|try|catch|throw|true|false|auto|static|extern|inline|typedef|cout|cin|printf)\b',
    'IDENTIFIER': r'\b[a-zA-Z_]\w*\b',
    'NUMBER': r'\b\d+\b',
    'SINGLELINECOMMENT': r'//.*',
    'MULTILINECOMMENT': r'/\*[\s\S]*?\*/',
    'OPERATOR': r'[+\-*/=<>!]',
    'SPECIALCHARACTER': r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\"",
    'WHITESPACE': r'\s+',
    'UNKNOWN': r'.'
}

# Create a Function to tokeniaze the input 
def tokenize(input_program):
    tokens = []
    index = 0
    while index < len(input_program):
        match = None
        for token_type, pattern in Token_type.items():
            regex = re.compile(pattern)
            match = regex.match(input_program, index)
            if match:
                # Extract the matched token and its type
                token_value = match.group(0)
                if token_type not in ['WHITESPACE']:  # Ignore whitespace tokens
                    tokens.append((token_value, token_type))
                index = match.end(0)  # Move to the end of the matched token
                break
        if not match:  # If no pattern matched, move forward
            index += 1
    return tokens


print("Enter your code (type 'END' on a new line to finish):")
input_program_lines = []


# To input multiline string 
while True:
    line = input()
    if line.strip().upper() == 'END':  # User types 'END' to finish input
        break
    input_program_lines.append(line)

# Join all lines into a single string for tokenizing
input_program = "\n".join(input_program_lines)

# Tokenize the input program
tokens = tokenize(input_program)

# Display the tokens with their types
for token, token_type in tokens:
    print(f"The token '{token}' Type --> {token_type}")
    
input("Enter anything to EXIT : ")

