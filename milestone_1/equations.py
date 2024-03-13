import math

print("Please enter an equation as a string of the form: `<a>x^2 + <b>x + <c> = 0`")
s = input()
s = s.replace(" ", "")
escape_chars = "x()+"
a = int(s[: s.find("+")].replace("x^2", "").strip(escape_chars))
b = int(s[s.find("+") : s.rfind("+")].strip(escape_chars))
c = int(s[s.rfind("+") : s.find("=")].strip(escape_chars))

print(f"a = {a}\nb = {b}\nc = {c}")

x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print(f"x1 = {x1} x2 = {x2}")
