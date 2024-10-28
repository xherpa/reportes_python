import hubspot
from hubspot.crm.contacts import PublicObjectSearchRequest, ApiException
from dotenv import load_dotenv
import os

HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")

api_client = hubspot.Client.create(access_token=HUBSPOT_TOKEN)


def disponibilidad_por_AdId(availability_grade, ad_id, date_start, date_stop):
    filters = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "availability_grade_",
                        "operator": "IN",
                        "values": availability_grade,
                    },
                    {"propertyName": "ad_id_", "operator": "EQ", "value": ad_id},
                    {
                        "propertyName": "createdate",
                        "operator": "BETWEEN",
                        "value": date_start,
                        "highValue": date_stop,
                    },
                ]
            }
        ]
    )
    try:
        response_api = api_client.crm.contacts.search_api.do_search(
            public_object_search_request=filters
        )
        # pprint(response_api.total)
        # pprint(response_api.results)
        return response_api.total
    except ApiException as e:
        print("Exception when calling search_api->do_search: %s\n" % e)


def ventas_por_AdId(services_sold, ad_id, date_start, date_stop):
    filters = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "services_sold",
                        "operator": "IN",
                        "values": services_sold,
                    },
                    {"propertyName": "ad_id_", "operator": "EQ", "value": ad_id},
                    {
                        "propertyName": "createdate",
                        "operator": "BETWEEN",
                        "value": date_start,
                        "highValue": date_stop,
                    },
                ]
            }
        ]
    )

    try:
        response_api = api_client.crm.contacts.search_api.do_search(
            public_object_search_request=filters
        )
        # pprint(response_api.total)
        # pprint(response_api.results)
        return response_api.total
    except ApiException as e:
        print("Exception when calling search_api->do_search: %s\n" % e)


def chequeos_de_credito_por_AdId(date_start, date_stop, ad_id):
    properties = [
        "firstname",
        "lastname",
        "email",
        "internet_availability",
        "availability_grade_",
        "ad_id_",
        "credit_results",
    ]

    filters = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {"propertyName": "credit_results", "operator": "HAS_PROPERTY"},
                    {"propertyName": "ad_id_", "operator": "EQ", "value": ad_id},
                    {
                        "propertyName": "createdate",
                        "operator": "BETWEEN",
                        "value": date_start,
                        "highValue": date_stop,
                    },
                ]
            }
        ],
        properties=properties,
    )
    resultados = 0

    try:
        total = []
        response_api = api_client.crm.contacts.search_api.do_search(
            public_object_search_request=filters
        )
        if response_api.results != []:
            # print(response_api.results[0].properties['availability_grade_'])
            # print(response_api.results)
            for results in response_api.results:
                print(ad_id)
                print(results, "\n")
                if results.properties["availability_grade_"] == "Fiber":

                    total.append(results.properties["availability_grade_"])
                    resultados = len(total)
                    print(total)
                    print(resultados)

        return resultados
    except ApiException as e:
        print("Exception when calling search_api->do_search: %s\n" % e)


def ventas_de_others_companies(services_sold, date_start, date_stop, ad_id):
    filters = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "services_sold",
                        "operator": "IN",
                        "values": services_sold,
                    },
                    {"propertyName": "ad_id_", "operator": "EQ", "value": ad_id},
                    {
                        "propertyName": "createdate",
                        "operator": "BETWEEN",
                        "value": date_start,
                        "highValue": date_stop,
                    },
                ]
            }
        ]
    )

    try:
        response_api = api_client.crm.contacts.search_api.do_search(
            public_object_search_request=filters
        )
        return response_api.total
    except ApiException as e:
        print("Exception when calling search_api->do_search: %s\n" % e)
