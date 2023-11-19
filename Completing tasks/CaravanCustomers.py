def CustomerDetails():
    #inputs the name and ensures it is a string 
    forname=str(input("Enter your forname: "))
    while str.isalpha(forname)==False:
        forname=str(input("It can only include letters. Please try again: "))
    
    #inputs the name and ensures it is a string 
    surname=str(input("Enter your surname: "))
    while str.isalpha(surname)==False:
        surname=str(input("It can only include letters. Please try again: "))
    
    #inputs the age, ensures it is a number and the user has inputted a response
    while True:
        try:
            age=int(input("Enter your age: "))
        except ValueError:
            print("It must be a number")
        else:
            if age>120 and age<-1:
                print("You must enter a number")
            else:
                break
    #inputs the number, ensures the number is 11 digits long so it is equivalent to  the length of a phone number 
    while True:
        try:
            number=input("Enter your phone number: ")
        except ValueError:
            print("It must be a number: ")
        else:
            if len(number)!=11:
                print("Your number must be eleven digits long")
            else:
                break
    #ensures either male/female/other is the only response taken and ensuring no other response is accepted
    while True:
        gender=str(input("Enter your gender Male/Female/Other: ")).title()
        if gender not in ("Male","Female","Other"):
            print("Must be Male, Female or Other")
        else:
            if age=="":
                print("You must enter your age")
            else:
                break
            
        
    #opens the file and allows the customers details to be written in
    text_file=open("customerDetails.txt","a")
    #inputs the details into the text file
    text_file.write(str(forname))
    text_file.write("    ")
    text_file.write(str(surname))
    text_file.write("    ")
    text_file.write(str(age))
    text_file.write("    ")
    text_file.write(str(number))
    text_file.write("    ")
    text_file.write(str(gender))

    #open the file to append - if it's not there it'll be created

    fileObject = open("customerDetails.txt","a")

    # write to the file with a newline character at the end

    fileObject.write(nameSave + ageSave + numberSave + genderSave + "\n")
    fileObject.close()



#defining a search function to retrieve specified customer details from disc
def searching():
    search= input ('Please enter the firstname of the customer you would like to search for: ')
    file=open('customerDetails.txt', 'r')
    found='no'
    
    #python keeps reading the file until EOF
    while found=='no':
        recordVar=file.readline()
        
        #checks if the file is empty
        if recordVar=='': 
            file.close()
            print ('Customer not found')
            break
        #checks if search is in the recordVar and if so it outputs the information in the recordVar
        if search in recordVar: 
            print ('Information' , recordVar)
            found='yes'
            break
    
    #if the information is not found the program will output customer not found 
    if found!='yes':
        return ('Customer not found')

CustomerDetails()

searching()
