import requests
import datetime
import time

url="https://api.covid19api.com/summary"


def report_covid_status(serial, limit=10):

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    serial.write(f"            COVID STATUS AT {now}\r\n".encode())
    time.sleep(0.5)
    serial.flush()
    serial.write("\r\n".encode())
    data = requests.get(url).json()

    headers = ["country", "cases", "deaths", "recoveries"]
    serial.write(f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}\r\n".encode())
    print_country(serial, data["Global"], key="Global")
    time.sleep(1)
    countries = sorted(data["Countries"], key=lambda x: -x["TotalConfirmed"])
    for i in range(0, limit):
        print_country(serial, countries[i])


def print_country(serial, data, key=None ):
    total = print_number(data["TotalConfirmed"])
    deaths  = print_number(data["TotalDeaths"])
    recovered = print_number(data["TotalRecovered"])

    if key == None:
        key = nice_name(data["Country"])

    serial.write(f"{key:>9}: {total} {deaths} {recovered}\r\n".encode())
    serial.flush()
    time.sleep(0.5)

def print_number(value):
    '''prints a number with padding and uk style commas'''
    return f'{value: 10,}'

def nice_name(name):
    if name.startswith("Russia"):
        return "Russia"
    elif name.startswith("United States"):
        return "US"
    elif name.startswith("Iran"):
        return "Iran"
    elif name.startswith("United Kingdom"):
        return "UK"
    else:
        return name

if __name__ == "__main__":
    import sys
    report_covid_status(sys.stdout.buffer)

