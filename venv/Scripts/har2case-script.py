#!D:\HttpRunnerManager-master\venv\Scripts\python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'har2case==0.2.0','console_scripts','har2case'
__requires__ = 'har2case==0.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('har2case==0.2.0', 'console_scripts', 'har2case')()
    )
