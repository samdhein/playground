from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def level_one():
    return render_template("index.html", color="blue", num=3)	# return three 

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", color="blue", num=num)	# return rum 

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", color=color, num=num)	# return rum 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.