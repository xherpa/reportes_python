# from hubspot_extract import disponibilidad_por_AdId, ventas_por_AdId, chequeos_de_credito_por_AdId
from database.querys import extraccion_ids_is, insert_datos
from hubspot_extract import chequeos_de_credito_por_AdId, disponibilidad_por_AdId, ventas_de_others_companies, ventas_por_AdId

filters = [
    {
    "filtros": [{ 
        "pagina": "AT&T-Hs",
        "facebook_page": ['Internet Services','Internet Deals'],
        "filter": [{
        "fibra": ["Fiber"],   
        "dsl": ["25-75 Mb", "100"],   
        "sales_fibra": ["300 Mbps", "500 Mbps", "Fiber", "2000 Mbps", "5000 Mbps"],    
        "sales_dsl": ["25 Mbps", "50 Mbps", "75 Mbps", "100 Mbps"] 
        }]
    }],   
    },
    {
    "filtros": [{
        "pagina": "Credit Check",
        "facebook_page": ['Internet Services','Internet Deals'],
        "filter": [
        { "credit_checks": ['AT&T - Fiber 1000 Mbps', 'AT&T - Fiber 5000 Mbps'] }
        ]
    }]
    },
    {
    "filtros": [{
        "pagina": "Others Companies",
        "facebook_page": ['Internet Services', 'Internet Deals'],
        "filter": [
        { "sales_others_companies": ['Frontier Upgrade', 'Internet Frontier', 'Internet WindStream', 'Internet Spectrum', 'Spectrum 500 Mbps', 'Spectrum 300 Mbps', 'Spectrum 100 Mbps', 'Spectrum 50 Mbps', 'Wireless Spectrum', 'spectrum_600_mbps', 'Other Int. (Opus)', 'Vivint', 'WOW 100', 'WOW 200', 'WOW 300', 'WOW 500', 'WOW 600', 'WOW 1 Gig', 'WOW 1.2 Gig', 'Ziply', 'Optimum 100 Mbps', 'Optimum 200 Mbps', 'Optimum 300 Mbps', 'Optimum 500 Mbps', 'Optimum 1000 Mbps', 'Fidium'] }
        ]
    }]
    }
]

def internet_services (date_start, date_stop,date_start_original, date_stop_original):
    ad_id = extraccion_ids_is(date_start_original,date_stop_original)
    for id in ad_id:
        for page in filters:
            pagina = page["filtros"][0]["pagina"]
            facebook_page = page["filtros"][0]["facebook_page"]
            tipo = page["filtros"][0]["filter"]
            
            
            if pagina == "AT&T-Hs":
                for type in tipo[0]:
                    try:
                        if type.find("sales") != 0:
                            result = disponibilidad_por_AdId(tipo[0][type],id[1],f"{date_start}Z",f"{date_stop}Z")

                            insert_datos(type,result,"Internet Service",id[1],date_start_original,date_stop_original)
                            # print("Total:",result)
                        else:
                            result = ventas_por_AdId(tipo[0][type],id[1],f"{date_start}Z",f"{date_stop}Z")

                            insert_datos(type,result,"Internet Service",id[1],date_start_original,date_stop_original)
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
                        
                        insert_datos(type_credit,result,"Internet Service",id[1],date_start_original,date_stop_original)
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

                        insert_datos(type_other_companies,result,"Internet Service",id[1],date_start_original,date_stop_original)
                        # print("Total:",result)
                    except:
                        print()
                    
    print("Others Companies listos")

    return "Datos extraidos con exito"