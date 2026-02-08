# total_cash=500000
# while total_cash>=0:
#     name_of_applicant=str(input("Please enter your name:"))
#     age_of_applicant=int(input("Please enter your age:"))
#     salary_of_applicant=int(input("Please enter your salary:"))
#     loan_amount=0
#     remaining_cash = total_cash
#     if 21 <= age_of_applicant <= 50:
#         if salary_of_applicant >=50000:
#             print("You are eligible for a loan")
#             loan_amount = int(input("Please enter the required amount:"))
#             if loan_amount<=remaining_cash:
#                 print("Transaction Successful")
#                 remaining_cash=total_cash-loan_amount
#             else:
#                 loan_amount=int(input("Please enter a lower amount"))
#                 remaining_cash=total_cash-loan_amount
#         else:
#             print("Sorry you are inegligible for a loan")
#     else:
#             print("Sorry you are inegligible for a loan")

my_list=[1,2,3,4,5,6]

my_list[4]=3
print(my_list)
id(my_list)
print(id(my_list))
