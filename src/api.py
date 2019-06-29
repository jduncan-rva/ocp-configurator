from flask_restful import Resource, reqparse
import json
import os

api_version = 'v1'
configmap_file = 'configmap.json'

reqparse = reqparse.RequestParser()
reqparse.add_argument('auth_type',
                      type=str,
                      required=False,
                      help="No authentication type provided"
                      )
reqparse.add_argument('workshop_name',
                      type=str,
                      required=False,
                      help="No workshop type specified"
                      )


class ConfigMapAPI(Resource):
    """Gets and existing ConfigMap object or generates a new one, depending on the HTTP Type"""

    def get(self):
        """Retrieves an existing ConfigMap object"""
        if os.path.exists(configmap_file):
            with open(configmap_file, 'r') as configmap_data:
                return json.load(configmap_data)

        else:
            return {'configmap': 'No ConfigMap present'}, 400

    def post(self):
        """Creates a new ConfigMap"""
        args = reqparse.parse_args()
        configmap_data = {
            'kind': 'ConfigMap',
            'apiVersion': api_version,
            'metadata': {'name': 'configurator-configmap'},
            'data': {
                'auth_type': args['auth_type'],
                'workshop_name': args['workshop_name']
            }
        }

        with open(configmap_file, 'w') as outfile:
            json.dump(configmap_data, outfile)

        return {'configmap': configmap_data}, 201

    def delete(self):
        """Removes an existing ConfigMap"""
        if os.path.exists(configmap_file):
            os.remove(configmap_file)

            return {'configmap': 'configmap deleted'}, 200

        else:
            return {'configmap': 'No ConfigMap present'}, 400
