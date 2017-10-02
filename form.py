from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route("/")
def root():
	query = request.args.get('name')
	return render_template("form.html", ret=query)
	
if __name__ == "__main__":
	my_app.debug = True
	my_app.run()