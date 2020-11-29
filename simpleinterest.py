#in this code we are going to calculate the interest of an amount
#for given principal amount, time and
#rate of interest

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is',t)
    print('The rate of interest is',r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si 

#Driver code
simple_interest(8,6,8)    



#now lets improve the code

#user input
def interest():
    principal = int(input('Please enter the principal amount:'))
    time = float(input('Please enter the time period:'))
    rate = float(input('Please enter the rate:'))
     
    #processing
    simpleinterest = (principal*time*rate)/100
    #output 
    print('The principal is:', principal)
    print('The time period is:', time)
    print('The rate of interest is', rate)
    print('This is the simple interest:', simpleinterest)


interest()
