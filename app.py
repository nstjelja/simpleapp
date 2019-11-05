import flask, time, os

app = flask.Flask(__name__)

def write_health(health):
    f = open("health.db","w")
    f.write(health)
    f.close()

def read_health():
    if not os.path.exists("health.db"):
        write_health("1")
    f = open("health.db","r")
    health = f.read()
    f.close()
    return health

@app.route('/')
def index():
    return "Hello"

@app.route('/healthy')
def healthy():
    is_healthy = read_health()
    if is_healthy=="1":
        status=200
        msg = "yes"
    else:
        status=500
        msg = "no"
    return msg , status

@app.route("/sethealthy",methods=['GET', 'POST'])
def sethealthy():
    write_health(flask.request.args.get("set"))
    return "ok"

@app.route('/ready')
def ready():
    time.sleep(30) #simlating connection to database
    return 'ready',200

if __name__ == "__main__":
    app.run(debug=True, port=5555,host='0.0.0.0')