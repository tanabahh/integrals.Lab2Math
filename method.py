from functions import f, z, g, c, s, q


class LeftRectangles:
    def __init__(self, f, a, b, e):
        self.f = f
        self.a = a
        self.b = b
        self.e = e

    def check_params(self):
        if (self.f == z) or (self.f == c):
            return self.a >= 0
        else:
            return True

    def iteration(self, n):
        h = (self.b - self.a) / float(n)
        total = 0
        for k in range(0, n):
            if ((self.f == g) or (self.f == q)) and ((self.a + (k * h)) == 0):
                total += (self.f(pow(1, -10)) + self.f(- pow(1, -10)))/2
            elif (self.f == c) and ((self.a + (k * h)) == 0):
                total += self.f(pow(1, -10)) / 2
            else:
                total += self.f((self.a + (k * h)))
        result = h * total
        return result

    def get_answer_and_count(self):
        check = self.check_params()
        if check:
            n = 1
            int1 = self.iteration(n)
            n *= 2
            int2 = self.iteration(n)
            while (abs(int1 - int2)/3 > self.e) and (n < 4000000):
                int1 = int2
                n *= 2
                int2 = self.iteration(n)
            return [int2, n, abs(int1-int2)/3]
        else:
            return False


class RightRectangles:
    def __init__(self, f, a, b, e):
        self.f = f
        self.a = a
        self.b = b
        self.e = e

    def check_params(self):
        if (self.f == z) or (self.f == c):
            return self.a >= 0
        else:
            return True

    def iteration(self, n):
        h = (self.b - self.a) / float(n)
        total = 0
        for k in range(1, n):
            if ((self.f == g) or (self.f == q)) and ((self.a + (k * h)) == 0):
                total += (self.f(pow(1, -10)) + self.f(- pow(1, -10)))/2
            elif (self.f == c) and ((self.a + (k * h)) == 0):
                total += self.f(pow(1, -10)) / 2
            else:
                total += self.f((self.a + (k * h)))
        result = h * total
        return result

    def get_answer_and_count(self):
        check = self.check_params()
        if check:
            n = 1
            int1 = self.iteration(n)
            n *= 2
            int2 = self.iteration(n)
            while (abs(int1 - int2)/3 > self.e) and (n < 4000000):
                int1 = int2
                n *= 2
                int2 = self.iteration(n)
            return [int2, n, abs(int1-int2)/3]
        else:
            return False


class CenterRectangles:
    def __init__(self, f, a, b, e):
        self.f = f
        self.a = a
        self.b = b
        self.e = e

    def check_params(self):
        if (self.f == z) or (self.f == c):
            return self.a >= 0
        else:
            return True

    def iteration(self, n):
        h = (self.b - self.a) / float(n)
        total = 0
        for k in range(0, n+1):
            if ((self.f == g) or (self.f == q))and (((self.a + (k * h)) + h / 2) == 0):
                total += (self.f(pow(1, -10)) + self.f(- pow(1, -10)))/2
            elif (self.f == c) and (((self.a + (k * h)) + h / 2) == 0):
                total += self.f(pow(1, -10)) / 2
            else:
                total += self.f((self.a + (k * h)) + h / 2)
        result = h * total
        return result

    def get_answer_and_count(self):
        check = self.check_params()
        if check:
            n = 1
            int1 = self.iteration(n)
            n *= 2
            int2 = self.iteration(n)
            while (abs(int1 - int2)/3 > self.e) and (n < 4000000):
                int1 = int2
                n *= 2
                int2 = self.iteration(n)
            return [int2, n, abs(int1-int2)/3]
        else:
            return False

