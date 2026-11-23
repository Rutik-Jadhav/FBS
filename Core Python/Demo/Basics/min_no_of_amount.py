
amt=980
fh=amt //500
amt = amt%500

th = amt// 200
amt = amt%200

h = amt//100
amt = amt % 100

f =amt//50
amt = amt%50

t = amt//20
amt=amt%20

ten= amt//10
amt = amt%10

totel_notes = fh + th + h + f + t + ten
print(totel_notes)
