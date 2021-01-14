#Merge two dictionaries
def merge(dic1,dic2):
    return(dic2.update(dic1))


dic1={"one":1,"two":2,"Three":3}
dic2={"four":4,"five":5,"six":6}
print(merge(dic1,dic2))
print(dic2)

