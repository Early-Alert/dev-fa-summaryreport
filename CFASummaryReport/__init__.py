import datetime
import logging
import requests
import azure.functions as func
import pytz

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info(f"UCT TIMSTAMP --> {utc_timestamp}")
    
    string_utc = datetime.datetime.fromisoformat(str(utc_timestamp)[:-6])
    
    logging.info(f'Converted UTC Time --> {string_utc.strftime("%B %d, %Y at %H:%M:%S UTC")}')
    
    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # est_time = pytz.timezone('EST')
    # current_eastern_time = datetime.datetime.now(est_time)
    # current_eastern_time_object = datetime.datetime.strftime(current_eastern_time, "%Y-%m-%d %H:%M:%S")
    # logging.info(f"Eastern Time --> {str(current_eastern_time_object)}")


    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    utc_timestamp_object = datetime.datetime.fromisoformat(utc_timestamp)

    if utc_timestamp_object.hour == 13 and utc_timestamp_object.minute >= 25:
        url = "https://ea-weather-endpoints.azurewebsites.net/summary/chick-fil-a/two-days-report"
    elif utc_timestamp_object.hour == 18 and utc_timestamp_object.minute >= 25:
        url = "https://ea-weather-endpoints.azurewebsites.net/summary/chick-fil-a/one-day-report"
    else:
        logging.info("********* NOT TRIGGERING ANYTHING *********")
        logging.info(f"Current Time Is --> {utc_timestamp_object}")

    response = requests.get(url=url)
    return_response = response.text
    logging.info(f"This is the response we get {return_response}")
    logging.info('Python timer trigger function ran at %s', utc_timestamp)


    # url = "https://ea-weather-endpoints.azurewebsites.net/summary/chick-fil-a/"
    # response = requests.get(url=url)
    # return_response = response.text
    # logging.info(f"This is the response we get {return_response}")
    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)

"""
def abc():
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info(f"UCT TIMSTAMP --> {utc_timestamp}")
    
    string_utc = datetime.datetime.fromisoformat(str(utc_timestamp)[:-6])
    
    logging.info(f'Converted UTC Time --> {string_utc.strftime("%B %d, %Y at %H:%M:%S UTC")}')
    
    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # est_time = pytz.timezone('EST')
    # current_eastern_time = datetime.datetime.now(est_time)
    # current_eastern_time_object = datetime.datetime.strftime(current_eastern_time, "%Y-%m-%d %H:%M:%S")
    # logging.info(f"Eastern Time --> {str(current_eastern_time_object)}")


    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    utc_timestamp_object = datetime.datetime.fromisoformat(utc_timestamp)
    print(utc_timestamp_object.hour)


abc()
"""


"""
    url = "https://ea-ss-as-aqi-reports-01-dev.azurewebsites.net/summary/chick-fil-a/"
# https://ea-weather-endpoints.azurewebsites.net/

    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()
    # print("Current UTC Timestamp --> ", utc_timestamp)
    response = requests.get(url=url)
    return_response = response.text
    # print('Python timer trigger function ran at %s', utc_timestamp)
    # print('This is the response we get', return_response)
    logging.info(return_response)
    return return_response
"""

"""

    0 15 20,22 * * *
    url = "https://ea-ss-as-aqi-reports-01-dev.azurewebsites.net/summary/chick-fil-a/"
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info("Current UTC Timestamp --> ", utc_timestamp)
    logging.info("Type of UTC Timestamp --> ", type(utc_timestamp))

    if mytimer.past_due:
        logging.info('The timer is past due!')

    est_time = pytz.timezone('EST')
    logging.info(f"Current Eastern Time is {est_time}")
    response = requests.get(url=url)
    return_response = response.text
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('1- This is the response we get', return_response)


    url_old = "https://ea-ss-as-aqi-reports-01-dev.azurewebsites.net/summary/old-chick-fil-a/"
    response_old = requests.get(url=url_old)
    return_response_old = response_old.text
    logging.info('2- This is the response we get', return_response_old)

    return f"{return_response}\n \n {return_response_old}"
    """

"""
def temp():
    url = "https://ea-ss-as-aqi-reports-01-dev.azurewebsites.net/summary/chick-fil-a/"
    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()
    # print("Current UTC Timestamp --> ", utc_timestamp)
    # print("Type of UTC Timestamp --> ", type(utc_timestamp))

    est_time = pytz.timezone('EST')
    current_eastern_time = datetime.datetime.now(est_time)

    print(f"Current Eastern Time is {current_eastern_time}")
    response = requests.get(url=url)
    return_response = response.text
    # print('Python timer trigger function ran at %s', utc_timestamp)
    # print('This is the response we get', return_response)

    return return_response

print(temp())
"""
