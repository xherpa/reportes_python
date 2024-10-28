from database.querys import insert_datos,extraccion_ids_frontier
from hubspot_extract import disponibilidad_por_AdId

filters = [
        {
            "filtros": [{
                "pagina": "Frontier",
                "facebook_page": ['Frontier Services'],
                "filter": [{
                    "fibra": ["Frontier"],

                    "dsl": ["Frontier DSL"],

                    "salesFibra": ["Fiber"],

                    "salesDsl": ["DSL"],

                    "fibrasATFrontier": ["300 Mbps", "500 Mbps", "Fiber", "2000 Mbps", "5000 Mbps"],

                    "dslATFrontier": ["25 Mbps", "50 Mbps", "75 Mbps", "100 Mbps"],

                    "OthersCompanies": ["Xmart Fi", "25 Mbps", "50 Mbps", "75 Mbps", "100 Mbps", "300 Mbps", "500 Mbps", "Fiber", "2000 Mbps", "5000 Mbps", "Internet Frontier"],

                    "creditCheck": ["Frontier - 1000 Mbps", "Frontier - 200 Mbps", "Frontier - 2000 Mbps", "Frontier - 300 Mbps", "Frontier - 500 Mbps", "Frontier - 5000 Mbps"],
                    }]
                }]
            }
        ]



def frontier (date_start, date_stop, date_start_original, date_stop_original): 
    ad_id = extraccion_ids_frontier(date_start_original,date_stop_original)

    for id in ad_id:
        for page in filters:
            pagina = page["filtros"][0]["pagina"]
            facebook_page = page["filtros"][0]["facebook_page"]
            tipo = page["filtros"][0]["filter"]

            if pagina == "Frontier":
                for type in tipo[0]:
                    try:
                        if type.find("sales") != 0:
                            result = disponibilidad_por_AdId(tipo[0][type],id[1],f"{date_start}Z",f"{date_stop}Z")

                            insert_datos(type,result,"Frontier",id[1],date_start_original,date_stop_original)
                            # print("Total:",result)
                        else:
                            result = ventas_por_AdId(tipo[0][type],id[1],f"{date_start}Z",f"{date_stop}Z")

                            insert_datos(type,result,"Frontier",id[1],date_start_original,date_stop_original)
                            # print("Total:",result)
                    except:
                        print("")

    print("Disponibilidades y ventas listas")

    for id in ad_id:
        for page in filters:
            pagina = page["filtros"][0]["pagina"]
            facebook_page = page["filtros"][0]["facebook_page"]
            tipo = page["filtros"][0]["filter"]

            if pagina == "Credit Check":
                for type_credit in tipo[0]:
                    try:
                        result = chequeos_de_credito_por_AdId(f"{date_start}Z",f"{date_stop}Z",id[1])

                        insert_datos(type_credit,result,"Frontier",id[1],date_start_original,date_stop_original)
                        # print("Total:",result)
                    except:
                        print()

    print("Chequeos de credito listos")
    
    for id in ad_id:
        for page in filters:
            pagina = page["filtros"][0]["pagina"]
            facebook_page = page["filtros"][0]["facebook_page"]
            tipo = page["filtros"][0]["filter"]



            if pagina == "Others Companies":
                for type_other_companies in tipo[0]:
                    try:
                        result = ventas_de_others_companies(tipo[0]['sales_others_companies'],f"{date_start}Z",f"{date_stop}Z",id[1])

                        insert_datos(type_other_companies,result,"Home Services",id[1],date_start_original,date_stop_original)
                        # print("Total:",result)
                    except:
                        print()

    print("Others Companies listos")



    return "Datos extraidos con exito"
