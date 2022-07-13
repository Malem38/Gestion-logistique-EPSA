from pydantic import BaseModel
from custypes import *


class PiecesReelles(BaseModel):
    reference: str
    nom: str
    quantite: int
    lien_achat: str
    prix: float
    poids: float
    fabricant: str
    description: str


class PiecesComplet(PiecesReelles):
    nombre_commande: int
    nombre_reel: int

    class Config:
        orm_mode = True


class KitBase(BaseModel):
    nom: str
    nb_pieces: int
    responsable: str
    departement: Departement
    lieu_stock: LieuStock


class KitComplet(KitBase):
    id: int

    class Config:
        orm_mode = True
