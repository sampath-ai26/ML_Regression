class multifunc():
    def Subfields():
        print("Sub-fields in AI are: ")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("NLP")

    def OddEven():
        num= int(input("Enter a number"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num, "is Odd number")
            
    def Elegible():
        gender=input("Your Gender: ")
        age= int(input("Your Age :"))
        if ( gender.lower() == 'male' and age > 20 ):
            print( "Elegible")
        elif ( gender.lower() =='female' and age >17 ):
            print ("Elegible")
        else:
            print( 'NOT ELIGIBLE')
            
