"flask --app webapp run --debug"
"http://127.0.0.1:5000/"
"testA,40,-111,1974_2013,CCSM4,Search"
from flask import Flask, render_template, request
import os
import subprocess as sub

env_copy = os.environ.copy()
env_copy["MY_VARIABLE"] = "new_value"

cwd = os.getcwd()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    text_input = request.form['text_input']
    with open(os.path.join(cwd, 'list.txt'), 'w') as flist:
      flist.write('id,lat_dd,lon_dd,yr_window,gcm_name,wind_str_option' + chr(10))
      flist.write(text_input + chr(10))
    stationID = text_input.split(',')[0]
    sub.run(["python", "CL_Tool_Standalone.py"], env=env_copy)
    with open(os.path.join(cwd, 'pars', stationID + '.par')) as fpar:
      string = fpar.read()
    return render_template("result.html", text=string)
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
    

