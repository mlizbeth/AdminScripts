import csv
import re
import copy

#regex = r'(^[a-z]{2,8}[0-9]*)'

with open('its.csv', 'r') as in_file, open('out.csv', 'w', newline='') as out_file:
    data = list(csv.reader(in_file))
    writer = csv.writer(out_file, delimiter=',')
    data_bak = copy.deepcopy(data)
    groups = set()
    keyList = []
    valueList = []

    for entry in data:
        entry.remove(entry[0])
        for sublist in entry:
           groups.add(sublist)

    groupList = copy.deepcopy(list(groups))

    writer.writerow(groupList)

    for row in data_bak:
        keyList.append(row[0])
    
    for row in data:
        valueList.append(row)

    masochism = dict(zip(keyList, valueList))

    for username, usergroup in masochism.items():
        dataToWrite = []
        for col in range(0, len(groupList)):
            for rowItem in range(0, len(usergroup)):
                if usergroup[rowItem] == groupList[col]:
                    dataToWrite.append(username)
                    break
                else:
                    if rowItem == (len(usergroup)-1):
                        dataToWrite.append(' ')
        writer.writerow(dataToWrite)
out_file.close()