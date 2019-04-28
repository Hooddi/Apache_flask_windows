activate_this = r'F:\Github_hudi\Public\Apache_Flask_windows\venv\Scripts\activate_this.py'
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

import sys
#Expand Python classes path with your app's path
sys.path.insert(0, r'F:\Github_hudi\Public\Apache_Flask_windows')

from test import app as application