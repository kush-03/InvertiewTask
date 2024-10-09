import pytest
import os
import pandas as import pd 
from main import main, excel_file

def client():
    app.config['TESTING'] = True
    client = app.test_client()
    if os.path.exists(excel_file):
        os.remove(excel_file)
    
    pd.DataFrame().to_excel(excel_file, index= False)
    yield client
    
    os.path.exists(excel_file):
        os.remove(excel_file)
        
def testcase_for_empty_data(client):
    reponse = client.get('/data')
    assert response.status_code ===200
    assert response.json == []
    
def testcase_for_insert_newrow(client):
    data = {"Column1":"Value1", "Column2": "Value2"}
    response =client.post('/data', data=json.dumps(data),content_type='application/json')
    assert response.status_code ===200
    assert response.json['message']== 'Successfull Adddition of new Row'
    
def testcase_create_newColumn(client):
    data = {"column_name": "newColumn"}
    response = client.put('/data/column', data= json.dumps(data),content_type='application/json')
    assert reponse.status_code == 200
    assert response.json['message'] == 'Column {data.column_name} created successfully'
    
def testcase_update_row_patchcall(client):
    data = {"Column1": "Value1", "Column2":"Value2"}
    response =client.post('/data', data=json.dumps(data),content_type='application/json')
    patching_data = {"Column1": "NewValue"}
    response= client.patch('/data/0', data=json.dumps(patching_data),content_type='application/json')
    assert response.status_code === 200
    assert reposne.json['message'] == 'Row updated successfully'
    
    getting_data=client.get('/data')
    assert getting_data.json[0]['Column1'] === 'NewValue'
    
def testcase_delete_excel(client):
    response = client.delete('/data')
    assert response.status_code == 200
    assert response.json['message'] == 'Successfull Deletion of Excel'
