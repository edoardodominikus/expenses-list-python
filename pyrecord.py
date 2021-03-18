from datetime import*
import pycategories

categories = pycategories.Categories()
class Record:
    """Represent a record."""
    def __init__(self,date,category,description,amount ): 
        """ This method is for initializing the class for records which accept 3 attributes in parameter
            with @property we can input the class (example : record = Record('food','sandwich',-100))
        """
        self._category = category
        self._description = description
        self._amount = amount
        self._date = date
    @property
    def category(self):
      return self._category
    @property
    def description(self):
      return self._description
    @property
    def amount(self):
      return self._amount 
    @property
    def date(self):
      return self._date
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """This method is for inputting records.txt to the Record class list"""
        try:
          fh = open('records.txt','r')
          self._initial_money = int(fh.readline())
          try:
                self._records = []
                 #input initial amount in first line

                for line in fh.readlines(): #putting data structures in tuple
                    temp = (line.split(' '))
                    temp[3] = int(temp[3])
                    self._records.append(Record(temp[0],temp[1],temp[2],temp[3]))
                
            #check if there is file but empty or format error
          except ValueError:

                    self._records = []
                    self._initial_money = 0
               
          else:
                
                fh.close()
            #if there is no record.txt file
        except FileNotFoundError and ValueError:
          
                self._initial_money=0
                self._records = []
          
    def money(self,_initial_money):
        self._initial_money = _initial_money
    
    def get_money(self):
        # print(self._initial_money)
        return self._initial_money

    def pull_records(self):
        
          return self._Record


    def add(self,a,categories):
        """This method for adding data into record by user input 
            with checking it first if the categories that the user inputted is in the categories listed
        """
        try:        #input and putting data into tuple
                #a = input('Add an expense or income record with description and amount:\n')
                
            temp1 = a.split(' ')
            
            if len(temp1) == 4:
              temp_date = temp1[0]
              try:
                date.fromisoformat(temp_date)
                category = temp1[1]
                temp = categories.is_category_valid(category)
                
                if temp == False:
                    print('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
                else:
                    temp1[3] = int(temp1[3])
                    self._records.append(Record(temp1[0],temp1[1],temp1[2],temp1[3]))
                    #add start value money
                    self._initial_money = self._initial_money + temp1[3]
              except ValueError:
                    a = ''
                    print('The format of date should be YYYY-MM-DD.Fail to add a record.')
            elif len(temp1) == 3:
              today = str(date.today())
              print(today)
              temp1.insert(0,today)
              category = temp1[1]
              temp = categories.is_category_valid(category)
                
              if temp == False:
                    print('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
              else:
                    temp1[3] = int(temp1[3])
                    self._records.append(Record(temp1[0],temp1[1],temp1[2],temp1[3]))
                    #add start value money
                    self._initial_money = self._initial_money + temp1[3]
        except ValueError:
                a = ''
                print('Invalid value for money.\nFail to add a record.')
        except IndexError:
                a = ''
                print('The format of a record should be like this: breakfast -50.\nFail to add a record.')

    def view(self):
        """This method is for printing all the data in record and balance """
        # 1. Print all the records and report the balance.
        print("Date"+" "*10+"Categories"+" "*10+"Description"+" "*10+"Amount")
        print("=================================")
        for i in self._records:
            print(f"{i.date:<20}{i.category:<20s} {i.description:^20s} {str(i.amount):>20s}")
        print("=================================")
        print('Now you have %d dollars.'%self._initial_money)
          
    def delete(self,delete_records):
        """This method is for deleting data in record list
            First it will prompt from which category do you want to delete?
            Next, it will show the data from that category and index will be shown.
            Choose the index and delete.
        """
        
        # sub = categories.find_subcategories(delete_records)
       
        # temp = list(filter(lambda n : n.category in sub ,self._records))
        # print("Date"+" "*10+"Categories"+" "*5+"Description"+" "*5+"Amount")
        # print("=================================")
        # for j,i in enumerate(temp):
        #     print(f"{i.date:<20s}{i.category:<20s} {i.description:^20s} {str(i.amount):>20s} {str(j):>10} ")
        #     #print(i[0]+" "*10+i[1]+" "*10+str(i[2])+' '+str(j)+')')
        # print("=================================")
        # ask = int(input('Which index do you want to delete?'))
        
        self._initial_money = self._initial_money - int(self._records[delete_records].amount)
        self._records.pop(delete_records)

    
    def save(self):
        """This method is for saving data to file records.txt """
        # 1. Write the initial money and all the records to 'records.txt'.
        self._initial_money = str(self._initial_money)
        print(self._initial_money)
        #write/make file
        with open('records.txt','w') as fh:
          fh.write(self._initial_money+"\n")
          fh.write('\n'.join('{} {} {} {}'.format(x.date,x.category,x.description,x.amount) for x in self._records))