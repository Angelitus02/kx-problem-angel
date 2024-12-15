# store hardcoded data that can be accessed through a REST GET call in JSON format
from flask import jsonify

class Storage():
#random generated dummy data
    data = [
        {
            'question': 'What is the capital of France?',
            'answer': 'Paris',
            'alternate_answers': ['France', 'Madrid', 'Rome', 'Berlin']
        },
        {
            'question': 'What is the capital of United States?',
            'answer': 'Washington',
            'alternate_answers': ['New York', 'Ontario', 'Las Vegas', 'Los Angeles']
        },
        {
            'question': 'What is the capital of Japan?',
            'answer': 'Tokyo',
            'alternate_answers': ['Kyoto', 'Hiroshima', 'Osaka', 'Sapporo']
        }
    ]

    @classmethod
    def getData(dummy):
        return jsonify(dummy.data)
