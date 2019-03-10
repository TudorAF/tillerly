

from app import db


class TillerTransaction(db.Model):

    transaction_id = db.Column(db.String(24), primary_key=True) #Transaction ID
    trans_date = db.Column(db.Date) #Date
    trans_description  = db.Column(db.String(125)) #Description
    short_description = db.Column(db.String(100))  #Short Description
    full_description = db.Column(db.String(225))#Full Description
    amount = db.Column(db.Numeric()) #Amount
    category_hint = db.Column(db.String(50)) #Category Hint
    account_type = db.Column(db.String(25)) #Account
    account_num = db.Column(db.String(10)) #Account #
    institution = db.Column(db.String(20)) #Institution
    dateadded = db.Column(db.DateTime) #Date Added

    def __repr__(self):
        return ('{amount} was spent on {trans_date} at {description} '.format(amount=self.amount,
                                                                              trans_date=self.trans_date,
                                                                              description=self.short_description))


tiller_map = {'Transaction ID': 'transaction_id',
              'Date': 'trans_date',
              'Description': 'trans_description',
              'Short Description': 'short_description',
              'Full Description': 'full_description',
              'Amount': 'amount',
              'Category Hint': 'category_hint',
              'Account': 'account_num',
              'Account #': 'account_num',
              'Institution': 'institution',
              'Date Added': 'dateadded',
              'Check Number': None,
              'Month': None,
              'Dup Match': None,
              'Week': None,
              'Dup Score': None,
              }


### these fields are transmitted but are not needed
#


#used for testing in command line
#    transaction_id  = 'sdfasdf' ,
#    trans_date  = '2019/01/01' ,
#    trans_description = 'test',
#    short_description = 'test test',
#    full_description  = 'testtestestetsetsadfsadf',
#    amount   = 100.00,
#    category_hint  = 'test',
#    institution  = 'test',
#    account_type = 'test',
#    account_num = 'xxxx564',
#    dateadded   = '2019-03-09 22:38:23.290128'