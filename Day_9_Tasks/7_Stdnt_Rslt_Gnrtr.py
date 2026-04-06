# 7. Student Result Generator (Method Overloading Concept) A school system calculates student results differently depending on available data. Create a Result class where a method can calculate the result using either two subjects or three subjects.

class Result:
    def cal(self,sub1=0,sub2=0,sub3=0):
        res=sub1+sub2+sub3
        return res

r=Result()

print("***Note: If subject marks are not available, enter ZERO***\n")
try:
    s1=int(input("Enter English marks "))
    s2=int(input("Enter Maths marks "))
    s3=int(input("Enter Science marks "))
except ValueError:
    print("Enter Integer numbers only")

print("The Total is ",r.cal(s1,s2,s3))
