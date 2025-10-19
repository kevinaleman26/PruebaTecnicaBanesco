from dataclasses import asdict
import json

from src.utils.helpers import read_data_from_file, get_user_data
from src.models.saleUser import SalesUsuarios
from src.models.saleSummary import SaleSummary

def trax_lists():
    full_list = read_data_from_file()

    andrew_list_trx = full_list[full_list['Rep'] == 'Andrews']
    gil_list_trx = full_list[full_list['Rep'] == 'Gill']
    howard_list_trx = full_list[full_list['Rep'] == 'Howard']
    jardine_list_trx = full_list[full_list['Rep'] == 'Jardine']
    jones_list_trx = full_list[full_list['Rep'] == 'Jones']
    kivell_list_trx = full_list[full_list['Rep'] == 'Kivell']
    morgan_list_trx = full_list[full_list['Rep'] == 'Morgan']
    parent_list_trx = full_list[full_list['Rep'] == 'Parent']
    smith_list_trx = full_list[full_list['Rep'] == 'Smith']
    sorvino_list_trx = full_list[full_list['Rep'] == 'Sorvino']
    thompson_list_trx = full_list[full_list['Rep'] == 'Thompson']

    trx_list = [
        andrew_list_trx, 
        gil_list_trx, 
        howard_list_trx,
        jardine_list_trx,
        jones_list_trx,
        kivell_list_trx,
        morgan_list_trx,
        parent_list_trx,
        smith_list_trx,
        sorvino_list_trx,
        thompson_list_trx
    ]
    
    return trx_list


if __name__ == "__main__":
    
    response = []
    for usr, trx_list in zip(get_user_data(), trax_lists()):
        sale_usr = SalesUsuarios(usr, SaleSummary(trx_list))
        response.append(asdict(sale_usr)) 

    with open("python/integration_output.json", "w", encoding="utf-8") as f:
        json.dump(response, f, indent=4, ensure_ascii=False)