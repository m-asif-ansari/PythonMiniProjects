def calculator():
  print('Enter the number corresponding to the operation you have to perform')
  print("Add: 1")
  print("Subtraction: 2")
  print("Multiplication: 3")
  print("division: 4")

  ch = int(input())
  if ch >= 5:
    print("enter only 1,2,3,4")
    return
  print("Enter 1st number")
  a = int(input())
  print("Enter 2nd number")
  b = int(input())
  if ch == 1:
    print('Result',a + b)
  elif ch == 2:
    print('Result',a - b)
  elif ch == 3:
    print('Result',a * b)
  elif ch == 4:
    print('Result',a / b)
  


def main():
  print('Welcome to PyCalculator')
  ch = 'y'
  while ch.lower() == 'y':
    calculator()

    ch = input('Do you want to do more operations (y/n)')
  print()
  print('Exiting!!')
  print('Thanks for using PyCalculator')

if __name__ == '__main__':
  main()
