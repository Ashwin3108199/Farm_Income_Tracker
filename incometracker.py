import datetime
import pandas as pd
import calendar
import openpyxl
import warnings


warnings.filterwarnings("ignore",category = DeprecationWarning)   #### To suppress the warnings

year = int(input('Enter the current year:'))
month = int(input('Enter the current month:'))

days = calendar.monthrange(year,month)[1]

empty_df = pd.DataFrame()

empty_df.to_excel(r'##############enter the file path###############')

print('The monthly Tracker')

item_list = ['Mango','Gauva','Sugarcane','Corn']
print(datetime.date.today())


Mango_income = []
Gauva_income = []
Sugarcane_income = []
Corn_income = []

count = 0

while count <= days:
    days_income = []
    pd.ExcelFile.close



    for item in item_list:
        print(f'Enter the amount collected for the {datetime.date.today()} for item {item}:')
        income = int(input(f"Enter todays's {item} collection in RS:"))

        if item == 'Mango':
            Mango_income.append(income)

        elif item == 'Gauva':
            Gauva_income.append(income)

        elif item == 'SugarCane':
            Sugarcane_income.append(income)

        elif item == 'Corn':
            Corn_income.append(income)



    Amount = int(days_income[0]) + int(days_income[1]) + int(days_income[2]) +int(days_income[3])
    count += 1

    print(f"Today's TOTAL Collection is {Amount}")

    if count == 1:
        item_list.append('Null')
    days_income.append('Null')




    dict_farm_income = {
        'ITEMS': item_list,
        'Income for the day' : days_income,
    }


    pd_dict = pd.DataFrame(dict_farm_income)

    pd_dict['ITEMS'][4] = 'Todays Collection'
    pd_dict['Income for the day'][4] = Amount
    print(pd_dict)


    with pd.ExcelWriter('########Excel_PAth############',mode = 'a',engine='openpyxl') as writer:
        pd_dict.to_excel(writer sheet_name = f'sheet{count}',index = False)

    if count == 1:

        work_book = openpyxl.load_workbook('#########Excel_Path######')
        sheet = work_book.get_sheet_by_name('Sheet1')
        work_book.remove_sheet(sheet)
        work_book.save('#########Excel_Path######')

    def Total():

        df_total = pd.ExcelFile('##########Excel_Path#######')
        sheet_num = len(df_total.sheet_names)
        print((f'The Farm_income_Excel file contains {sheet_num} sheets'))

        if sheet_num == 2:

            TT_cal_y_n = input(f'Do you want to check the total sum from the {sheet_num } sheets:"YES OR NO":')

            if TT_cal_y_n == 'YES':

                Mango_total = 0
                Gauva_total = 0
                Sugarcane_total = 0
                Corn_total = 0
                over_all_total = 0

                for i in range(sheet_num):


                    dat_f = pd.read_excel(r'#############Excel_Path########',sheet_name= i)

                    Mango_total = Mango_total + dat_f['Income for the day'][0]
                    Gauva_total = Gauva_total + dat_f['Income for the day'][1]
                    Sugarcane_total = Sugarcane_total + dat_f['Income for the day'][2]
                    Corn_total = Corn_total + dat_f['Income for the day'][3]
                    over_all_total = over_all_total + dat_f['Income for the day'][4]

                print(f'The sum total of the MANGO is {Mango_total}RS')
                print(f'The sum total of the Gauva is {Gauva_total}RS')
                print(f'The sum total of the Sugar_Cane is {Sugarcane_total}RS')
                print(f'The sum total of the Corn is {Corn_total}RS')
                print(f'The over all collection  is {over_all_total}RS')

            else :

                pass
    Total()