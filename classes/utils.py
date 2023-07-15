import random
def generate_serial_id():
    id = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    id_length = 10
    for i in range(id_length):
        id += random.choice(chars)*2
        if i <10:
            id += '::'
    return id