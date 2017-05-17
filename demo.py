from flask import Flask, render_template, redirect, url_for, request
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("start.html")


@app.route('/wifi', methods=['POST', 'GET'])
def wifi():
    return render_template('wifi.html')

@app.route('/drop')
def drop():
    return render_template('drop.html')


@app.route('/connectedDevices')
def devices():
    os.system("arp | cat > ~/Desktop/connected.txt")
    os.system("sed -i '1d' ~/Desktop/connected.txt")
    my_dict = {}
    with open("/home/aditya/Desktop/connected.txt", 'r') as f:
        for line in f:
            items = line.split()
            key, values = items[0], items[1:]
            my_dict[key] = values
    return render_template('connectedDevices.html',result = my_dict)

@app.route('/logactivity',methods=['POST','GET'])
def logactivity():
    if request.method == 'POST':
        if request.form['submit'] == 'log_sub':
            myaddr = request.form['log_addr']
            sript = "grep " + myaddr + " /var/log/syslog | cat > ~/Desktop/newlog.txt"
            print(sript)
            os.system(sript)
            content = os.popen("cat ~/Desktop/newlog.txt").read()
        return render_template('logactivity.html',content=content)
    if request.method == 'GET':
        return render_template('logactivity.html')

@app.route('/blockip')
def blockip():
    return render_template('blockedip.html')


@app.route('/blockipadd')
def blockipadd():
    os.system("arp | cat > ~/Desktop/connected.txt")
    os.system("sed -i '1d' ~/Desktop/connected.txt")
    my_dict = {}
    with open("/home/aditya/Desktop/connected.txt", 'r') as f:
        for line in f:
            items = line.split()
            key, values = items[0], items[1:]
            my_dict[key] = values
    return render_template('blockipadd.html',result = my_dict)


if __name__ == '__main__':
    app.run(port=8083)
