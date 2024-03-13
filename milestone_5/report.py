import datetime
import argparse

monthes_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def read_db(filename_:str)->list:
    database = []
    with open(filename_, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                item = line.strip().split(',')
                database.append(dict(name=item[0], hiring_date=item[1], department=item[2],
                                     birthday=item[3]))
    return database

def get_bd_list_by_month(mon:int, database:list):
    employees = []
    for item in database:
        bdate = item.get("birthday")
        month = int(bdate[bdate.index("-")+1:bdate.index("-")+3])
        if mon == month:
            employees.append(item)
    return employees

def get_anniv_list_by_month(mon:int, database:list)->list:
    employees = []
    for item in database:
        bdate = item.get("hiring_date")
        month = int(bdate[bdate.index("-") + 1:bdate.index("-") + 3])
        year = int(bdate[:bdate.index("-")])
        if mon == month and (datetime.datetime.now().year - year) % 10 == 0:
            employees.append(item)
    return employees

def split_by_dept(empl_list:list)->dict:
    bd_dict = dict()
    for item in empl_list:
        if item.get("department") in bd_dict.keys():
            l = list(bd_dict.get(item.get("department")))
            l.append(item)
            bd_dict.update({item.get("department"): l})
        else:
            bd_dict[item.get("department")] = [item]
    return bd_dict

def execute_report(filename_, month_):
    database = read_db(filename_)
    month = monthes_dict.get(month_.capitalize())
    bdays = get_bd_list_by_month(month, database)
    print('--- Birthdays ---')
    print(f'Total: {len(bdays)}')
    print('By department:')
    splited = split_by_dept(bdays)
    for i in splited.keys():
        print(f'- {i}: {len(splited.get(i))}')

    anniversaries = get_anniv_list_by_month(month, database)
    print('--- Anniversaries ---')
    print(f'Total: {len(anniversaries)}')
    print('By department:')
    splited = split_by_dept(anniversaries)
    for i in splited.keys():
        print(f'- {i}: {len(splited.get(i))}')

def execute_report_with_names(filename_, month_):
    database = read_db(filename_)
    month = monthes_dict.get(month_.capitalize())
    bdays = get_bd_list_by_month(month, database)
    print('--- Birthdays ---')
    print(f'Total: {len(bdays)}')
    print('By department:')
    splited = split_by_dept(bdays)
    for i in splited.keys():
        print(f'- {i}: {len(splited.get(i))}')
        for j in splited.get(i):
            print(f'  * {j.get('name')}')

    anniversaries = get_anniv_list_by_month(month, database)
    print('--- Anniversaries ---')
    print(f'Total: {len(anniversaries)}')
    print('By department:')
    splited = split_by_dept(anniversaries)
    for i in splited.keys():
        print(f'- {i}: {len(splited.get(i))}')
        for j in splited.get(i):
            print(f'  * {j.get('name')}')


parser = argparse.ArgumentParser()
parser.add_argument('params', nargs='+')
parser.add_argument('-v', dest='execute', action='store_const', const=execute_report_with_names, default=execute_report)
args = parser.parse_args()
args.execute(args.params[0],args.params[1])
