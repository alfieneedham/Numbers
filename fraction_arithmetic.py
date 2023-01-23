from math import gcd

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
        if self.den == 0:
            print("Divide by zero error.")
            print(str(1/0)) 
        if (self.den) < 0:
            self.num *= -1
            self.den *= -1
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
        if newDen == 0:
            print("Divide by zero error.")
        else:
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

if __name__ == "__main__":

    fractionA = Fraction(33, -7)
    fractionB = Fraction(-8, 2)
    print("Fraction A simplified:")
    fractionA.print_fraction()
    print("Fraction B simplified:")
    fractionB.print_fraction()
    print("Add:")
    fractionA.add(fractionB).print_fraction()
    print("Sub:")
    fractionA.sub(fractionB).print_fraction()
    print("Mul:")
    fractionA.mul(fractionB).print_fraction()
    print("Div:")
    fractionA.div(fractionB).print_fraction()
    print("Equal?")
    print(fractionA.find_if_equal(fractionB))
    print ("A > B?")
    print(fractionA.find_if_greater(fractionB))