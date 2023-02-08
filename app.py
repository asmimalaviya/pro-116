# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Asmi" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

my father is very supportive
he allwayas help me 
i love my father 

# define the route to mother webpage
my mom is very good mother
she help me in study
i love my mom

# define the route to friends webpage
my father are very helpfull 
they do not leave me alone 
they play with me 

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
