from pydantic import BaseModel
from custypes import Departement, LieuStock


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
    responsable: str
    departement: Departement
    lieu_stockage: LieuStock


class KitComplet(KitBase):
    id: int
    nb_pieces: int

    class Config:
        orm_mode = True


class Infos(BaseModel):
    departements: list[str]
    lieux_stock: list[str]

    class Config:
        orm_mode = True


class PiecesKitBase(BaseModel):
    nomenclature_catia: str
    materiau: str
    quantite: int
    id_kit: int
    lien_MEP: str


class PiecesKitComplet(PiecesKitBase):
    id_commande: int | None = None
    id_piece: str | None = None
    lieu_stockage: str | None = None

    class Config:
        orm_mode = True
