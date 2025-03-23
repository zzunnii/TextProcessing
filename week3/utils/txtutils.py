# utils/txtutils.py 파일
def simple_tokenize(txt):
    txt = txt.lower()
    txt = txt.replace('.', ' .')
    token = txt.split()
    return token

def lower_tokenize(txt):
    txt = txt.lower()
    token = txt.split()
    return token

def complex_tokenize(txt):
    txt = txt.lower()
    txt = txt.replace('.', ' .')
    token = txt.split()
    return token