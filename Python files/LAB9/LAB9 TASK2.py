bus_station = {}

while True:
    n = input('Яка потрібна дія ?\n1 - дізнатись значення за ключем\n'
              '2 - вивести весь список рейсів\n3 - додати нову рейс\n'
              '4 - видалити рейс\nend - закінчити роботу\n')
    if n == '1':
        key1 = input('ключ -  ')
        print(bus_station[key1])
    elif n == '2':
        print(bus_station)
    elif n == '3':
        key = input('тег нового рейсу - ')
        flight_number = input('номер рейсу - ')
        driver = input('водій - ')
        price = input('вартість квитка - ')
        departure_time = input('час відправлення - ')
        arrival_time = input('час прибуття - ')
        bus_station[key] = {'bus flights': {
            'flight number': flight_number,
            'driver': driver,
            'price': price,
            'departure time': departure_time,
            'arrival time': arrival_time
        }}
    elif n == '4':
        key = input('який рейс видалити?')
        del bus_station[key]
    elif n == 'end':
        break
    else:
        raise Exception('Некоректне значення дії')
