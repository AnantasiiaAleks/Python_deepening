from datetime import datetime, timedelta

def future_day(days_cnt: int) -> str:
    """
    Возвращает дату, которая наступит через указанное количество дней
    :param days_cnt: количество дней
    :return: дата в формате YYYY-MM-DD
    """

    current_day = datetime.now()
    future = current_day + timedelta(days=days_cnt)
    return future.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(future_day(10))
    print(future_day(30))