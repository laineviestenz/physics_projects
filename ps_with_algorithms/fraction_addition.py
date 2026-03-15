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
        
        return fraction((new_numerator + other_numerator), common_denominator)
    
    def get_gcd(self):
        """Assumes we have two fractions: a/m and b/n"""
        """Euclid's algorithm courtesy PSwAaDSUP"""
        m = self.denominator
        n = self.numerator
    
        while m % n != 0: #while remainder not zero
            old_m = m
            old_n = n

            m = old_n
            n = old_m%old_n
        return n

    def simplify(self):
        gcd = fraction.get_gcd(self)
        new_numerator = self.numerator / gcd
        new_denominator = self.denominator / gcd
        return fraction(new_numerator, new_denominator)
    
    def show(self):
        print(str(self.numerator) + '/' + str(self.denominator))

a = fraction(3, 4)
b = fraction(1, 8)

c = fraction.add(a, b)
fraction.show(c)

fraction.show(c.simplify())
