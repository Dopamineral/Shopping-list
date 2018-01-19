#file to write in shopping list
f = open('shopping list.txt','w')

#time basics
import datetime
today = datetime.datetime.now()

#elementree basics
import xml.etree.ElementTree as ET
tree = ET.parse('food.xml')
root = tree.getroot()

total = 0

for food in root.findall('food'):

    item = food.find('item').text

    duration = food.find('duration').text
    duraint = int(duration)
    
    price = food.find('price').text
    intprice = float(price)

    dateraw = food.find('date_last').text
    date2 = dateraw[0:10]
    date = datetime.datetime.strptime(date2,"%Y-%m-%d")
   # print dateraw
   # print date2
   # print date

    
    expdate = date + datetime.timedelta(days=duraint)
    
    if expdate < today:
        print item,price
        fitem = str(item)
        fprice = str(price)
        f.write(fitem +"--- "+ fprice + "\n") 

        total = total + intprice
        #conditional sub-part to the initial food-counter, this will change
        #date only for those which have been selected previously
        for date in food.findall('date_last'):
            #print date.text
            date.text = str(datetime.datetime.now())
            #print date.text
print total
ftotal = str(total)
f.write("\n" + "Estimated total: " + ftotal)

tree.write('food.xml')
f.close()

