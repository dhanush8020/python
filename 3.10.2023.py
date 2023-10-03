def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # No matching opening bracket found
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # Mismatched brackets

    return len(stack) == 0  # True if all brackets are matched

# Example usage:
input_expression = input("Enter a string with parentheses: ")
if is_balanced(input_expression):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")
