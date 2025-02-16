from flask import Flask, render_template, request, redirect, url_for
from models import db, OneTb, NTb, get_table_info

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create a new 1Tb record
        name = request.form['name']
        new_record = OneTb(name=name)
        db.session.add(new_record)
        db.session.commit()

        #nrelations = NTb.query.all()


        return redirect(url_for('index'))

    # Fetch all 1Tb records
    records = OneTb.query.all()

    nrelations = NTb.query.all()

    return render_template('index.html', records=records, nrelations=nrelations)

@app.route('/nrelations/<int:one_tb_id>', methods=['GET', 'POST'])
def nrelations(one_tb_id):
    if request.method == 'POST':
        # Create a new nTb record
        description = request.form['description']
        new_n_relation = NTb(description=description, one_tb_id=one_tb_id)
        db.session.add(new_n_relation)
        db.session.commit()
        return redirect(url_for('index'))

    table_info = get_table_info('nTb')
    return render_template('nrelations.html', one_tb_id=one_tb_id, table_info=table_info)

if __name__ == '__main__':
    app.run(debug=True)
