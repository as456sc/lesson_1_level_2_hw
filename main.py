from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


def time_now():
  print(datetime.today())


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    time_now()