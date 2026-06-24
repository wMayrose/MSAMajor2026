import flask
from flask import request, jsonify
import student_generator_v2 as sg

#create a flask app object
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the list of student dictionaries based on a search key, and a value
Input: search_key - key in the dictionary we want to check the value of
       search_value - the value of the key we need to match
Output: list of student dictionaries that match the search criteria
"""

def search_dictionary_list(search_key, search_value):
    #get the list of student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    new_search_list = []

    #loop through the dictionaries
    for student_dictionary in student_dictionaries:
        if student_dictionary[search_key].lower() == search_value.lower():
            new_search_list.append(student_dictionary)
    return new_search_list


#create a route/view for the homepage of the application
@app.route('/', methods=["GET"])
def index():
    return "<h1>Student Data API</h1>"

#create endpoint for the functions we will create
#create a route to return all student data
@app.route('/api/students/all', methods = ['GET'])
def api_all():
    #get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

#create a route that returns students in a specific major
#api/major/{major we are looking for}
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major:str):
    #call the search function to get students with this major
    major_students = search_dictionary_list("major", major)
    return jsonify(major_students)

#create a route that returns students of a specific class
#api/class/{the class we are looking for}
@app.route('/api/class/<string:student_class>', methods=['GET'])
def api_students_by_class(student_class:str):
    #call the search function to get students from that class
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)

#create a route that returns a specific student by ID
@app.route('/api/student/ID/<string:ID>', methods=['GET'])
def api_get_student_by_id(ID:str):
    #call the search function to get students from that class
    ID_students = search_dictionary_list("ID", ID)
    return jsonify(ID_students)



#run the application
app.run(debug=True)