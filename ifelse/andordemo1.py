cardNo =20 # must be > 0
exp= 2024 # must be > 2020
cvv = 19 # must be >0
otp = 1235 # must be 1234

if(cardNo> 0 and exp> 2020 and cvv> 0) or otp == 1234:
    print("Valid card")

else:
    print("Invalid card")    