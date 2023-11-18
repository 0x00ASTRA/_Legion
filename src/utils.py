import random
import rsa

def generate_serial_id(id_length = 6, section_size = 4):
    id = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

    for i in range(id_length):
        id += random.choice(chars) * section_size
        if i < id_length:
            id += '::'
    return id

def generate_keys() -> tuple:
    (pubkey, privkey) = rsa.newkeys(2048)
    return (pubkey, privkey)
