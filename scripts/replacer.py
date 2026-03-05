import re
from datetime import datetime

# CONFIGURATION
TEX_FILE = '../../Cover Letter.tex'

def replace_body(new_body: str):

    with open(TEX_FILE, 'r') as f:
        content = f.read()

    pattern = r'(% -- BODY BEGIN --\n).*?(% -- BODY END --)'
    replacement = r'\g<1>' + new_body + r'\n\g<2>'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        raise ValueError("Could not find BODY BEGIN/END markers in the file.")

    with open(TEX_FILE, 'w') as f:
        f.write(new_content)

    print("Body Replaced [✅]")

def replace_subject(new_subject: str):

    with open(TEX_FILE, 'r') as f:
        content = f.read()

    pattern = r'(% -- SUBJECT BEGIN --\n).*?(% -- SUBJECT END --)'
    replacement = r'\g<1>' + new_subject + r'\n\g<2>'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        raise ValueError("Could not find SUBJECT BEGIN/END markers in the file.")

    with open(TEX_FILE, 'w') as f:
        f.write(new_content)

    print("Subject Replaced [✅]")

def replace_salutations(new_salutations: str):

    with open(TEX_FILE, 'r') as f:
        content = f.read()

    pattern = r'(% -- SALUTATIONS BEGIN --\n).*?(% -- SALUTATIONS END --)'
    replacement = r'\g<1>' + new_salutations + r'\n\g<2>'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        raise ValueError("Could not find SALUTATIONS BEGIN/END markers in the file.")

    with open(TEX_FILE, 'w') as f:
        f.write(new_content)

    print("Salutations Replaced [✅]")

def replace_date(): 
    with open(TEX_FILE, 'r') as f:
        content = f.read() 

    date_str = datetime.now().strftime("%B %#d, %Y")

    pattern = r'(% -- DATE BEGIN --\n).*?(% -- DATE END --)'
    replacement = r'\g<1>' + date_str + r'\n\g<2>'
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0 :
        raise ValueError("Could not find DATE BEGIN/END markers in the file.")

    with open(TEX_FILE, 'w') as f:
        f.write(new_content)

    print("Date Replaced [✅]")