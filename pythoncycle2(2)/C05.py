#Input string from given string where first and last characters exchanged
def change(str):
      return str[-1:] + str[1:-1] + str[:1]
str=input("Enter the string: ")
print("Modified string: ",change(str))
