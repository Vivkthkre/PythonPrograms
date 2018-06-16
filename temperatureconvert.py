def convert(temp,unit):
    unit=unit.lower()
    if unit=='c':
        temp=9/5 *temp + 32
        return "%s degrees fahrenhiet"%temp
    if unit=='f':
        temp=(temp-32) / 9 * 5
        return "%s degrees celcius"%temp
intemp=int(input("Temperature:"))
inunit=str(input("unit of measure(c/f):"))  
print(convert(intemp,inunit))
