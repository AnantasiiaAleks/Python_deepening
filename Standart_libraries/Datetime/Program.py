from datetime import datetime

def current_datetime() -> str:
    """
    Показывает текущие дату и время в формате гггг-мм-дд чч:мм:сс,
    день недели,
    номер недели с начала года
    """


    current = datetime.now()
    format_current = current.strftime('%Y-%m-%d\t%H:%M:%S')
    day_of_week = current.strftime('%A')
    week_no = current.isocalendar()[1]

    return f'Точные дата и время: {format_current},\n' \
          f'День недели: {day_of_week},\n' \
          f'Номер недели c начала года: {week_no}'


if __name__ == '__main__':
    print(current_datetime())