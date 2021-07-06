import requests
import getpass
import pandas as pd
from past.builtins import raw_input

url = "https://engiegbs.service-now.com/sys_report_template.do?jvar_report_id=5e4ca2311be66c90f2fffc07cb4bcbd0"

uname=raw_input("Enter Username: ")
pswd=getpass.getpass('Enter Password: ')

r=requests.get(url, auth=(uname, pswd))
c=pd.read_csv(url)


if r.status_code==requests.codes.ok:
    print("Requests made a connection.\n")
    f=open(r'C:\dump.csv', 'w')
    f.write(r.content)
    f.close()

else:
    print("\nAn error occured while establishing a connection.")
    print("Status code returned: ",r.status_code)

c=input("\nEnter a key to exit.\n")