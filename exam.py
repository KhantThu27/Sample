x = int(input("Please Enter exam result:"))


if x >= 90 and x <= 100:
	print("A")
elif x >= 80 and x < 90:
	print("B")
elif x >= 60 and x < 80:
	print("C")
elif x >= 50 and x < 60:
	print("D")
elif x < 50 and x > 0:
	print("F")
else:
	print("Check Again")
