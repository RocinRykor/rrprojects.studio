import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)


import rrprojects

app = rrprojects.application

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
