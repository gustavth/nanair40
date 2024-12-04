from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from baseClasses.Employee import Employee


validation = ValidationUI() 

class EmployeeUI(BaseUI):
    def addEmployee(self): # use employee base class
        userClass = Employee()

        fields = [
            ('kennitala', "Enter a kennitala: ", validation.validateKennitala),  # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter your name: ", validation.validateName),
            ('phone', "Enter a phonenumber: ", validation.validatePhone),
            ('homephone', "Enter a homephone: ", validation.validatePhone),
            ('country', "Enter a country: ", validation.validateCountry),
            ('email', "Enter your email: ", validation.validateEmail),
            ('address', "Enter your address: ", validation.validateAddress),
        ]

        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add employee',prompt, validationFunc, userClass.__dict__)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            userClass.__dict__[key] = value


        # Here a instance would get created in order to send to data layer
        new_employee = Employee(userClass.__dict__['kennitala'], userClass.__dict__['name'], userClass.__dict__['phone'], userClass.__dict__['homephone'], userClass.__dict__['location'], userClass.__dict__['email'], userClass.__dict__['address'])


        while True:
            self.printBaseMenu('Add employee', [f'{key}: {value}' for key, value in userClass.__dict__.items()], 'Choose an option: ') # if the user finished entering all the information needed then he gets to choose either to quit or go back
            optionInput, isValid = self.takeInput(['[B]ack', '[Q]uit'])

            if isValid:
                match optionInput.lower():
                    case 'b':
                        return False
                    case 'q':
                        return 'q'



    def showEmployee(self):
    
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        lookUpKennitala = self.getValidInput( 'View/edit employee',"Look up employee by kennitala: ", validation.validateKennitala)

        match lookUpKennitala.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with the kennitala entered 


    def editEmployee():
        pass
        



       
        
    def showEmployees(self):
        pass
        # Here we need to call showEmployees in the wrapper to get all of the employees in the system


        

    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        


