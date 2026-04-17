"""1. Student Score Processor
Scenario: A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file"""

std_det=[("Virat",60),("Rajath",55),("Jitesh",45)]
print(std_det,type(std_det))

std_dic=dict(std_det)
print(std_dic,type(std_dic))

for k, m in std_dic.items():
    if m>50:
        print(k)
total=sum(std_dic.values())
print(total)

l=len(std_dic)
print(l)

avg=total/l
print(f"{avg:.2f}")

f=open("result.txt","w")
f.write(str(f"Average of students above 50 is: {avg:.2f}"))
f.close()
