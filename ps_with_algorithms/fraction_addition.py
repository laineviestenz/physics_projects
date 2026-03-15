class fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other_fraction):
        """add the fractions by simplest method of common denominator, return
        unsimplified result"""
        new_numerator = self.numerator * other_fraction.denominator
        other_numerator = self.denominator * other_fraction.numerator
        common_denominator = self.denominator * other_fraction.denominator
        
        return ((new_numerator + other_numerator), common_denominator)
    
    def simplify(self, other_fraction):
        pass

a = fraction(3, 4)
b = fraction(1, 8)

print(a.add(b))



