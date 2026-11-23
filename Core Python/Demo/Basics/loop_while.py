n = 153
rev = 0
temp = n
while(n>0):
    d = n % 10
    rev = rev + d**3
    n= n//10
if n == rev:
    print("amstong number")
else:
    print("not amstong")