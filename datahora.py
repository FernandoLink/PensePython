import datetime
import time

data = datetime.date(year=2021, month=12, day=25)
hora = datetime.time(hour=21, minute=10, second=30)
dataHora = datetime.datetime(year=2021, month=12, day=25, hour=21, minute=10, second=30)

print(f'\033[31mData:\033[m {data}.')
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.isoformat())
print(f'\033[31mHora:\033[m {hora}.')
print(f'\033[31mdataHora:\033[m {dataHora}.')
print(f'\033[31mToday:\033[m {datetime.date.today()}')
print(f'\033[31mNow:\033[m {datetime.datetime.now()}')
print(f'\033[31mTime:\033[m {time.time()}')
timestamp = time.time()
print(f'\033[31mTimestamp:\033[m {datetime.date.fromtimestamp(timestamp)}')
