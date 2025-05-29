csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
#print(csv.split(';'))
# print(','.join(csv.split(':')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
# friends_list = [','.join(','.join(csv.split(';')).split(':'))]
friends_list = csv.replace(':', ',').replace(';',',').split(',')
print(friends_list)