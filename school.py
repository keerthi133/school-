name=input("enter your name:")
print("welcome ",name)
id=int(input("enter your id:"))
print("your id is",id)
print("enter your marks out of 100:")
math=int( input("enter your marks in maths:"))
sci=int(input("enter your marks in sci:"))
social=int(input("enter your marks in social:"))
hindi=int(input("enter your marks in hindi:"))
eng=int(input("enter your marks in eng:"))
avg=(math+sci+social+hindi+eng)/5
print("your average is",avg)
if(avg>=90 and avg<=100):
 print("grade A+")
elif(avg>=80 and avg<90):
 print("grade A")
elif(avg>=70 and avg<80):
 print("grade B")
elif(avg>=60 and avg<70):
 print("grade C")
elif(avg>=50 and avg<60):
 print("grade D")
elif(avg<50):
 print("FAIL")
elif(avg>=100):
 print("pls enter your marks out of 100:")
 
Output:
enter your name:Keerthi
welcome Keerthi
enter your id:12345
your id is:12345
enter your marks out of 100:
enter your marks in maths:80
enter your marks in sci:70
enter your marks in social:60
enter your marks in hindi:50
enter your marks in eng:40
your avg is 60
grade C
