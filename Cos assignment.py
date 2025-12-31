status = int(input("Enter filing status (single=0, married separate=1, married jointly/qualifying widow(er)=2, head=3): "))
income = float(input("Enter taxable income:  $"))

print("Status:", status)
print("Income:", income)

tax = 0
#single
if status == 0:
	if income <= 8350:
		tax = income*0.10
	elif income <= 33950:
		tax = 8350*0.10
		tax += (income - 8350) * 0.15
	elif  income <= 82250:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (income - 33950) * 0.25
	elif income <= 171550:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (82250 - 33950) * 0.25
		tax += (income - 82250) * 0.28
	elif income <= 372950:
		tax = 8350*0.10
		tax += (33950- 8350) * 0.15
		tax += (82250 - 33950) * 0.25
		tax += (171550 - 82250) * 0.28
		tax += (income - 171550) * 0.33
	else:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (82250 - 33950) * 0.25
		tax += (171550- 82250) * 0.28
		tax += (372950 - 171550) * 0.33
		tax += (income - 372950) * 0.35
	print(f"your tax is ${tax: .2f}")

#married separate
elif status == 1:
	if income <= 8350:
		tax = income*0.10
	elif income <= 33950:
		tax = 8350*0.10
		tax += (income - 8350) * 0.15
	elif income <= 68525:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (income - 33950) * 0.25
	elif income <= 104425:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (68525 - 33950) * 0.25
		tax += (income - 68525) * 0.28
	elif income <= 186475:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (68525 - 33950) * 0.25
		tax += (104425 - 68525) * 0.28
		tax += (income - 104425) * 0.33
	else:
		tax = 8350*0.10
		tax += (33950 - 8350) * 0.15
		tax += (68525 - 33950) * 0.25
		tax += (104425 - 68525) * 0.28
		tax += (186475 - 171550) * 0.33
		tax += (income - 186475) * 0.35
	print(f"your tax is ${tax: .2f}")

#married jointly/qualified widow(er)
elif status == 2:
	if income <= 16700:
		tax = income*0.10
	elif income <= 67900:
		tax = 16700*0.10
		tax += (income - 16700) * 0.15
	elif income <= 137050:
		tax = 16700*0.10
		tax += (67900 - 16700) * 0.15
		tax += (income - 67900) * 0.25
	elif income <= 208850:
		tax = 16700*0.10
		tax += (67900 - 16700) * 0.15
		tax += (137050 - 67900) * 0.25
		tax += (income - 137050) * 0.28
	elif income <= 372950:
		tax = 16700*0.10
		tax += (67900 - 16700) * 0.15
		tax += (137050 - 67900) * 0.25
		tax += (208850 - 137050) * 0.28
		tax += (income - 208850) * 0.33
	else:
		tax = 16700*0.10
		tax += (67900 - 16700) * 0.15
		tax += (137050 - 67900) * 0.25
		tax += (208850 - 137050) * 0.28
		tax += (372950 - 208850) * 0.33
		tax += (income - 372950) * 0.35
	print(f"your tax is ${tax: .2f}")

#head
elif status == 3:
	if income <= 11950:
		tax = income*0.10
	elif income <=  45500:
		tax = 11950*0.10
		tax += (income - 11950) * 0.15
	elif income <= 117450:
		tax = 11950*0.10
		tax += (45500 - 11950) * 0.15
		tax += (income - 45500) * 0.25
	elif income <= 190200:
		tax = 11950*0.10
		tax += (45500 - 11950) * 0.15
		tax += (117450 - 45500) * 0.25
		tax += (income - 117450) * 0.28
	elif income <= 372950:
		tax = 11950*0.10
		tax += (45500 - 11950) * 0.15
		tax += (117450 - 45500) * 0.25
		tax += (190200 - 117450) * 0.28
		tax += (income - 190200) * 0.33
	else:
		tax = 11950*0.10
		tax += (45500 - 11950) * 0.15
		tax += (117450 - 45500) * 0.25
		tax += (190200 - 117450) * 0.28
		tax += (372950 - 190200) * 0.33
		tax += (income - 372950) * 0.35
	print(f"your tax is ${tax: .2f}")
else:
		print("invalid status")
		

		
		


	

	
	