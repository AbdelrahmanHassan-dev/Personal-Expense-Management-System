import sys
from datetime import datetime
import csv
import re
import calendar
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
class Expenses:
    def __init__(self,category,price,time_buying=None):
        self.category = category
        self.price = price
        if time_buying == None:
            self.time_buying = datetime.now().date()
        else:
            self.time_buying = time_buying

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if price > 0 :
            self._price = price 
        else:
            raise ValueError("the price has to be positive")

    
    def put_info_csv (self):
        '''
        Docstring for put_info_csv: it is take dictionary and put it like a row in csv file 
        '''
        with open("expenses.csv", "a") as file :
            file_name= ["category","price","time_buying"]
            writer = csv.DictWriter(file, fieldnames=file_name) 
            # writer.writeheader() #I did that because everytime I run the code it is rewrite the first agina in the csv file
            writer.writerow({"category":self.category ,"price":self.price,"time_buying":self.time_buying})

def main():
    while True:
        try:
            while True:
                try:
                    num_prog =int(input("\n \n \n Welcome to Personal Accounting System\n \n Choose an option:\n 1. Add expense\n 2. Average monthly spending per day \n 3. Show data in PDF \n 4. Show data without anychange: \n 5. Show what is the high expenses \n 6. Convert the prices into EGP \n 7. Exit\n \nJust write the number: \n" ))
                    break
                except ValueError:
                    print("there are mistake, you have to input just the number")
            if num_prog == 1 :
                while True:
                    try:
                        text_input = input("enter the category, then the price, and the time: ")
                        if get_info(text_input) == True:
                            break
                        else:
                            print("\ntry agian with the right format like that (meal, 505, 2026-01-30)\n if you want to get out click ctrl+D \n ")

                    except:
                        sys.exit()

            if num_prog == 2:
                while True:
                    try:
                        date_year= int(input("Enter the year: "))
                        date_month= int(input("Enter the month: "))
                        print(average_price_month(data_month(show_statistics(),date_year,date_month)))
                        break
                    except ValueError:
                        print("there are mistake, Enter the year and the month like this format 2025, 01")
            if num_prog ==3:
                all_thing_pdf(show_statistics())
            if num_prog == 4:
                show_data(show_statistics())
            if num_prog == 5:
                get_high_expenses(show_statistics())

            if num_prog ==6:
                # print(convert_currency(show_statistics(),price_change()))
                print(tabulate((convert_currency(show_statistics(),price_change())), headers="keys"))
                
            if num_prog == 7:
                sys.exit("Thanks for using OUR system0")
        except:
            sys.exit("Thanks for using OUR system")
    

# def accountant():
#     ...

def get_info(text_input):
        if match := re.search(r"^([a-z]+), ?([0-9]+)(?:, ?(\d{4}[-,\/]\d{1,2}[-,\/]\d{1,2})|,? ?(\d{4}[-,\/]\d{1,2}[-,\/]\d{1,2})?)",text_input): 
            time_text = match.group(3)
            if time_text:
                time_text= datetime.strptime(match.group(3),'%Y-%m-%d').date()
            else:
                time_text=datetime.now().date()
            obj = Expenses(match.group(1), int(match.group(2)),time_text)
            obj.put_info_csv()
            return True
        else:
            return False
        

def show_statistics():
    try:
        list_price=[]
        with open("expenses.csv") as file:
            reader = csv.DictReader(file)
            list_expenses=list(reader)
            return (list_expenses)
    except FileNotFoundError:
        sys.exit("there aren't file by this name or this path")

def data_month(list_expenses, year,month):
    list_month=[]
    for line in list_expenses:
        date= datetime.strptime(line["time_buying"],'%Y-%m-%d').date()
        if date.year == year and date.month == month: 
            list_month.append(line)
        num_days = calendar.monthrange(year, month)[1]
    return list_month, num_days


# data_month(show_statistics(),2025,10)

def average_price_month(list_month):
    list_price_month=[]
    for line in list_month[0]:
        list_price_month.append(int(line["price"]))
    return round(sum(list_price_month)/list_month[1])

# print(average_price_month(data_month(show_statistics(),2025,10)))


def show_data(list_expenses):
    # headers=
    # print(tabulate((list_expenses, headers="keys")))
    print(tabulate(list_expenses, headers="keys"))

# show_data(show_statistics())


def get_high_expenses(list_expenses):
    get_high = list(filter(lambda line:int(line['price'])>1000,list_expenses))
    show_data(get_high)

# get_high_expenses(show_statistics())
def price_change():
    page= requests.get("https://wise.com/gb/currency-converter/rub-to-egp-rate")
    soup=BeautifulSoup(page.content,"lxml")
    # print(soup)
    the_section = soup.find_all("div",{'class':'_container_1st55_1'})
    # print(the_section[0])
    part1= (the_section[0].find_all("table",{'class':'_table_1st55_9'}))[0].find('tbody').find_all('tr')[0].find_all('td')[1].text
    # print(part1)
    get_value = re.search(r"^([0-9]+|[0-9]\.[0-9]+) EGP", part1)
    if get_value:
        try:
            return float(get_value.group(1))
        except:
            return False
    else:
        return False

def convert_currency(list_expenses, price_change):
    if price_change == False:
        return("Sorry We have a problem right now we will solve it soon!")
    return (list(map(lambda line: line|{"price": int(line["price"])*price_change},list_expenses)))
# convert_currency(show_statistics(),price_change())


def all_thing_pdf(list_expenses):
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=24)
    # # page_width = pdf.w
    # # page_height = pdf.h
    # # text_height = 10
    # # pdf.set_y((page_height-text_height)/2)
    # # pdf.cell(w=page_width, h=text_height, txt="Centered Text", align='C', ln=1)
    # pdf.cell(w=0, h=10, txt="Welcome to Personal Accounting System", align='C', ln=1)

    # pdf.set_font("Arial", size=12)
    # pdf.write(20,f"{list_expenses}")
    # pdf.output("te.pdf")    

    new_list= [["category","price","time_buying"]]
    for line in list_expenses:
        new_list.append([line['category'],line['price'],line['time_buying']])
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.cell(w=0, h=10, txt="Welcome to Personal Accounting System", align='C', ln=1)
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    with pdf.table() as table:
            for data_row in new_list:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)
    pdf.output("report.pdf")
        


# all_thing_pdf(show_statistics())

if __name__ == "__main__":
    main()