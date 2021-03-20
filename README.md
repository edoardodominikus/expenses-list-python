# expenses-list-python
A simple python program for daily life expenses list with UI.
# What I learned
- Input output.
- Sequences, sets and dictionary.
- Control construct.
- Exceptions & file.
- Functions.
- Recursions.
- Object oriented programming.
- Iterable, iterator, and generator.
- Time and Tkinter Module.
#**Program explanation**
* Function :
  1. Set initial value money.
  2. Add / delete records.
  3. Add / delete categories.
  4. Find records based on categories.
  5. Display records based on categories and balance.
* Program is divided to 3 sections (main, pycategories, pyrecord) :
  1. main.py .
    - Main code for this program, consists of GUI tkinter design. Some of the tkinter module that i used       are:
          - Label
          - Entry Box
          - Button
          - Button
          - Scrollbar
          - List Box
          - Combo Box
  2. pycategories.py .
    - Consists class categories and declaring list information.
    
  3. pyrecords.py .
    - Consists 2 classes, record and records. Record class is used to make a new data type that             contains the attributes category,description,amount,date. The records class is for storing user       input data. The saved records will later go into records.txt file with format of [Category]           [Description] [Amount] [Date] [Time].
