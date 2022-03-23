from datetime import date
from pyxirr import xirr


# test = (xirr(['2020-01-01', '2021-01-01', '2022-01-01','2023-01-01'], [-100, 10, 10,110]))
# test = test *100
# test = round(test, 2)
# test = (f'{test:.2f}')

# print(test)

def xirr_test(Class):

    test = (xirr(['2020-01-01', '2021-01-01', '2022-01-01','2023-01-01'], [-100, 10, 10,110]))
    test = test *100
    test = round(test, 2)
    test = (f'{test:.2f}')
