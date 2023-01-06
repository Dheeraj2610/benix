
decimal = 150
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")

   """ def decimal_to_octal(decimal_number):
  octal_number = ""
  while decimal_number > 0:
    octal_number = str(decimal_number % 8) + octal_number
    decimal_number = decimal_number // 8
  return octal_number
decimal_number = 10
print(f"Octal representation of {decimal_number}: {decimal_to_octal(decimal_number)}")
