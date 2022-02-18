#!/usr/bin/env python3

import requests
import json

class ShapeWayAPI:
    '''
    This will serve as the primary interface to Shapeways.com and will allow
    us to get an estimate for the price of the object
    '''
    def __init__(self,access_token):
        self.headers = {'Authorization': 'Bearer ' + access_token}
        self.payload = {
           'fileName': , // make sure include the correct file extension
           'file': ,
           'description': ,
           'hasRightsToModel': 1,
           'acceptTermsAndConditions': 1
        }
    def uploadFile(self,file,description="Cool stl file!"):
        '''
        This method will upload the .stl file to shapeways
        Input:
            - file: The full filepath including ".stl" of the file to upload
            - description: A description of the stl file being uploaded
        Output:
            - Tuple: (Model ID, Price)
                - Model ID: The model ID as given by shapeways
                - Price: Price as estimated by Shapeways
        '''
        #we want to first open the file
        with open(file, 'rb') as f:
            modelData = model_file.read()
        #extract the name of the file
        #example input: dir1/subdir2/subdir3/example.stl
        name = file.split('/')[-1]
        #Now we can add it to our payload
        self.payload['file'] = base64.b64encode(modelData).decode('utf-8')
        self.payload['fileName'] = name
        self.payload['description'] = description


        response = requests.post(url='https://api.shapeways.com/models/v1', 
                headers=self.headers, data=json.dumps(self.payload))
        response = json.loads(response)

        modelId = response["modelId"]
        price = response['materials']['6']['price']
        
        return modelID,price


        




