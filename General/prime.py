from math import sqrt
class Prime:

    def __init__(self,number):
        self.number = number
    
    def isNumPrime(self):
        flag = 0
        if num > 1:
            for j in range(2,int(sqrt(num))+1):
                if num % j == 0:
                    flag = 1
                break
            if  flag == 0 :
                print(num,"is a prime")
            else:
                print(num,"is not prime")

        else:
            print(num,"is not prime")

num = 2

check_prime = Prime(num)
check_prime.isNumPrime()