from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

chama=[
    {
    "id": 1,
    "name":"Narc-Kenya",
    "hqAddress":"Thika Road",
    "logoUrl":"users/pivs/jubile.jpg"
},
{
    "id": 2,
    "name":"ODM",
    "hqAddress":"Thika Road",
    "logoUrl":"users/pivs/jubile.jpg"
},
{
    "id": 3,
    "name":"Narc",
    "hqAddress":"Thika Road",
    "logoUrl":"users/pivs/jubile.jpg"
}
]
    
offices=[
    {
    "id":101,
    "type":"Local",
    "name":"presidential"
},
{
    "id":102,
    "type":"Executive",
    "name":"Legislature"
},
{
    "id":103,
    "type":"Local",
    "name":"Nothing"
}
]


    

@app.route('/parties')
def get_all_parties():
    return jsonify({"parties":chama})

@app.route('/parties', methods=['POST'])
def create_party():
    request_data=request.get_json()
    new_party={

            
            "id":request_data['id'],
            "name":request_data["name"],
            "hqAddress":request_data["hqAddress"],
            "logoUrl":request_data["logoUrl"]          
       
    }
    chama.append(new_party)
    return make_response(jsonify({
        "Messge":"Party create successfully",
        "Party name": new_party['name']
    }), 201)

@app.route('/parties/<string:name>', methods=['GET'])
def get_specific_party(name):
    for cham in chama:
        if cham['name']==name:
            return jsonify(cham)
    return jsonify({"Message":"Chama not found"})

@app.route('/parties/<int:id>', methods=['GET'])
def get_specific_party_byID(id):
    for ch in chama:
        if ch['id']==id:
            return jsonify(ch)
    return jsonify({"Message":"Chama not found"})

@app.route('/party/<int:id>', methods=['PATCH'])
def edit_specific_party(id):
    request_data=request.get_json()
    updateparty={
        
        'name':request_data['name']
        

    }
    chama.append(updateparty)
    return jsonify(updateparty)

@app.route('/party/', methods=['DELETE'])
def delete_specific_party():
    pass

@app.route('/offices', methods=['POST'])
def create_office():
    request_data=request.get_json()
    newoffice={
        "ID":request_data['ID'],
        "Type":request_data["Type"],
        "Name":request_data["Name"]

    }
    offices.append(newoffice)
    return jsonify(newoffice)



@app.route('/offices')
def get_all_office():
    return jsonify({"offices":offices})
    
@app.route('/offices/<int:id>', methods=['GET'])
def get_specific_office(id):
    for office in offices:
        if office['id']==id:
            return jsonify(office)
    return jsonify({"Message":"Office Data not found"})

@app.route('/offices/<int:id>', methods=['DELETE'])
def delete_specific_office(id):
    for office in offices:
        if office['id']==id:
            return jsonify({"Message":"Deleted successfully"})
    return jsonify({"Message":"Nothing to delete"})

if __name__ == '__main__':
    app.run(debug=True)

