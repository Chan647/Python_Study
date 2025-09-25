'''
def mul(*values) :
    i = 1
    for value in values :
        i *= value
    return i
    
result = mul(5,7,9,10)
print(result)

def print_n_times(*values, n=2) :
    for i in range(n) : 
        for value in values :
            print(value)
        print()
    

print_n_times()

def test(a,b=10,c=20) :
    print(a+b+c)

test(10,20,30)
test(10,20)
test(a=20)
'''

