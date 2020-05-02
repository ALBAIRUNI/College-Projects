import sys
from struct import pack, unpack


def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


def encrypt(block):
    a, b, c, d = unpack("<4I", block)
    for rno in xrange(32):
        a = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
        b = c ^ F(a ^ F(d) ^ (a | d))
        c = d ^ F(a | F(a) ^ a)
        d = a ^ 31337

        a = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)
        b = b ^ F(d ^ F(a) ^ (d | a))
        c = a ^ F(d | F(d) ^ d)
        d = d ^ 1337

    return pack("<4I", a, b, c, d)


pt = open(sys.argv[1]).read()
while len(pt) % 16: pt += "#"

ct = "".join(encrypt(pt[i:i + 16]) for i in xrange(0, len(pt), 16))
open(sys.argv[1] + ".enc", "w").write(ct)


def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for i in xrange(32):
        a3 = a

        d = d ^ 1337
        a = c ^ (F(d | F(d) ^ d))
        b = b ^ (F(d ^ F(a) ^ (d | a)))
        c = a3 ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))

        a2 = a

        a = d ^ 31337
        d = c ^ (F(a | F(a) ^ a))
        c = b ^ (F(a ^ F(d) ^ (a | d)))
        b = a2 ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))

    return pack("<4I", a, b, c, d)


pt = open(sys.argv[1]).read()
ct = "".join(decrypt(pt[i:i + 16]) for i in xrange(0, len(pt), 16))
x = 0
for i in ct:
    if i == '#':
        x += 1
print(ct[0:len(ct) - x])
