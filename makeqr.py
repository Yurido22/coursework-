import pyqrcode
from input import data


def qr_text():
    numbers = pyqrcode.create(data)
    print(numbers.text)


def terminal():
    text = pyqrcode.create(data, error='')


def qr_png():
    ID = pyqrcode.create(data, error='M', version=, mode='binary')
    # ID.svg('qr-id.svg', scale=8, background="white", module_color=(50, 92, 168))
    ID.png('qr-id.png', scale=8,  background="white", module_color=(50, 92, 168))
    # ID.eps('qr-id.eps', scale=2, background="white", module_color=(50, 92, 168))
    print(ID.terminal(quiet_zone=2))


# qr()
