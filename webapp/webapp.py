"flask --app webapp run --debug"
"http://127.0.0.1:5000/"
"testA,40,-111,1974_2013,CCSM4,Search"
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, render_template, request, send_from_directory
import os
import subprocess as sub

env_copy = os.environ.copy()
env_copy["MY_VARIABLE"] = "new_value"

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
#print("Current working directory:", cwd)
#print("Parent directory:", parent_dir)

app = Flask(__name__)

# Set the app root to /cligenpar
app.config['APPLICATION_ROOT'] = '/cligenpar'

# Apply ProxyFix to handle headers from IIS reverse proxy (if needed)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route('/pars/<filename>')
def download_par(filename):
    return send_from_directory(os.path.join(cwd, 'pars'), filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']
        with open(os.path.join(parent_dir, 'GDB-to-Pars-CLIGEN/list.txt'), 'w') as flist:
            flist.write('id,lat_dd,lon_dd,yr_window,gcm_name,wind_str_option' + chr(10))
            flist.write(text_input + chr(10))
        stationID = text_input.split(',')[0]
        result = sub.run(["python", "CL_Tool_Standalone.py"], cwd=cwd, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        par_filename = stationID + '.par'
        par_url = f"cligenpar/pars/{par_filename}"
        par_path = os.path.join(parent_dir, 'GDB-to-Pars-CLIGEN/pars', par_filename)
        try:
            with open(par_path) as fpar:
                string = fpar.read()
        except FileNotFoundError:
            string = f"PAR file '{par_filename}' was not found. Please check your input and try again.  Attempting to open: " + par_path
            par_url = None
        return render_template("result.html", text=string, par_url=par_url)
    return render_template("index.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001, debug=True)

