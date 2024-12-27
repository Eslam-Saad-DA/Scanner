
# Top-Down Recursive Descent Parser for Simple Grammar

def simple_grammar_check(grammar):

    for nt, rules in grammar.items():
        if len(rules) != 2:  # Each non-terminal must have exactly 2 rules
            return False
        for rule in rules:
            if not rule:  # Empty rule
                return False
            # Check for allowed simple grammar structure: terminal(s) or terminal + non-terminal
            if not rule[0].islower():
                return False  # Rule must start with a terminal
        if len(set(rules)) != 2:  # No duplicate rules
            return False

        if(rules[0][0] == rules[1][0]):
            return False        # check on disjoint
    return True

def recursive_parser(input_str, grammar, non_terminal, index):
    """
    Recursive function to parse the input string.
    """
    if index == len(input_str):
        return index

    for rule in grammar[non_terminal]:
        temp_index = index
        stack = []
        for symbol in rule:
            if symbol.isupper():  # Non-terminal
                temp_index = recursive_parser(input_str, grammar, symbol, temp_index)
                if temp_index == -1:
                    break
            else:  # Terminal
                if temp_index < len(input_str) and input_str[temp_index] == symbol:
                    temp_index += 1
                    stack.append(symbol)
                else:
                    break
        else:  # Success in current rule
            return temp_index

    return -1  # Parsing failed


def main():
    print("Recursive Descent Parsing For Following Grammar")
    print("\U0001F447 Grammars \U0001F447\n")
    # Step 1: Getting the number of non-terminals
    n = int(input("Enter the number of non-terminals: "))
    # Step 2: Input Grammar
    grammar = {}
    for i in range(n):
        nt = input(f"Enter non-terminal {i + 1}: ").strip()
        grammar[nt] = []
        for j in range(2):
            rule = input(f"Enter rule number {j + 1} for non-terminal '{nt}': ").strip()
            grammar[nt].append(rule)

    # Step 3: Check if the grammar is simple
    if simple_grammar_check(grammar):
        print("\nThe entered grammar is a SIMPLE grammar. \n")
    else:
        print("\nThe entered grammar is NOT a SIMPLE grammar. \n")
        print("Try again")
        return main()

    input_string = input("Enter the string to be checked: ").strip()
    print(f"The input String: {list(input_string)}")

    stack_after_checking = []
    result = recursive_parser(input_string, grammar, list(grammar.keys())[0], 0)

    if result == len(input_string):
        print(f"Stack after checking: {stack_after_checking}")
        print("The rest of unchecked string: []")
        print("Your input String is Accepted.")

    else:
        print(f"Stack after checking: {stack_after_checking}")
        print(f"The rest of unchecked string: {list(input_string[result:])}")
        print("Your input String is Rejected.")
        


    # Step 4 Displaying user input choices
    while True:
        print("====================================================")
        print("1-Another Grammar.")
        print("2-Another String.")
        print("3-Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            return main()  # Restart the program for new grammar
        elif choice == '2':
            # Step 5: Input String and Parse
            input_string = input("Enter the string to be checked: ").strip()
            print(f"The input String: {list(input_string)}")

            stack_after_checking = []
            result = recursive_parser(input_string, grammar, list(grammar.keys())[0], 0)

            if result == len(input_string):
                print(f"Stack after checking: {stack_after_checking}")
                print("The rest of unchecked string: []")
                print("Your input String is Accepted.")
            else:
                print(f"Stack after checking: {list(input_string[result:])}")
                print(f"The rest of unchecked string: []")
                print("Your input String is Rejected.")
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()