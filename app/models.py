

import csv

class  TillerTransactions(object):

    file = r'TillerTransaction.csv'

    def getdata(self):
        data = []
        with open(r'TillerTransaction.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data


