addkey = 'PJKVA RJGME BWJBH'
subkey = 'CJDTK WEDYD QWUL'
minkey = 'SBVRZ ZENPV ND'

import string 
ttn = {}
ntt = {}
holder = 0
for x in string.ascii_lowercase:
    ttn[x] = holder
    ntt[holder] = x
    holder+=1

def decode_sub(s):
    dec = ''
    s = s.to_lower()
    for x in range(0, len(s)):
        print(x, ttn[x])
        dec += ntt[ttn[x] - ttn[x]] 
    return dec
