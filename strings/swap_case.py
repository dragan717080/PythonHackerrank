import re

def swap_case(s):
    return re.sub("[A-Za-z]", lambda c: chr(ord(c.group(0)) + 32) if bool(re.match('[A-Z]', c.group(0))) else chr(ord(c.group(0)) - 32), s)

if __name__ == '__main__':
    #s = input()
    s = "K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx"
    result = swap_case(s)
    print(result)
    "k96.5gi.SABdh3S.6IfZXmaH5ipTMwj4W0Uj9mowc45EOzKHAsS73GXkOqCD90uGE02CaXpNYmwTywtrvCo.0vNbQ.Siq5hfHKX"
    "k96.5gi.SABdh3S.6IfZXmaH5ipTMwj4W0Uj9mowc45EOzKHAsS73GXkOqCD90uGE02CaXpNYmwTyw'trvCo.0vNbQ.Siq5hfHKX"