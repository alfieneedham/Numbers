from math import gcd

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.__simplify()



    def add(self, otherFraction):
        newNum = self.num + otherFraction.num
        newDen = self.den + otherFraction.den
        
        answer = Fraction(newNum, newDen)

    
    def sub(self, otherFraction):
        newNum = self.num - otherFraction.num
        newDen = self.den - otherFraction.den
        return(newNum, newDen)
    


    def mul(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        answerFraction = Fraction(newNum, newDen)
    
    def div(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        answerFraction = Fraction(newNum, newDen)

    def __simplify(self):
        commonDen = gcd(self.num, self.den)
        self.num /= commonDen
        self.den /= commonDen

    def print_fraction(self):
        print(str(int(self.num)) + "/" + str(int(self.den)))

fractionA = Fraction(5, 7)
fractionB = Fraction(6, 14)
fractionA.print_fraction()
fractionB.print_fraction()
fractionA.mul(fractionB)
answerFraction.print_fraction()

# * add equal, greater, lesser as bool