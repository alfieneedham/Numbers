from math import gcd

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.__simplify()

    def add(self, otherFraction):
        newNum = (self.num * otherFraction.den) + (otherFraction.num * self.den)
        newDen = self.den * otherFraction.den
        answerFraction = Fraction(newNum, newDen)
        return(answerFraction)

    def sub(self, otherFraction):
        newNum = (self.num * otherFraction.den) - (otherFraction.num * self.den)
        newDen = self.den * otherFraction.den
        answerFraction = Fraction(newNum, newDen)
        return(answerFraction)
    
    def mul(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        answerFraction = Fraction(newNum, newDen)
        return(answerFraction)
    
    def div(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        answerFraction = Fraction(newNum, newDen)
        return(answerFraction)

    def __simplify(self):
        commonDen = gcd(int(self.num), int(self.den))
        self.num /= commonDen
        self.den /= commonDen

    def print_fraction(self):
        print(str(int(self.num)) + "/" + str(int(self.den)))
        
    def find_if_equal(self, otherFraction):
        # * This is unnecessary as fractions are simplified anyway, but this method would be necessary if they were not simplified. Returns True if equal, False otherwise.
        if (self.num * otherFraction.den) == (otherFraction.num * self.den):
            return(True)
        else:
            return(False)
        
    def find_if_greater(self, otherFraction):
        # * If fractionA is greater than fractionB, it returns True. Otherwise, it returns false, indicating that it is lesser than fractionB.
        if (self.num * otherFraction.den) > (otherFraction.num * self.den):
            return(True)
        else:
            return(False)

numFractionA = int(input("Enter numerator of fractionA: "))
denFractionA = int(input("Enter denominator of fractionA: "))
numFractionB = int(input("Enter numerator of fractionB: "))
denFractionB = int(input("Enter denominator of fractionB: "))

fractionA = Fraction(numFractionA, denFractionA)
fractionB = Fraction(numFractionB, denFractionB)
fractionA.print_fraction()
fractionB.print_fraction()
fractionA.add(fractionB).print_fraction()
fractionA.sub(fractionB).print_fraction()
fractionA.mul(fractionB).print_fraction()
fractionA.div(fractionB).print_fraction()
print(fractionA.find_if_equal(fractionB))
print(fractionA.find_if_greater(fractionB))