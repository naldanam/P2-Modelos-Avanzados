#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
from sklearn.externals import joblib
from m09_model_deployment import predict_proba


app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
        title='Price Car Prediction API',
    description='Price Car Prediction API')

ns = api.namespace('predict', 
     description='Price Car Regressor')
   
parser = api.parser()


parser.add_argument('year', type=str, required=True, help='year to be analyzed', location='args')
parser.add_argument('mileage', type=str, required=True, help='mile to be analyzed', location='args')
parser.add_argument('state', type=str, required=True, help='state to be analyzed', location='args')
parser.add_argument('make', type=str, required=True, help='URL to be analyzed', location='args')
parser.add_argument('model', type=str, required=True, help='URL to be analyzed', location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})
@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        
        year= args['year']
        mileage= args['mileage'] 
        state= args['state']
        make= args['make']
        model = args['model']
        
        string  = '{year:' + year + ', mileage:' + mileage +  ', state:' +  state +  ', make:' + make +  ', model:' + model
        print(string)
        
        return {
         "result": predict_proba(year, mileage, state, make, model)
        }, 200

        
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
