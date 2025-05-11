table = {
    0:  {"id": {"S": 5},    "+": "",        "*": "",        "(": {"S": 4},  ")": "",        "$": "",                "E": 1,     "T": 2,     "F": 3},
    1:  {"id": "",          "+": {"S": 6},  "*": "",        "(": "",        ")": "",        "$": {"accept": ""},    "E": "",    "T": "",    "F": ""},
    2:  {"id": "",          "+": {"R": 2},  "*": {"S": 7},  "(": "",        ")": {"R": 2},  "$": {"R": 2},          "E": "",    "T": "",    "F": ""},
    3:  {"id": "",          "+": {"R": 4},  "*": {"R": 4},  "(": "",        ")": {"R": 4},  "$": {"R": 4},          "E": "",    "T": "",    "F": ""},
    4:  {"id": {"S": 5},    "+": "",        "*": "",        "(": {"S": 4},  ")": "",        "$": "",                "E": 8,     "T": 2,     "F": 3},
    5:  {"id": "",          "+": {"R": 6},  "*": {"R": 6},  "(": "",        ")": {"R": 6},  "$": {"R": 6},          "E": "",    "T": "",    "F": ""},
    6:  {"id": {"S": 5},    "+": "",        "*": "",        "(": {"S": 4},  ")": "",        "$": "",                "E": "",    "T": 9,     "F": 3},
    7:  {"id": {"S": 5},    "+": "",        "*": "",        "(": {"S": 4},  ")": "",        "$": "",                "E": "",    "T": "",    "F": 10},
    8:  {"id": "",          "+": {"S": 6},  "*": "",        "(": "",        ")": {"S": 11}, "$": "",                "E": "",    "T": "",    "F": ""},
    9:  {"id": "",          "+": {"R": 1},  "*": {"S": 7},  "(": "",        ")": {"R": 1},  "$": {"R": 1},          "E": "",    "T": "",    "F": ""},
    10: {"id": "",          "+": {"R": 3},  "*": {"R": 3},  "(": "",        ")": {"R": 3},  "$": {"R": 3},          "E": "",    "T": "",    "F": ""},
    11: {"id": "",          "+": {"R": 5},  "*": {"R": 5},  "(": "",        ")": {"R": 5},  "$": {"R": 5},          "E": "",    "T": "",    "F": ""}
}

rules = {
    "E+T":  "E",
    "T"  :  "E",
    "T*F":  "T",
    "F"  :  "T",
    "(E)":  "F",
    "id" :  "F"
}

def action(x):
    ans = table[stack[x][0]][string[0]]
    if ans != "": return list(ans.keys())[0]
    else: return -1
    
def number(x):
    ans = table[stack[x][0]][stack[x][1]]
    if ans != "":
        if type(ans) == type(dict()):
            return list(ans.values())[0]
        else: return ans
    else: return -1

print("This program checks if the entered string is valid according to the grammar:\nE -> E + T | T\nT -> T * F | F\nF -> ( E ) | id\n")
print("Enter the string to be checked. The string must be in the form of:\n<id> + <id> * <id> + <id> * <id> + ...\n")
print("Press Enter to exit the program.\n")

while True:    
    inputs = input("Enter your string:\n")
    if inputs == "": break
    a, i, j = 0, 0, 0
    string = list()
    stack = [[0]]
    while i < len(inputs):
        if inputs[i] == "i":
            string.append("id")
            i += 1
            j += 1
        elif inputs[i] == "(" or inputs[i] == ")":
            string.append(inputs[i])
        else:
            string.append(inputs[i])
            j -= 1
        i+= 1
        if j < 0 or j > 1: break
        
    if j == 1:
        string.append("$")
        while 1:
            if action(a) == "S":
                stack[a].append(string[0])
                string.pop(0)
            elif action(a) == "R":
                if stack[a-1][1] == "id":
                    stack.pop()
                    a -= 1
                    stack[a][1] = "F"
                elif stack[a-1][1] == "F":
                    if len(stack) > 3 and stack[a-2][1] == "*" and stack[a-3][1] == "T":
                        stack.pop()
                        stack.pop()
                        a -= 2
                    stack.pop()
                    a -= 1
                    stack[a][1] = "T"
                elif stack[a-1][1] == "T":
                    if len(stack) > 3 and stack[a-2][1] == "+" and stack[a-3][1] == "E":
                        stack.pop()
                        stack.pop()
                        a -= 2
                    stack.pop()
                    a -= 1
                    stack[a][1] = "E"
                elif stack[a-1][1] == ")" and stack[a-2][1] == "E" and stack[a-3][1] == "(":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    a -= 3
                    stack[a][1] = "F"
                else:
                    print("INVALID string entered. SYNTAX ERROR!")
                    break
            elif action(a) == "accept":
                print("VALID string entered. ACCEPTED!")
                break
            else:
                print("INVALID string entered. SYNTAX ERROR!")
                break
            stack.append([number(a)])
            a += 1
    else: print("INVALID string entered. SYNTAX ERROR!")