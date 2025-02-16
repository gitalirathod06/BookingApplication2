# multiple movie multiple booking plateform

def SingleTonclass(arg):
    L=[]
    def Inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return Inner

@SingleTonclass
class Movie1():
    def __init__(self):
        self.maxtic=100

    def Booking(self):
        print(f'Available ticket is {self.maxtic}')
        reqtic=int(input('enter the tickets:'))

        if reqtic<=self.maxtic:
            print('Ticket booked successfully...')
            self.maxtic-=reqtic
            
        else:
            print('ticket not available')
@SingleTonclass
class Movie2():
    def __init__(self):
        self.maxtic=200

    def Booking(self):
        print(f'Available ticket is {self.maxtic}')
        reqtic=int(input('enter the tickets:'))

        if reqtic<=self.maxtic:
            print('Ticket booked successfully...')
            self.maxtic-=reqtic
            
        else:
            print('ticket not available')

@SingleTonclass
class Movie3():
    def __init__(self):
        self.maxtic=300

    def Booking(self):
        print(f'Available ticket is {self.maxtic}')
        reqtic=int(input('enter the tickets:'))

        if reqtic<=self.maxtic:
            print('Ticket booked successfully...')
            self.maxtic-=reqtic
            
        else:
            print('ticket not available')


def BookMyShow():
    print('1]Movie1 \n2]Movie2 \n3]Movie3')
    option=int(input('Choose the movie:'))

    if option==1:
        user=Movie1()
        user.Booking()

    elif option==2:
        user=Movie2()
        user.Booking()

    elif option==3:
        user=Movie3()
        user.Booking()

    else:
        print('No movie available')


def PayTM():
    print('1]Movie1 \n2]Movie2 \n3]Movie3')
    option=int(input('Choose the movie:'))

    if option==1:
        user=Movie1()
        user.Booking()

    elif option==2:
        user=Movie2()
        user.Booking()

    elif option==3:
        user=Movie3()
        user.Booking()

    else:
        print('No movie available')


BookMyShow()
print('-------------')
PayTM()
print('-------------')
BookMyShow()
print('-------------')
PayTM()
print('-------------')
BookMyShow()
print('-------------')
PayTM()
print('-------------')

            
