
from flask import Flask, redirect, request, render_template,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.members'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "abc" 
db = SQLAlchemy(app)

class Members(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(20), unique = False, nullable = False)
    phone = db.Column(db.String(10),unique=False, nullable = False)

    def __repr__(self):
       return f"id: {self.id}, name : {self.name}, email: {self.email}, phone : {self.phone}"

@app.route('/', methods = ['POST',"GET"])
def main():
    if request.method == 'GET':
       employes = Members.query.all()
  
       return render_template('index.html', employees = employes,)

@app.route('/insert', methods= ['POST','GET'])
def insert():
    if request.method == 'POST':
          name = request.values.get('name')
          email = request.values.get('email')
          number = request.values.get('phone')
          code = Members(name = name, email = email, phone = number)
          db.session.add(code)
          db.session.commit()
          flash('Employe added')
          return redirect('/')

@app.route('/update', methods = ['POST','GET'])
def update():        
    if request.method == 'POST':
        name = request.values.get('name')
        email = request.values.get('email')
        phone = request.values.get('phone')
        id = request.values.get('id')
        employe = Members.query.get(id)
        employe.name, employe.email, employe.phone = name ,email, phone
        db.session.commit()
        flash('Employe updated')
        return redirect('/')    
    
@app.route('/delete/<id>')
def delete(id):
    employe = Members.query.get(id)
    db.session.delete(employe)
    db.session.commit()
    flash('Employe deleted')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)