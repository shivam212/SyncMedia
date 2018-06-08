import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sh = client.open("syncmedia")
sk=sh.worksheet("Sheet1")
records = sk.get_all_records()
pp=pprint.PrettyPrinter()
pp.pprint(records)