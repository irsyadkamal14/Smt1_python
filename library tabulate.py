from tabulate import tabulate

b=['Smith', 'Jane', 'Doe']
c=[39, 25, 28]
info = {'First Name': [a=[]], 'Last Name': ['Smith', 'Jane', 'Doe'], 'Age': [39, 25, 28]}

print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

      
a=input("masukkan :")



#table = [['First Name', 'Last Name', 'Age'], list.['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]

#print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex = True))
