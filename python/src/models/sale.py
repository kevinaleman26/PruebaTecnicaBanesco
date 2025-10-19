from dataclasses import dataclass

@dataclass
class Sale:
    units: float
    unit_cost: float
    total: float
    
    def __init__(self, units, unit_cost, total):
        self.units = units
        self.unit_cost = unit_cost
        self.total = total
        
    def sale_calculation(self):
        self.total = self.units * self.unit_cost
        
    def __repr__(self):
        return f"Sale(units='{self.units}', unit_cost='{self.unit_cost}', total='{self.total}')"