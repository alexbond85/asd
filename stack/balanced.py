def balanced_brackets(brackets: str, stack=None):
    if stack is None:
        stack = []
    for i, b in enumerate(brackets):
        is_closing = b == ')'
        if is_closing:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                return balanced_brackets(brackets[i+1:], stack=stack)
        else:
            stack.append(b)
    return len(stack) == 0


assert balanced_brackets("(()())")
assert not balanced_brackets(")(")
assert not balanced_brackets(")()(")
assert not balanced_brackets("())(")
assert not balanced_brackets("))((")
assert not balanced_brackets("((())")
assert balanced_brackets("((((()))))()()(())")
