from wtforms import Form, StringField, SelectField

class TelephoneSearchForm(Form):
    choices = [('Country', 'Country'),
               ('Region', 'Region'),
               ('Local Exchange', 'Local Exchange'),
               ('SLID', 'SLID'),
               ('Extension', 'Extension')]
    select = SelectField('Search for phone number:', choices=choices)
    search = StringField('')
