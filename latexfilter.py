#!/usr/bin/python

import sys

skip = False

for line in sys.stdin:
    stack = [""]

    for char in line:
        if char == '(':
            stack.append("(")
        elif char == ')' and len(stack) > 1:
            stack = stack[:-1]
            skip = True
        elif char == ' ' and skip:
            skip=False
        elif char == '\n':
            stack[0] = "".join(stack)+"\n"
        else:
            stack[-1] = stack[-1]+char

    sys.stdout.write(stack[0])