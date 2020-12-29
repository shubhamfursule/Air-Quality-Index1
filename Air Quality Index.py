dictonary12={}
def check_air_quality(day,air_quality_index):
    if day not in dictonary12:
        b=[]
        b.append(air_quality_index)
        dictonary12.update({day:b})
    else:  
        dictonary12[day].append(air_quality_index)
        dictonary12.update({day:dictonary12[day]})
    #print(dictonary12)
    return dictonary12
for i in range(10):
    day1,air_index=input().split(",")
    a=check_air_quality(day1,int(air_index))
print(a)