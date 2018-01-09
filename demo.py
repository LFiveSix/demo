from flask import Flask
from flask_wtf.csrf import CSRFProtect
import subprocess
import os
csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)


@csrf.exempt
@app.route('/webhook', methods=['POST'])
def webhook():
    # status = os.system('sh /str/mcld.sh')
    status = subprocess.Popen(['sh /str/mcld.sh'], shell=True)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
