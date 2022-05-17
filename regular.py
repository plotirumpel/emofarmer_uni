import re
def regular_1_1(st):
    return re.fullmatch(r"[a-z]+@[a-z]+\.[a-z]{2,}", st)

def regular_1_2(st):
    return re.fullmatch(r'[a-z-_0-9]+@[a-z-_0-9]+\.[a-z]{2,}', st)

def regular_1_3(st):
    return re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", st)

def regular_2(st):
    st = re.sub(r'[ ()-]','',st)
    return re.findall(r'\d{7,10}', st)

def regular_3(st):
    return re.sub(r' +,', ',', st)

def regular_4(st):
    pair = re.compile(r'([\w]+)-([\w]+)',re.U)
    for m in re.finditer(pair,str):
        st = re.sub(m.group(2),m.group(1),st)
        st = re.sub(m.group(1),m.group(2),st,1)
    return st

def regular_5(st):
    cats = re.compile(r'\bкот\b', flags=re.MULTILINE+re.IGNORECASE)
    return len(cats.findall(st))

def regular_6(st):
    chislo = r'-\d+'
    for m in re.findall(chislo,st):
        changed = int(m)+1
        st = re.sub(m, str(changed), st)
    return st


