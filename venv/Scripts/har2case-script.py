#!C:\Users\o_p_q_o\PycharmProjects\Python\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'har2case==0.1.10','console_scripts','har2case'
__requires__ = 'har2case==0.1.10'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('har2case==0.1.10', 'console_scripts', 'har2case')()
    )
