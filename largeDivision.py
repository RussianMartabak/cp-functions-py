x = 900000000000000694
print(x)
# this for dealing with a number 10^18 and up in python
# for example given x it will return the result in an integer
def largeDivision(n, divider):
    num = str(n)
    
    p1m = 1000000000 # same as add 9 zeroes
    
    p1 = int(num[0:9]) # leading 9 numbers
    

    p1div = int((p1 / 2) * p1m)
    print(p1div)
    p1div = str(p1div)
    p2 = int(num[9:len(num)]) # trailing 9 
    p2div = str(int(p2 / 2))
    # insert p2div backward to the p1div number
    out = ''
    for i in range(len(p1div) - len(p2div)):
        out += p1div[i]
    for k in range(len(p2div)):
        out += p2div[k]
    return int(out)

print(largeDivision(x, 2))