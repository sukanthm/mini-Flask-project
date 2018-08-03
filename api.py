dict={}
dict[1]='FIR 1: IPC 304, IPC 302'
dict[2]='FIR 1: IPC 387; FIR 2: IPC 304'
dict[3]='FIR 1: IPC 307; FIR 2: IPC 304; FIR 3: IPC 345, IPC 324'

from flask import Flask,abort,request,redirect,url_for

app = Flask(__name__)

@app.before_request
def limit_remote_addr():
  if request.remote_addr != '172.22.6.45' and request.remote_addr!='172.21.22.30' and request.remote_addr!='172.22.6.207':
    abort(403)

@app.route('/getHistory/<int:id>/')
def getHistory(id):
  return dict.get(id, 'Do not request random guid :@')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('getHistory',id = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('getHistory',id = user))

@app.errorhandler(404)
def page_not_found(error):
    return 'please use the right api syntax :(', 404

@app.errorhandler(500)
def page_not_found(error):
    return 'Do not request random guid :@', 500
	
@app.errorhandler(403)
def page_not_found(error):
    return 'You do not have access to this data :P', 403	
  
if __name__ == '__main__':
   app.run('172.21.22.30',5000)