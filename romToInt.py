class Converter():
    def __init__(self):
        self.numerals = {"I": 1, "IV": 4, "V":5, "IX": 9, "X": 10,
                         "XL": 40, "L": 50, "XC": 90, "C": 100,
                         "CD":400, "D": 500, "CM": 900, "M":1000}
        self.sum = 0
    def romToInt(self, s):
         i = 0
         while i < len(s):
             if i != len(s)-1 and s[i] + s[i+1] in self.numerals.keys() :
                 self.sum += self.numerals[s[i]+s[i+1]]
                 i += 2
             else:
                 self.sum += self.numerals[s[i]]
                 i += 1
         return self.sum

n = 'MCMX'
print(Converter().romToInt(n))
print(Converter().romToInt("MMXX"))
print(Converter().romToInt("MCMLXIX"))
print(Converter().romToInt("CDXX"))
print(Converter().romToInt("XCVI"))

