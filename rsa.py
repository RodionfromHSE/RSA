import numpy as np

def gen_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while np.gcd(e, phi) != 1: e += 1 # e _|_ phi
    d = pow(e, -1, phi)
    return {
        'public': {'e': e, 'n': n},
        'private': {'d': d, 'n': n}
    }

def encrypt(m, pub):
    return pow(m, pub['e'], pub['n'])

def encrypt_str(s, pub):
    cs = [encrypt(ord(c), pub) for c in s]
    text = ''.join([str(c) + ' ' for c in cs])
    return text

def decrypt(c, priv):
    return pow(c, priv['d'], priv['n'])

def decrypt_str(text, priv):
    cs = [int(c) for c in text.split()]
    s = ''.join([chr(decrypt(c, priv)) for c in cs])
    return s

