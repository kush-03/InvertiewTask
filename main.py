from flask import Flask
import pandas as pd
import os

app=Flask(__name__)
excel_file = 'data.xlsx'

def excel_load():
    return pd.read_excel(excel_file)

def excel_save(df):
    df.to_excel(excel_file, index=False)
    
@app.route('/data', methods=['GET'])    
def get_data():
    df = excel_load()
    data = df.to_dict(orient='records')
    return jsonify(data)
    
@app.route('/data', methods=['POST'])
def insert_data():
    df = excel_load()
    row_new = request.json
    df = df.append(row_new)
    excel_save(df)
    return jsonify({'message' : 'Successfull Adddition of new Row'}), 200
  
@app.route('/data', methods=['DELETE']) 
def delete_data():
    df=excel_load()
    df.drop()
    excel_save(df)
    return jsonify({'message' : 'Successfull Deletion of Excel'}), 200

@app.route('/data/column', methods=['PUT'])
def add_column()
    df= excel_load()
    column_name = request.json.get('column_name')
    if column_name in df.column:
        return jsonify({'message': 'Column already exists'}), 400
    df[column_name] = None
    excel_save(df)
    return jsonify({'message' : 'Column {column_name} created successfully'}), 200

@app.route('/data/<int:row_index>', methods=['PATCH'])
def rename_column(row_index):
    df= excel_load()
    if row_index >=len(df):
        return jsonify({'message': 'Row index out of bound error'}), 400
    new_data = request.jsonify
    for col, value in new_data.items():
        if col in df.columns:
            df.at[row_index,col]= value
        else:
            return jsonify({'message': 'Column does not exist'}), 400
        excel_save(df)
        return jsonify({'message': 'Row updated successfully'}), 200
        
if __name__ == '__main__':
    if not os.path.exits(excel_file)
    pd.DataFrame().to_excel(excel_file, index=False)
