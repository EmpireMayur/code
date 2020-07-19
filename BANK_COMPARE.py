import math
t=int(input("m=no. of test cases:"))
for i in range(t):
    loan_amount=int(input("enter amount"))
    year=int(input("years"))
    bank_sum=[0]*2
    bank_sum[0]=0
    bank_sum[1]=0

    for i in range(2):
        num_slab=int(input("no. of slabs"))

        for j in range(num_slab) :
            num_years=int(input("years"))
            monthly_rate=float(input("rate"))

            nr=loan_amount*monthly_rate
            dr=1-1/math.pow((1+monthly_rate),12*num_years)

            current_sum=nr/dr

            bank_sum[i]+=current_sum


    if bank_sum[0]<bank_sum[1]:
        print("BANK A")
    else:
        print("BANK B")



