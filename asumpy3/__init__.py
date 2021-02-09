class asumpy3:
        
    def angA():
        angb = int(input(("Please tell me the value of Angle B>>")))
        angc = int(input(("Please tell me the value of Angle C>>")))
        anga = 180 - (angb + angc)

        #To figure out if the provided angles form a valid triangle(all 3 possibilities have same provision)  
        if (anga + angb + angc) == 180 and anga>0 : 
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle A = 180 - (Angle B + Angle C)")
            print("Angle A = 180 - " "(" ,angb, " + ",angc, ")") 
            print ("Angle A = 180 -" ,(angb+angc), )
            print("Angle A =" ,(180- (angb+angc)))
            print("The value of Angle a is>> ", anga, " Degrees")

                
        elif (anga + angb + angc) != 180 or anga<=0:   
            print ("This triangle is not valid")

    def angB():
        anga = int(input(("Please tell me the value of Angle A>> ")))
        angb = int(input(("Please tell me the value of Angle B>> ")))
        angc = 180 - (anga + angb)

        if (anga + angb + angc) == 180 and angc>0 :
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle C = 180 - (Angle A + Angle B)")
            print("Angle C = 180 - " "(" ,anga, " + ",angb, ")") 
            print ("Angle C = 180 -" ,(anga+angb), )
            print("Angle C =" ,(180- (anga+angb)))
            print("The value of Angle c is>> ", angc, " Degrees")

                
        elif (anga + angb + angc) != 180 or angb<=0:   
            print ("This triangle is not valid")

    def angC():
        anga = int(input(("Please tell me the value of Angle A>> ")))
        angb = int(input(("Please tell me the value of Angle B>> ")))
        angc = 180 - (anga + angb)

        if (anga + angb + angc) == 180 and angc>0 :
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle C = 180 - (Angle A + Angle B)")
            print("Angle C = 180 - " "(" ,anga, " + ",angb, ")") 
            print ("Angle C = 180 -" ,(anga+angb), )
            print("Angle C =" ,(180- (anga+angb)))
            print("The value of Angle c is>> ", angc, " Degrees")

                
        elif (anga + angb + angc) != 180 or angb<=0:   
            print ("This triangle is not valid")
