import sys

# Read the arguments
filepath = sys.argv[1]

# Read lines
lines = []

with open(filepath, "r") as program:
    program_lines = [line.strip() for line in program.readlines()]

program = []
token_counter = 0
label_tracker = {}

for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # Check if line is empty
    if opcode == "":
        continue

    # Check if line contains a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # Else, store opcode
    program.append(opcode)
    token_counter += 1

    # Handling each opcode
    # OPCODE PUSH
    if opcode == "PUSH":
        # Expect a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        # Parsing the string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JUMP.EQ.0":
        # Read the label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "JUMP.GT.0":
        # Read the label
        label = parts[1]
        program.append(label)
        token_counter += 1

    

###
# Making the interpreter
### 

class Stack:
    def __init__(self):
        self.lst = [0 for _ in range(256)]
        self.pointer = -1
    
    def push(self, number):
        self.pointer += 1
        self.lst[self.pointer] = number
    
    def pop(self):
        number = self.lst[self.pointer]
        self.pointer -= 1
        return number
    
    def peek(self):
        return self.lst[self.pointer]
    

pc = 0
stack = Stack()
while program[pc] != "HALT":
    opcode = program[pc]
    pc += 1
    if opcode == "PUSH":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "READ":
        number = int(input())
        stack.push(number)
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push(a-b)
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)

    elif opcode == "JUMP.EQ.0":
        number = stack.peek()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "JUMP.GT.0":
        number = stack.peek()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1