from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_manager import UsersManager

ORIGIN_IATA_CODE = "LON"
MIN_NIGHTS_IN_DST = 7
MAX_NIGHTS_IN_DST = 28

sheet_manager = DataManager()
flight_search_manager = FlightSearch()
notification_manager = NotificationManager()
users_manager = UsersManager()

sheet_data = sheet_manager.get_destination_data()
users_emails = users_manager.get_users_emails()

print(sheet_data)

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = flight_search_manager.get_destination_code(city["city"])
        city_id = city["id"]
        city_iata_code = city["iataCode"]
        sheet_manager.update_city_iata_code(city_id=city_id,
                                            iata_code=city_iata_code)
    origin_city_code = ORIGIN_IATA_CODE
    destination_city_code = city["iataCode"]
    now = datetime.now()
    from_time = now.date().strftime("%d/%m/%Y")
    to_time = (now.date() + timedelta(days=180)).strftime("%d/%m/%Y")
    min_nights_in_dst = MIN_NIGHTS_IN_DST
    max_nights_in_dst = MAX_NIGHTS_IN_DST
    flight_data = flight_search_manager.check_for_flights(origin_city_code=origin_city_code,
                                                          destination_city_code=destination_city_code,
                                                          from_time=from_time,
                                                          to_time=to_time,
                                                          min_nights_in_dst=min_nights_in_dst,
                                                          max_nights_in_dst=max_nights_in_dst)
    if flight_data is None:
        print("MESSAGE: flight_data is empty")
        continue

    # if flight_data.price < city["lowestPrice"]:
    #     print("Message will be sent")
    #     print(f"{flight_data.destination_city}: £{flight_data.price}")
    #     message_to_send = f"Only {flight_data.price} pounds to fly from " \
    #                       f"{flight_data.origin_city}-{flight_data.origin_airport}" \
    #                       f" to {flight_data.destination_city}-{flight_data.destination_airport}," \
    #                       f"from {flight_data.out_date} to {flight_data.return_date}"
    #     notification_manager.send_message(message=message_to_send)
    #
    #     for user_email in users_emails:
    #         notification_manager.send_email(recipient_email=user_email, message=message_to_send)
    # else:
    #     print("Message will not be sent")

    print(f"{flight_data.destination_city}: £{flight_data.price}")
    message_to_send = f"Only {flight_data.price} pounds to fly from " \
                      f"{flight_data.origin_city}-{flight_data.origin_airport}" \
                      f" to {flight_data.destination_city}-{flight_data.destination_airport}," \
                      f"from {flight_data.out_date} to {flight_data.return_date}"
    notification_manager.send_message(message=message_to_send)

    for user_email in users_emails:
        notification_manager.send_email(recipient_email=user_email, message=message_to_send)

sheet_manager.set_destination_data(destination_data=sheet_data)
