from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from data_loader import fetch_courses
from chatbot import Chatbot

app = Flask(__name__)
api = Api(app)

URL = 'https://brainlox.com/courses/category/technical'
courses = fetch_courses(URL)
chatbot = Chatbot(courses)

class Chat(Resource):
    def post(self):
        data = request.get_json()
        user_input = data.get('message')
        response = chatbot.get_response(user_input)
        return jsonify({'response': response})

api.add_resource(Chat, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
