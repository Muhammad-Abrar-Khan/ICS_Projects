def project():
      print('''\n Write symbols as input(S) so that you can perform your desirable operations:
      * for Multiplication
      / for Division
      + for Addition
      - for Subtraction
      ** for Power
      % for Remainder
      x for Multiplication Table
      i for Even or odd number
      p for Prime number''')

      s = input("\nEnter your choice : ")

      if s == 'x':
            a=int(input("Enter a number : "))
            if s == 'x':
                print(f"\nMultiplication Table of {a} is:")
                i=0
                for i in range(1,11):
                    print(f"{a}*{i}={a * i}")

      elif s == 'p':
          a = int(input("enter a number : "))
          prime = True
          for i in range(2, a):
            if (a % i == 0):
                prime = False
                break

          if prime:
            print("Yes it is a prime number !")
          else:
            print("No it is not a prime number")

      elif s == 'i':
          a=int(input("Enter a number : "))
          r=a%2
          if r == 0:
              print("It is an Even number ")
          else:
              print("It is an Odd number")

      else:

          a = int(input("Enter a number : "))
          b = int(input("Enter a number : "))
          if s =='*':
            print(f"{a}*{b}={a*b}")

          elif s =='/':
            print(f"{a}/{b}={a/b}")

          elif s =='+':
            print(f"{a}+{b}={a+b}")

          elif s == '-':
            if a>b:
                print(f"{a}-{b}={a - b}")
            elif a<b:
                print(f"{a}-{b}={a - b}")

          elif s == '**':
            print(f"{a}**{b}={a ** b}")

          elif s == '%':
            print(f"{a}%{b}={a % b}")

      again()

def again():
      calculate_again=input("\nDo you want to calculate again?\nType y for yes & n for no :\n")
      if calculate_again == "y":
            project()
      elif calculate_again == "n":
            print("\nThank you for using this code!")

project()













