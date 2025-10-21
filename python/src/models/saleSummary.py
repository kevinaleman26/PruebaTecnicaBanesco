from dataclasses import dataclass
from .sale import Sale

@dataclass
class SaleSummary:
    total_units_sold: int
    total_revenue: float

    def __init__(self, sale_list):
        unit_list = []
        total_list = []
        for usuario in sale_list.values.tolist():
            unit_list.append(usuario[4])
            total_list.append(usuario[6])
            
        self.total_units_sold = self.total_units(unit_list)
        self.total_revenue = self.total_revenue(total_list)
        
    def total_units(self, unit_list):
        return sum(unit_list)
    
    def total_revenue(self, total_list):
        return sum(total_list)
        

    def __repr__(self):
        return f"SaleSummary(total_units_sold='{self.total_units_sold}', total_revenue='{self.total_revenue}')"