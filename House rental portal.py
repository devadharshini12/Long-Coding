#import json
users = []
PaymentDetails = [] #details
HouseList = []
CustomerHistory = []


class HouserentingPortal:

    def __init__(self, userId: int, Name: str, Email: str, Password: str, Role: str):
        self.userid = userId
        self.name = Name
        self.email = Email
        self. password = Password
        self.role = Role

    def hardcode(self):
        users.append(self)
        return users

    def validatelogin(self, email, passwrod):
        for user in users:
            if user.email == email and user.password == Password:
                return user
            else:
                return False
        return None
    

class Admin:

    def __init__(self, userId: int, Name: str, Email: str, Password: str, Role: str):
        self.userid = userId
        self.name = Name
        self.email = Email
        self. password = Password
        self.role = Role

    def hardcode(self):
        users.append(self)
        return users

    def validatelogin(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
            else:
                return False
        return None
    

class House:

    def __init__(self, HouseId, Locality, City, Type, Squarefeet, Rent):
        
        self.houseid = HouseId
        self.locality = Locality
        self.city = City
        self.type = Type
        self.squarefeet = Squarefeet
        self.rent = Rent


class Advertisement(House):
    
    def __init__(self, id, Name, Email, Password, Role):
        super(). __init__( id, Name, Email, Password, Role);


class Payment:
    
    def __init__(self, PaymentId, PaymentMothod, CardNo, Month, Year, CVV, Amount, PaymentStatu = 'not paid'):
        self.paymentId = PaymentId
        self.paymentmethod = PaymentMethod
        self.cardno = CardNo
        self.Month = Month
        self.year = Year
        self.CVV = CVV
        
        
        

    def hardcode(self):
        PaymentDetails.append(self)


class AdminReport(Payment,HouserentingPortal):
    
    def __init(self, userId, Name, Email, Password, Role):
        super().__init__(userId, Name, Email, Password, Role);


class housedetails(HouserentingPortal):

    def __init__self(self, userId, Name, Email, Password, Role):
        super().__init__(userId, Name, Email, Password, Role);

    def HouseCustomer(self):
        house1 = House(1, 'Kodambakkam', 'Chennai', '2BHK', '798', '6000')
        house2 = House(2, 'Goripalayam', 'Madurai', '1BHK', '560', '5500')
        house3 = House(3, 'Anna nagar', 'Chennai', '3BHK', '1200', '15000')
        HouseList.append(house1)
        HouseList.append(house2)
        HouseList.append(house3)

        CustomerWanted = True
        while(CustomerWanted):
            print("House details")
            print("1. Advertisement of Houses")
            print("2. Do the Payment")
            print("3. History of Bookings")
            print("4. Logout")
            Choice = int(input("Enter your Choice: "))

            if Choice == 1:

                lists = HouseList
                while(lists!=[]):
                    i_tem = lists.pop()
                    #HouseId, Locality, City, Type, Squarefeet, Rent
                    print(i_tem.houseid)
                    print(i_tem.locality)
                    print(i_tem.city)
                    print(i_tem.type)
                    print(i_tem.squarefeet)
                    print(i_tem.rent)
                    print('*******************************************')


            if Choice == 2:
                PaymentId = len(PaymentDetails)
                PaymentMethod = input('Enter you method of Payment: ')
                if(PaymentMethod == 'card'):
                    CardNo = input('Card Number: ')
                    Month = input('Month: ')
                    Year = input('Year: ')
                    CVV = input('CVV: ')
                    HouseYouWant = int(input('Enter the House You want: '))
                    if(HouseYouWant == 1):
                        print('You need to pay 6000')
                        print("*********PAYMENT SUCCESSFULL***********")
                    elif(HouseYouWant == 2):
                        print('You need to pay 5500')
                        print("*********PAYMENT SUCCESSFULL***********")
                    elif(HouseYouWant == 3):
                        print('You need to pay 15000')
                        print("*********PAYMENT SUCCESSFULL***********")
                    else:
                        print('INVALID HOUSE')
                        
                    

                elif(PaymentMethod == 'cash'):
                    HouseYouWant = int(input('Enter the House You want: '))
                    if(HouseYouWant == 1):
                        print('You need to pay 6000')
                        print("*******PAY CASH********")
                    elif(HouseYouWant == 2):
                        print('You need to pay 5500')
                        print("*******PAY CASH********")
                    elif(HouseYouWant == 3):
                        print('You need to pay 15000')
                        print("*******PAY CASH********")
                    else:
                        print('Invalid House')
                    

            if Choice == 3:
                temporaryBokingList = PaymentDetails
                while (temporaryBokingList != []):
                    print(temporaryBokingList.pop())

            if Choice == 4:
                print("*********YOU HAVE BEEN LOGGED OUT SUCCESSFULLY*********")
                return False


if __name__ == "__main__":
    
    Portal = HouserentingPortal(1, "Lucifer", "lucifer@gmail.com", "lucifer12", "Owner")
    Portal.hardcode()
    Portal = HouserentingPortal(2, "Peter Parker", "peterparker@gmail.com", "peter12", "Customer")
    Portal.hardcode()
    Portal = HouserentingPortal(3, "Tony Stark", "tonys@gmail.com", "tony12", "Admin")
    Portal.hardcode()
                    
    Portal = Admin(1, "Lucifer", "lucifer@gmail.com", "lucifer12", "Owner")
    Portal.hardcode()
    Portal = Admin(2, "Peter Parker", "peterparker@gmail.com", "peter12", "Customer")
    Portal.hardcode()
    Portal = Admin(3, "Tony Stark", "tonys@gmail.com", "tony12", "Admin")
    Portal.hardcode()
                                 

    Role = input('Enter your Role: ')
    if Role == 'Customer':
        print("*************WELCOME PETER**********")
        LoginUser = Portal.validatelogin("lucifer@gmail.com", "lucifer12")
        if LoginUser:
            HouseWork = housedetails(LoginUser.userid, LoginUser.name, LoginUser.email, LoginUser.password, LoginUser.role)
            HouseWork.HouseCustomer()

    if Role == 'Owner':
        print("*************WELCOME LUCIFER**********")
        LoginUser = Portal.validatelogin("lucifer@gmail.com", "lucifer12")
        if LoginUser:
            HouseWork = housedetails(LoginUser.userid, LoginUser.name, LoginUser.email, LoginUser.password, LoginUser.role)
            HouseWork.HouseCustomer()
                


         















        
