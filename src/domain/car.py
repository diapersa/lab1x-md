from dataclasses import dataclass


@dataclass
class Car:
    marca: str
    model: str
    tokenMasina: str
    pretAchizitie: int
    pretVanzare: int

    def __str__(self):
        return f"Marca: {self.marca}, Model: {self.model}, Token Masina: {self.tokenMasina}, Pret Achizitie: {self.pretAchizitie}, Pret Vanzare: {self.pretVanzare}"

    # def __gt__(self, other):
    #     return self.tokenMasina> other.tokenMasina