import csv
cwb_filename = '108061216.csv'
data = []
header = []
with open(cwb_filename) as csvfile:   
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)

id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
result = 0

for i in range(len(data)):
    if (data[i]['WDSD'] == '-99.000') | (data[i]['WDSD'] == '-999.000'):
        data[i]['WDSD'] = 'remove' 
for count in range(5):
    target_data = list(filter(lambda item: item['station_id'] == id[count], data))

    max = target_data[0]['WDSD']
    min = target_data[0]['WDSD']
    k = 0
    for i in range(len(target_data)):
        if target_data[i]['WDSD'] == 'remove':
                k = k + 1

    if len(target_data) - k > 1:
        for i in range(len(target_data)):     
            if (target_data[i]['WDSD'] != 'remove'):
                if float(target_data[i]['WDSD']) > float(max):
                    max = target_data[i]['WDSD']
                if float(target_data[i]['WDSD']) < float(min):
                    min = target_data[i]['WDSD']
            else:
                if i != len(target_data) - 1:
                    max = target_data[i + 1]['WDSD']
                    min = target_data[i + 1]['WDSD']
    if len(target_data) - k <= 1:
        result = [id[count],'None']    
    else:
        result = [id[count],(float(max) - float(min))]
    id[count] = result
    
print(id)