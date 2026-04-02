Subjects=["I","We"]
Verb=["play","watch"]
sports=list(map(str,input("Enter the sports :").split(' ')))
for subject in Subjects:
    for sport in sports:
        for verb in Verb:
            print(subject,verb,sport)