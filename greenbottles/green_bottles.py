

def song(n):
    print (str(n) + " green bottles sitting on the wall, " + str(n) + " green bottles sitting on the wall,")
    print("And if one green bottle should accidentally fall, there'll be " + str(n-1) + " green bottles sitting on the wall")
    print (" ")


green_bottles =  10 


while green_bottles>0:
    song(green_bottles)
    green_bottles -=1

        
