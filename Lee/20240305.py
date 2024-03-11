http://59.23.132.191/30stair/leap_year/leap_year.php?pname=leap_year

def main():
  year = 2024
  #윤년 조건 4년에 한번, 100의 약수는 아니여야 하나 400의 약수는 윤년
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      return print("YES")
  else:
      return print("NO")


main()



http://59.23.132.191/30stair/pythagoras/pythagoras.php?pname=pythagoras

def main():
  c = 5
  #a² + b² = c²
  for a in range(1, c):
    for b in range(1, c):
      if a**2 + b**2 == c**2:
        return print(a, b)


main()



http://59.23.132.191/30stair/gcd_lcm/gcd_lcm.php?pname=gcd_lcm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)