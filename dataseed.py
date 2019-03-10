from googleapiclient.discovery import  build
from httplib2 import  http
from oauth2client import file, client, tools
from collections import namedtuple
from app import db
from app.models import TillerTransaction, tiller_map
import csv
from datetime import date, datetime
from decimal import Decimal


class SeedData(object):

    def __init__(self):
        self.sheet_id = '1PY4A10ODPBOx4F8hqjwlQ-aDRIsilCwB1vrk7HCrvx8'  #tiller raw feed
        self.range_name = 'Transactions'

    def seed_db(self):
        """ seed_db is going to read data from csv into db """
        obj_list = []
        temp_dict = {}
        with open(r'TillerTransaction.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for k, v in row.items():
                    if tiller_map[k] is not None:
                        temp_dict.update({tiller_map[k]: v})
                #obj_list.append(self._transform_values(temp_dict))
                obj_list.append(TillerTransaction(**self._transform_values(temp_dict)))

            for ob in obj_list:
                db.session.add(ob)
                db.session.commit()
        return obj_list


    def _transform_values(self,temp_dict):

        temp_dict['dateadded'] = datetime.strptime(str(temp_dict['dateadded']), '%m/%d/%Y %H:%M:%S')
        temp_dict['trans_date'] = datetime.strptime(str(temp_dict['trans_date']), '%m/%d/%Y' )
        temp_dict['amount'] = Decimal(temp_dict['amount'].replace('$', '').replace(',', ''))
        return temp_dict

    def get_new_transactions(self):

        """ gets transactions from Google Spread sheets and inserts them into the database """
        pass


#Check Number	Month	Week		Dup Score	Dup Match
