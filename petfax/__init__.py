from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    # pets index route
    @app.route('/pets')
    def pets(): 
        return 'These are our pets available for adoption!'
    
    @app.route('/pets/adopt')
    def adopt():
        return 'This is where you can adopt a pet'



    return app
