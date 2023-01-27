import sys
from subprocess import getoutput as go
exe = sys.argv[1]
[print(x) for x in go("wine %s" % exe).split('\n') if (not x.startswith("00")) and (not x.startswith("wine"))]

