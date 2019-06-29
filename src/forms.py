from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class ConfigMapForm(FlaskForm):
    """Creates a WTForm to create a new ConfigMap object"""
    auth_type = SelectField('Authentication Type',
                            choices=[('httpd_auth', 'HTPasswd file based authentication'),
                                     ('saml', 'SAML Provider Authentication'),
                                     ('oid', 'OpenID (Github/Social media login)')],
                            validators=[DataRequired()])
    workshop_name = StringField('Workshop Name',
                                validators=[DataRequired()])
    submit = SubmitField('Create New Configuration')


class DeleteConfigMapForm(FlaskForm):
    """Removes an existing ConfigMap object"""
    submit = SubmitField('Remove Current Configuration')
