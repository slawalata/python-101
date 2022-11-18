from flask import Flask, request
from boto3 import resource
import boto3.dynamodb.conditions.Attr

import config

app = Flask(__name__)

AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
REGION_NAME = config.REGION_NAME

resource = resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)


def create_table_movie():
    table = resource.create_table(
        TableName='Movie',  # Name of the table
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # RANGE = sort key, HASH = partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',  # Name of the attribute
                'AttributeType': 'N'  # N = Number (B= Binary, S = String)
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


def write_to_movie(id, title, director):
    movie_table = resource.Table('Movie')
    response = movie_table.put_item(
        Item={
            'id': id,
            'title': title,
            'director': director,
            'upvotes': 0
        }
    )
    return response


def read_from_movie(id):
    movie_table = resource.Table('Movie')

    response = movie_table.get_item(
        Key={'id': id},
        AttributesToGet=['title', 'director']
    )

    return response


def read_from_movie_where(date, shift):
    movie_table = resource.Table('Movie')

    response = movie_table.scan(
        FilterExpression=Attr("Date").eq(date) and Attr("Shift").eq(shift)
    )


def update_in_movie(id, data: dict):
    movie_table = resource.Table('Movie')
    response = movie_table.update_item(
        Key={'id': id},
        AttributeUpdates={
            'title': {
                'Value': data['title'],
                'Action': 'PUT'
            },
            'director': {
                'Value': data['director'],
                'Action': 'PUT'
            }
        },
        # returns the new updated values
        ReturnValues="UPDATED_NEW"
    )
    return response


def upvote_a_movie(id):
    movie_table = resource.Table('Movie')
    response = movie_table.update_item(
        Key={'id': id},
        AttributeUpdates={
            'upvotes': {
                'Value': 1,
                'Action': 'ADD'
            }},

        ReturnValues="UPDATED_NEW"
    )

    response['Attributes']['upvotes'] = int(response['Attributes']['upvotes'])
    return response


def delete_from_movie(id):
    movie_table = resource.Table('Movie')
    response = movie_table.delete_item(
        Key={
            'id': id
        }
    )
    return response


@app.route('/')
def root_route():
    create_table_movie()
    return 'Table created'


@app.route('/movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    response = write_to_movie(data['id'], data['title'], data['director'])
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {'msg': 'Add Movie successful', }
    else:
        return {
            'msg': 'error occurred',
            'response': response
        }


@app.route('/movie/', methods=['GET'])
def get_movie(id):
    response = read_from_movie(id)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        if 'Item' in response:
            return {'Item': response['Item']}
        return {'msg': 'Item not found!'}
    return {
        'msg': 'error occurred',
        'response': response
    }


@app.route('/movie/', methods=['DELETE'])
def delete_movie(id):
    response = delete_from_movie(id)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'msg': 'Delete successful',
        }
    else:
        return {
            'msg': 'error occurred',
            'response': response
        }


@app.route('/movie/', methods=['PUT'])
def update_movie(id):
    data = request.get_json()
    response = update_in_movie(id, data)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'msg': 'update successful',
            'response': response['ResponseMetadata'],
            'ModifiedAttributes': response['Attributes']
        }
    else:
        return {
            'msg': 'error occurred',
            'response': response
        }


@app.route('/upvote/movie/', methods=['POST'])
def upvote_movie(id):
    response = upvote_a_movie(id)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'msg': 'Upvote successful',
            'response': response['ResponseMetadata'],
            'Upvotes': response['Attributes']['upvotes']
        }
    else:
        return {
            'msg': 'error occurred',
            'response': response
        }


if __name__ == "__main__":
    app.run()
