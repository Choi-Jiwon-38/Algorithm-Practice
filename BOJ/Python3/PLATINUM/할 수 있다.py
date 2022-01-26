signal = False

try:
    str = input()
    str = str.replace('/', '//')

    if signal == False and str[0] == '(':
        if str[1] == '+' or str[1] == '-' or str[1] == '//' or str[1] == '*':
            answer = 'ROCK'
            signal = True
        else:
            answer = eval(str)
    else:
        if str[0] == '+' or str[0] == '-' or str[0] == '//' or str[0] == '*':
            answer = 'ROCK'
            signal = True
        else:
            answer = eval(str)

    if signal == False:
        for i in range(len(str)):
            if i+1 <= len(str) - 1:
                if (str[i] == '+' or str[i] == '-' or str[i] == '//' or str[i] == '*') and (str[i+1] == '+' or str[i+1] == '-' or str[i+1] == '//' or str[i+1] == '*'):
                    answer = 'ROCK'
                    signal = True
                    break
                else:
                    answer = eval(str)
                
    if signal == False and '()' in str:
        answer = 'ROCK'
    
    if signal == False:
        for i in range(len(str)):
            if str[i] == '/':
                if str[i+2] == '+' or str[i+2] == '-' or str[i+2] == '*':
                    answer = 'ROCK'

except:
    answer = 'ROCK'

print(answer)