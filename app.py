#my flask code to render index.html as the homepage. It sets up the bare minimum code required for a Flask app to serve a basic webpage. Each piece plays a specific role in getting the HGCC homepage to display. 

# - Flask is the main class that creates the web application
# - render_template: this function helps me send HTML files (templates) from my server to the user's web browser

from flask import Flask, render_template

#create an instance of the Flask application
# '__name__' is the special Python variable that gets set to the name of the current module (app.py). 
# Flask uses this to know where to look for resoruce like templates and static files

app = Flask(__name__)

#define a route using the @app.route() decorator
# - a route maps a URL path (like '/' for the homepage) to a Python function. 
# - when a user visits the URL specified in the route, the function immediately below the decorator will be executed

@app.route('/')
def home():
    """This function is executed when a user navigates to the root URL ('/') of the HJCC web app"""
    # use render_template() to find and send the 'index.html' file from my 'templates' folder back to the user's browser. 
    return render_template('index.html')

#This is a standard Python idiom, it checks to see if the script is being run directly (e.g., 'python app.py') as opposed to being imported as a model into another script.

if __name__ == '__main__':
    # Start the flask development server. 
    # debug=True: this enables debug mode.
    # - it reloads the server automatically when you make code changes.
    # - it provides a debugger in teh browser if errors occur. 
    # - NOTE: turn debug=False in product environments for security
    app.run(debug=True)
