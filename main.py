
from datetime import datetime
current_datetime = datetime.now()
print('Текушая дата и время: ', end = "")
print(current_datetime)

task = int(input('Сколько еще бодрствуем ?'))
if task > 3:
    print('Не выспишься...')
else:
    print('Норм')