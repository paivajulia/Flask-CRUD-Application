from flask import Flask,request,render_template, redirect
from model import db, BoxModel

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boxes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        box_id = request.form['box_id']
        name_box = request.form['name_box']
        size_box = request.form['size_box']
        description_box = request.form['description_box']
        box = BoxModel(
            box_id=box_id, 
            name_box=name_box, 
            size_box=size_box, 
            description_box = description_box
            )
        db.session.add(box)
        db.session.commit()
        return redirect('/data')


@app.route('/data')
def RetrieveDataList():
    boxes = BoxModel.query.all()
    return render_template('datalist.html',boxes = boxes)

@app.route('/data/<int:id>')
def RetrieveSingleBox(id):
    box = BoxModel.query.filter_by(box_id=id).first()
    if box:
        return render_template('data.html', box = box)
    return f"Box with id ={id} Doenst exist"

@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    box = BoxModel.query.filter_by(box_id=id).first()
    if request.method == 'POST':
        if box:
            db.session.delete(box)
            db.session.commit()
 
            name_box = request.form['name_box']
            size_box = request.form['size_box']
            description_box = request.form['description_box']
            box = BoxModel(box_id=id, name_box=name_box, size_box=size_box, description_box = description_box)
 
            db.session.add(box)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Box with id = {id} Does nit exist"
 
    return render_template('update.html', box = box)

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    box = BoxModel.query.filter_by(box_id=id).first()
    if request.method == 'POST':
        if box:
            db.session.delete(box)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')

app.run(host='localhost', port=5000)