from datetime import date
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date

from database import Base
from custypes import *

class Membre(Base):
    __tablename__ = "membre"
    id: int = Column(Integer, primary_key=True)
    nom: str = Column(String, nullable=False)
    prenom: str = Column(String, nullable=False)
    trigramme: str = Column(String, nullable=False)
    pw_hash: str = Column(String, nullable=False)
    role : int = Column(Integer, nullable=False)
    mail : str = Column(String, nullable=False)

class Commande(Base):
    __tablename__ = "commande"
    id: int = Column(Integer, primary_key=True)
    responsable: int = Column(ForeignKey("membre.id"), nullable=False)
    fournisseur: str = Column(String, nullable=False)
    prix: float = Column(Float, nullable=False)
    poids: float = Column(Float, nullable=False)
    description: str = Column(String, nullable=False)
    contact: str = Column(String, nullable=False)
    lien_bon : str = Column(String, nullable=False)
    lieu_stockage: str = Column(String, nullable=True)
    budget: int = Column(Integer, nullable=True)
    statut: int = Column(Integer, nullable=True)
    commentaire_dirfin: str = Column(String, nullable=True)
    numero_centrale: str = Column(String, nullable=True)

class Kit(Base):
    __tablename__ = "kit"
    id: int = Column(Integer, primary_key=True)
    nom: str = Column(String, nullable=False)
    nb_pieces: int = Column(Integer, nullable=False)
    responsable: int = Column(ForeignKey("membre.id"), nullable=False)
    departement: str = Column(String)
    lieu_stockage: str = Column(String)

class PieceReelle(Base):
    __tablename__ = "piece_reelle"
    reference: str = Column(String, primary_key=True)
    nom: str = Column(String, nullable=False)
    quantite: int = Column(Integer, nullable=False)
    lien_achat: str = Column(String, nullable=False)
    prix: float = Column(Float, nullable=False)
    poids: float = Column(Float, nullable=False)
    fabricant: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)

class piece_conception(Base):
    __tablename__ = "piece_conception"
    nomenclature_catia: str = Column(String, primary_key=True)
    id_commande: int = Column(ForeignKey("commande.id"),nullable=False)
    id_piece: str = Column(ForeignKey("piece_reelle.reference"),nullable=False)
    materiau: str = Column(String, nullable=False)
    quantite: int = Column(Integer, nullable=False)
    id_kit: int = Column(ForeignKey("kit.id"), nullable=False)
    lieu_stockage: str = Column(String)
    lien_MEP: str = Column(String)

class DetailCommande(Base):
    __tablename__ = "detail_commande"
    id_commande: int = Column(ForeignKey("commande.id"), primary_key=True)
    id_piece_reelle: str = Column(ForeignKey("piece_reelle.reference"), primary_key=True)
    quantite: int = Column(Integer, nullable=False)
    date_livraison: date = Column(Date, nullable=False)
    lieu_stockage: str = Column(String)
    etat_verif: str = Column(String)

class HistoriqueCommande(Base):
    __tablename__ = "historique_commande"
    id_commande: int = Column(ForeignKey("commande.id"), primary_key=True)
    id_update: int = Column(Integer, primary_key=True)
    date_edition: date = Column(Date, nullable=False)
    action: str = Column(String, nullable=False)
    acteur: int = Column(ForeignKey("membre.id"), nullable=False)
    lieu_stockage: str = Column(String)
    budget: int = Column(Integer)
    description: str = Column(String)