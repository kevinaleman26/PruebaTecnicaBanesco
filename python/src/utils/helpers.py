from ..services.order_file import read_orders_csv
from ..services.user import fetch_data_from_api_user
from ..models.user import Usuario

def read_data_from_file():
    orders_df = read_orders_csv()

    if orders_df is None:
        print("\n" + "=" * 50)
        print("No se pudo proceder con el análisis de datos.")
        print("=" * 50)
        return orders_df

    return orders_df


def get_user_data():
    users_data = fetch_data_from_api_user()
    
    if users_data is None:
        print("\n[FIN] No se pudieron obtener los datos de usuario.")
        return None
    
    user_list = [ Usuario(usr) for usr in users_data ]
    
    return user_list

