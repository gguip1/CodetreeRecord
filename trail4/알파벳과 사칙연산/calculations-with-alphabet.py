expression = input()

# Please write your code here.
kind = [0] * 6

answer = -1

def calc():
    v = 0
    o = ''
    for n in range(len(expression)):
        if n == 0:
            match expression[n]:
                case 'a':
                    v = kind[0]
                case 'b':
                    v = kind[1]
                case 'c':
                    v = kind[2]
                case 'd':
                    v = kind[3]
                case 'e':
                    v = kind[4]
                case 'f':
                    v = kind[5]
        else: 
            match expression[n]:
                case 'a':
                    match o:
                        case '+':
                            v += kind[0]
                        case '-':
                            v -= kind[0]
                        case '*':
                            v *= kind[0]
                case 'b':
                    match o:
                        case '+':
                            v += kind[1]
                        case '-':
                            v -= kind[1]
                        case '*':
                            v *= kind[1]
                case 'c':
                    match o:
                        case '+':
                            v += kind[2]
                        case '-':
                            v -= kind[2]
                        case '*':
                            v *= kind[2]
                case 'd':
                    match o:
                        case '+':
                            v += kind[3]
                        case '-':
                            v -= kind[3]
                        case '*':
                            v *= kind[3]
                case 'e':
                    match o:
                        case '+':
                            v += kind[4]
                        case '-':
                            v -= kind[4]
                        case '*':
                            v *= kind[4]
                case 'f':
                    match o:
                        case '+':
                            v += kind[5]
                        case '-':
                            v -= kind[5]
                        case '*':
                            v *= kind[5]
                case '+':
                    o = '+'
                case '-':
                    o = '-'
                case '*':
                    o = '*'
    return v

def backtracking(cnt:int):
    global answer
    if cnt == 6:
        answer = max(answer, calc())
        return

    for v in range(1, 5):
        kind[cnt] = v
        backtracking(cnt + 1)

backtracking(0)
print(answer)