# app/models.py
from app import db
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Estabelecimento(db.Model):
    """This class represents the Estabelecimento table."""

    __tablename__ = 'estabelecimento'

    idEstabelecimento = db.Column(db.Integer, primary_key=True)
    nmEstabelecimento = db.Column(db.String(255))
    nrCodigoOficial = db.Column(db.String(255))
    idPais = db.Column(db.Integer)
    idUf = db.Column(db.Integer)
    idMunicipio = db.Column(db.Integer)
    nmLocalidade = db.Column(db.String(255))
    nrLatitude = db.Column(db.Float)
    nrLongitude = db.Column(db.Float)
    stAtivo = db.Column(db.Boolean)
    idCliente = db.Column(db.Integer)
    # produtores
    # ueps
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, nmEstabelecimento):
        """initialize with nmEstabelecimento."""
        self.nmEstabelecimento = nmEstabelecimento

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Estabelecimento.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Estabelecimento: {}>".format(self.nmEstabelecimento)


class Produtor(db.Model):
    """This class represents the Produtor table."""

    __tablename__ = 'produtor'

    idProdutor = db.Column(db.Integer, primary_key=True)
    nrDocumento = db.Column(db.String(255))
    nmProdutor = db.Column(db.String(255))
    nrTelefone = db.Column(db.String(255))
    dsEmail = db.Column(db.String(255))
    # cdEstabelecimento = db.Column(db.Integer)
    # estabelecimento = 

    # Estabelecimento (Many-to-One relationship)
    cdEstabelecimento = Column(Integer, ForeignKey('estabelecimento.idEstabelecimento'))
    estabelecimento = relationship("Estabelecimento", backref=db.backref("produtores", uselist=False))
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, nmProdutor):
        """initialize with nmProdutor."""
        self.nmProdutor = nmProdutor

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Produtor.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Produtor: {}>".format(self.nmProdutor)

class UnidadeExploracao(db.Model):
    """This class represents the UnidadeExploracao table."""

    __tablename__ = 'unidadeExploracao'

    idUnidadeExploracao = db.Column(db.Integer, primary_key=True)
    nrUnidadeExploracao = db.Column(db.Integer)
    cdEstabelecimento = db.Column(db.Integer)
    qtCapacidadeAlojamento = db.Column(db.Integer)
    csTipoUnidadeExploracao = db.Column(db.String(255))
    stAtiva = db.Column(db.Boolean)
    csTipoAnimal = db.Column(db.String(2))

    # Estabelecimento (Many-to-One relationship)
    cdEstabelecimento = Column(Integer, ForeignKey('estabelecimento.idEstabelecimento'))
    estabelecimento = relationship("Estabelecimento", backref=db.backref("ueps", uselist=False))
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, nrUnidadeExploracao):
        """initialize with nrUnidadeExploracao."""
        self.nrUnidadeExploracao = nrUnidadeExploracao

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return UnidadeExploracao.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<UnidadeExploracao: {}>".format(self.nrUnidadeExploracao)