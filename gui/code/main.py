import json
from flask import Flask, render_template, redirect
from flask_restful import Api
import requests
from forms import ConfigMapForm, DeleteConfigMapForm
from api import ConfigMapAPI

application = Flask(__name__)
application.config['SECRET_KEY'] = 'dh20e8hf982rhfw8hf80923hf8902hf028hf2809hf082hf'
api = Api(application)

api_version = 'v1'
port_number = 8000
api_url = "http://localhost:%s/api/%s/configmap" % (port_number, api_version)


def to_json_pretty(value):
    """Adds a jinja filter to create prettier json output"""

    return json.dumps(value, indent=2, separators=(',', ': '))


application.jinja_env.filters['tojson_pretty'] = to_json_pretty


@application.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    """Renders the index page with an existing config if present, and the form to create a new ConfigMap"""
    form = ConfigMapForm()
    delete_form = DeleteConfigMapForm()
    config_map = requests.get(api_url).json()

    print form.errors
    print delete_form.errors
    if form.validate_on_submit():

        configmap_data = json.dumps({
            "auth_type": form.auth_type.data,
            "workshop_name": form.workshop_name.data
        })

        headers = {'Content-Type': 'application/json'}
        requests.post(api_url, data=configmap_data, headers=headers)

        return redirect('/')

    if delete_form.validate_on_submit():

        requests.delete(api_url)

        return redirect('/')

    return render_template('base.html', form=form, delete_form=delete_form, config_map=config_map)


api.add_resource(ConfigMapAPI, '/api/%s/configmap' % api_version, endpoint='configmap')

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True, port=port_number)
