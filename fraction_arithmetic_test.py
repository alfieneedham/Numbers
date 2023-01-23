from fraction_arithmetic import Fraction

def addition_test1():
    print ("Testing 1/2 + 1/4 = 3/4:")
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    result = f1.add(f2)
    if (result.num == 3) and (result.den == 4):
        return True
    else:
        return False
    
def subtraction_test1():
    print("Testing 22/6 - 5/7 = 62/21:")
    f1 = Fraction(22, 6)
    f2 = Fraction(5, 7)
    result = f1.sub(f2)
    if (result.num == 62) and (result.den == 21):
        return True
    else:
        return False
    
def multiplication_test1():
    print("Testing 5/7 * 35/5 = 5/1:")
    f1 = Fraction(5, 7)
    f2 = Fraction(35, 5)
    result = f1.mul(f2)
    if (result.num == 5) and (result.den == 1):
        return True
    else:
        return False
    
def division_test1():
    print ("Testing 31/7 / 2/9 = 279/14:")
    f1 = Fraction(31, 7)
    f2 = Fraction(2, 9)
    result = f1.div(f2)
    if (result.num == 279) and (result.den == 14):
        return True
    else:
        return False
    
def addition_test2():
    print ("Testing 1089/11 + 1840/5 = 467/1:")
    f1 = Fraction(1089, 11)
    f2 = Fraction(1840, 5)
    result = f1.add(f2)
    if (result.num == 467) and (result.den == 1):
        return True
    else:
        return False
    
def subtraction_test2():
    print ("Testing 72/2 - 182/13 = 22/1:")
    f1 = Fraction(72, 2)
    f2 = Fraction(182, 13)
    result = f1.sub(f2)
    if (result.num == 22) and (result.den == 1):
        return True
    else:
        return False
    
def multiplication_test2():
    print ("Testing 2808/36 * 35/160 = 273/16:")
    f1 = Fraction(2808, 36)
    f2 = Fraction(35, 160)
    result = f1.mul(f2)
    if (result.num == 273) and (result.den == 16):
        return True
    else:
        return False
    
def division_test2():
    print ("Testing 91/195 / 108/36 = 7/45:")
    f1 = Fraction(91, 195)
    f2 = Fraction(108, 36)
    result = f1.div(f2)
    if (result.num == 7) and (result.den == 45):
        return True
    else:
        return False
    
def addition_test3():
    print ("Testing 0/238 + 7/4 = 7/4:")
    f1 = Fraction(0, 238)
    f2 = Fraction(7, 4)
    result = f1.add(f2)
    if (result.num == 7) and (result.den == 4):
        return True
    else:
        return False
    
def subtraction_test3():
    print ("Testing 27/48 - 0/59 = 9/16:")
    f1 = Fraction(27, 48)
    f2 = Fraction(0, 59)
    result = f1.sub(f2)
    if (result.num == 9) and (result.den == 16):
        return True
    else:
        return False
    
def multiplication_test3():
    print ("Testing 0/278 * 275/36 = 0/1:")
    f1 = Fraction(0, 278)
    f2 = Fraction(275, 36)
    result = f1.mul(f2)
    if (result.num == 0) and (result.den == 1):
        return True
    else:
        return False
    
def division_test3():
    print ("Testing 37/9 / 0/37 = error:")
    f1 = Fraction(37, 9)
    f2 = Fraction(0, 37)
    result = f1.div(f2)
    if result!= None:
        return(False)
    else:
        return(True)
    
def addition_test4():
    print ("Testing 35/0 + 275/36 = error:")
    try:
        f1 = Fraction(35, 0)
        f2 = Fraction(275, 36)
        result = f1.add(f2)
        return(False)
    except:
        return(True)
    
def subtraction_test4():
    print ("Testing 278/13 - 48/0 = error:")
    try:
        f1 = Fraction(278, 13)
        f2 = Fraction(48, 0)
        result = f1.sub(f2)
        return(False)
    except:
        return(True)
    
def multiplication_test4():
    print ("Testing 48/0 * 7/2 = error:")
    try:
        f1 = Fraction(48, 0)
        f2 = Fraction(7, 2)
        result = f1.mul(f2)
        return(False)
    except:
        return(True)
    
def division_test4():
    print ("Testing 35/0 + 275/36 = error:")
    try:
        f1 = Fraction(12, 5)
        f2 = Fraction(37, 0)
        result = f1.div(f2)
        return(False)
    except:
        return(True)
    
def addition_test5():
    print ("Testing 33/-7 + -8/2 = -61/7:")
    f1 = Fraction(33, -7)
    f2 = Fraction(-8, 2)
    result = f1.add(f2)
    if (result.num == -61) and (result.den == 7):
        return True
    else:
        return False
    
def subtraction_test5():
    print ("Testing -47/-3 - -12/5 = 271/15:")
    f1 = Fraction(-47, -3)
    f2 = Fraction(-12, 5)
    result = f1.sub(f2)
    if (result.num == 271) and (result.den == 15):
        return True
    else:
        return False
    
def multiplication_test5():
    print ("Testing 6/-278 * 7/9 = -7/417:")
    f1 = Fraction(6, -278)
    f2 = Fraction(7, 9)
    result = f1.mul(f2)
    if (result.num == -7) and (result.den == 417):
        return True
    else:
        return False
    
def division_test5():
    print ("Testing -45/-49 / -278/-1078 = 495/139:")
    f1 = Fraction(-45, -49)
    f2 = Fraction(-278, -1078)
    result = f1.div(f2)
    if (result.num == 495) and (result.den == 139):
        return True
    else:
        return False
    
def equal_test1():
    print("Testing 5/9 == 45/81 is True:")
    f1 = Fraction(5, 9)
    f2 = Fraction(45, 81)
    if f1.find_if_equal(f2) == True:
        return(True)
    else:
        return(False)
    
def equal_test2():
    print("Testing 2/3 == 4/7 is False:")
    f1 = Fraction(2, 3)
    f2 = Fraction(4, 7)
    if f1.find_if_equal(f2) == False:
        return(True)
    else:
        return(False)
    
def equal_test3():
    print("Testing -7/-12 == 7/12 is True:")
    f1 = Fraction(-7, -12)
    f2 = Fraction(7, 12)
    if f1.find_if_equal(f2) == True:
        return(True)
    else:
        return(False)
    
def equal_test4():
    print("Testing 5/9 == 5/-9 is False:")
    f1 = Fraction(5, 9)
    f2 = Fraction(5, -9)
    if f1.find_if_equal(f2) == False:
        return(True)
    else:
        return(False)
    
def greater_than_test1():
    print("Testing 36/37 > 38/39 is False:")
    f1 = Fraction(36, 37)
    f2 = Fraction(38, 39)
    if f1.find_if_greater(f2) == False:
        return(True)
    else:
        return(False)
    
def greater_than_test2():
    print("Testing 36/37 > 38/-39 is True:")
    f1 = Fraction(36, 37)
    f2 = Fraction(38, -39)
    if f1.find_if_greater(f2) == True:
        return(True)
    else:
        return(False)

    
tests = [addition_test1, subtraction_test1, multiplication_test1, division_test1, addition_test2, subtraction_test2, multiplication_test2,
         addition_test3, subtraction_test3, multiplication_test3, division_test3, addition_test4, subtraction_test4, multiplication_test4, division_test4,
         addition_test5, subtraction_test5, multiplication_test5, division_test5, equal_test1, equal_test2, equal_test3, equal_test4,
         greater_than_test1, greater_than_test2]

for test in tests:
    if test():
        print("PASS")
    else:
        print("FAIL")