from function import display_month
input_number = input()
try:
    try:
        input_number = int(input_number)
    except:
        input_number = float(input_number)
except:
    input_number = str(input_number)
result = display_month(input_number)
print(result)
# choice = "y"
# while choice == "y":
#     input_number = input("Input number: ")
#     if input_number.isdigit():
#         input_number = int(input_number)
#     elif input_number.strip().lstrip("-").isdecimal():
#         input_number = float(input_number)
#     elif input_number.strip().lstrip("-").isdigit():
#         input_number = int(input_number)
#     elif input_number.strip().replace(".", "").isdigit():
#         input_number = float(input_number)
#     else:
#         input_number = str(input_number)
#     result = display_month(input_number)
#     print(result)
#     choice = input("Choice (y/n):")
