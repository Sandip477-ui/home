Electricity_bill={'january' : 700,
                  'february': 800,
                  'march' : 850,
                  'april' : 900,
                  'may' : 980,
                  'june' : 1000,
                  'july' :2000,
                  'August' :2500,
                  'september':1900,
                  'october' :1800,
                  'november' : 1200,
                  'December' : 1600,
                  }
total= sum(Electricity_bill.values())
print(f'total Electricity bill is {total}')
print(f'avrege Electricity bill is {total/12}')