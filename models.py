from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OneTb(db.Model):
    __tablename__ = '1Tb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    n_relations = db.relationship('NTb', backref='1Tb', lazy=True)

class NTb(db.Model):
    __tablename__ = 'nTb'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    one_tb_id = db.Column(db.Integer, db.ForeignKey('1Tb.id'), nullable=False)

def get_table_info(table_name):
    if table_name == '1Tb':
        return {'table_name': '1Tb', 'fields': ['id', 'name']}
    elif table_name == 'nTb':
        return {'table_name': 'nTb', 'fields': ['id', 'description', 'one_tb_id']}
    else:
        return None
