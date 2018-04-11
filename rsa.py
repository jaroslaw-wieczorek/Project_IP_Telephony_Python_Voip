class Encrypt:

    def get_d(self, e, m):
        """Takes encoding number, 'e' and the value for 'm' (p-1) * (q-1).
        Returns a decoding number."""
        x = lasty = 0
        lastx = y = 1
        while m != 0:
            q = e // m
            e, m = m, e % m
            x, lastx = lastx - q * x, x
            y, lasty = lasty - q * y, y
        return lastx

    def get_e(self, m):
        """Finds an e coprime with m."""
        e = 2
        while self.gcd(e, m) != 1:
            e += 1
        return e

    def gcd(self, a, b):
        """Euclid's Algorithm: Takes two integers and returns gcd."""
        while b > 0:
            a, b = b, a % b
        return a

    def __init__(self, value):
        self.toEncrypt = value

    def setVars(self):
        p = int(input("p: "))
        q = int(input("q: "))
        n = p * q
        m = (p - 1) * (q - 1)
        e = self.get_e(m)
        print("N = ", n, "\ne = ", e)
        d = self.get_d(e, m)
        while (d < 0):
            d += m
        return [n, e, d]