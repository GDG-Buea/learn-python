# This program  gets the subtotal and the gratuity rate from the user,then computes the gratuity and total.

subtotal, gratuityRate = eval(input("Enter the subtotal and gratuity rate of a cylinder: "))

gratuity = int((gratuityRate/100) * 1000)/100

total = int((gratuity + subtotal) * 100) / 100

print("The gratuity is: ", gratuity, "and the total is: ", total)

