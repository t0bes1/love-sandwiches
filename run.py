# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")


def get_sales_data():
    while True:
        print("please enter sales data")
        print("data should be 6 numbers")
        data_str = input("Enter your data here:")

        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data is Valid")
            break
    return sales_data


def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"wrong numnber of {values}")
    except ValueError as e:
        print(f"invalid data: {e}")
        return False

    return True


def update_sales_worksheet(data):
    print("updating sales worksheet ...")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully")


def calculate_surplus_data(sales_row):
    print("Calculating surplus data...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)


def main():
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


print("Welcome to Love Sandwiches data automation")
main()
