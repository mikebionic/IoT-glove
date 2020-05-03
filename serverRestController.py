from flask import Flask,render_template,url_for,redirect,request,Response
app = Flask (__name__)

sw = 0

@app.route("/")
@app.route("/state")
def state():
	global sw
	return ("switch:"+str(sw))

@app.route("/state/<action>")
def action(action):
	global sw
	sw = action
	return ("switch:"+str(sw))

if __name__ == "__main__":
	app.run(host="0.0.0.0" , port=5000 , debug=True)
	
