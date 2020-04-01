import csv

sub = "jkjadls"
titile = ["user_id","user_name","age"]
stu2 = {4455:{"user":'123',"age":'13'},8888:{"user":234,"age":25}}
ret = []
for (uid,v) in stu2.items():
    ret.append([uid,v["user"],v["age"]])

out = open('Stu_csv1.csv','a', newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow([sub])
csv_write.writerow(titile)
for v in ret:
    csv_write.writerow(v)
    