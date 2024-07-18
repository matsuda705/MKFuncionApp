import json
import logging

import azure.functions as func

from create_dummy_data import CreateDummyData


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="get_current_data")
def get_current_data(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    create_dummy_instance = CreateDummyData()
    get_current_data = create_dummy_instance.create_all_data()

    return func.HttpResponse(
        json.dumps(get_current_data),
        status_code=200
    )
