import flask, time

app = flask.Flask(__name__)

global is_healthy
is_healthy="1"

@app.route('/')
def index():
    return "Hello"

@app.route('/healthy')
def healthy():
    global is_healthy
    print(is_healthy)
    if is_healthy=="1":
        status=200
        msg = "yes"
    else:
        status=500
        msg = "no"
    return msg , status

@app.route("/sethealthy",methods=['GET', 'POST'])
def sethealthy():
    global is_healthy
    is_healthy=flask.request.args.get("set")
    return "ok"

@app.route('/ready')
def ready():
    time.sleep(30) #simlating connection to database
    return 'ready',200

if __name__ == "__main__":
    app.run(debug=True, port=5555,host='0.0.0.0')