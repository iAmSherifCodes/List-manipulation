def largest_num(x):
    lm = x[0]
    for i in  x:
        if i > lm:
            lm = i
    return lm

def lowest_num(x):
    lw = x[0]
    for i in x:
        if i < lw:
            lw = i
    return lw

def reverse_list(x):
    rl =[]
    for i in range(len(x)):
        rl.insert(0,x[i])
    return rl

def search_element(e, x):
    if e in x:
        return True
    else:
        return False
    
def odd_position(x):
    rl = []
    for i in range(0,len(x),2):
        rl.append(x[i])
    return rl

def even_position(x):
    rl = []
    for i in range(1,len(x), 2):
        rl.append(x[i])
    return rl

def list_total(x):
    result = 0
    for i in x:
        result += i
    return result

def string_palindrome(strings):
    # string_list = strings.split()
    r = False
    
    s1 = list(strings)
    rv =[]
    for i in range(len(s1)):
        rv.insert(0,s1[i])
    for i in range(len(s1)):
        if s1[i] == rv[i]:
            r = True
        else:
            r = False
            break
    return r

def forloop_sum(x):
    sum =0
    for i in x:
        sum += i
    return sum

def whileloop_sum(x):
    sum = 0
    count = 0
    while count < len(x):
        sum += x[count]
        count += 1
    return sum

def dowhileloop_sum(x):
    count = 0
    sum = 0
    b = count < len(x)
    while b:
        sum += x[count]
        count +=1
        if count == len(x):
            break
    return sum

def list_concatenate(x1,x2):
    x1.extend(x2)
    return x1

def element_list_concatenation(x1,x2):
    cl = []
    for i in range(len(x1)):
        cl.append(x1[i])
        cl.append(x2[i])
    return cl

def list_of_digits(num):
    nl = str(num)
    l =[]
    for i in nl:
        l.append(i)
    return l