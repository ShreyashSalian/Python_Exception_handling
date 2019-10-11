class OddNumberException(Exception):
    def __init__(self,*args):
        self.args = args

class EvenNumberException(Exception):
    def __init__(self,*args):
        self.args = args

try:
    n = int(input("Enter a Number to check whether he number is odd or even : "))
    if n % 2 == 0:
        raise EvenNumberException("%d is a Even Number!!."%n)

    else:
        raise OddNumberException("%d is a Odd Number!!."%n)

except EvenNumberException as r:
    print(r)

except OddNumberException as r:
    print(r)
