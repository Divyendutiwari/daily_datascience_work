from flask import Flask,render_template,jsonify,request
app=Flask(__name__)
items=[
    {"id":1,"name":"stud"},
     {"id":2,"name":"stup"}       
]
@app.route('/')
def home():
    return "welcome to homepage"
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message":"item not found"}),404
    return jsonify(item)
@app.route('/items' ,methods=['POST'])
def create_item():
    if not 'name' in request.json:
        return jsonify({"message":"name is required"}),400
    new_item={
        "id":len(items)+1,
        "name":request.json['name']
    }
    items.append(new_item)
    return jsonify(new_item),201
if __name__=='__main__':
    app.run(debug=True)

    