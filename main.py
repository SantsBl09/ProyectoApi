import ui.user_interface as ui
import api.api_client as api

def menu():
    while True:
        print("Bienvenido al menú de opciones:\n1. Obtener datos de la API\n2. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion != "1" and opcion != "2":
            print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == "1":
            # 1. Pedir entradas 
            departamento, limite = ui.pedir_datos()
            print(f"\nConsultando {limite} registros de {departamento}...")
            
            # 2. Consultar API
            df = api.consultar_casos_covid(departamento, limite)
            
            # 3. Mostrar tabla formateada
            ui.mostrar_tabla(df)
            
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()