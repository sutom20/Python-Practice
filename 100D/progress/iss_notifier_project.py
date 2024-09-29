import time

import requests
import datetime
import smtplib

my_email = "tomarsam411@gmail.com"
my_pass = "khakra2024"
to_send_email = ["sumittomar909@gmail.com", "nishagup4523@gmail.com"]
tolerance = 5.0
my_lat = 12.971599
my_long = 77.594566
# my position

def is_night_time():
    format_val = 0
    parameters = {
        'lat': my_lat,
        'lng': my_long,
        'formatted': format_val
    }

    response_my_loc = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response_my_loc.raise_for_status()
    data = response_my_loc.json()
    print(data)

    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    # print(sunrise)
    # print(sunset)

    time_now = datetime.datetime.now()
    time_now_hr = time_now.hour
    # print(time_now_hr)

    if sunset < time_now_hr < sunrise:
        return True

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data = response_iss.json()
    print(data)

    longitude_iss = float(data['iss_position']['longitude'])
    latitude_iss = float(data['iss_position']['latitude'])

    lat_upper_limit = my_lat + tolerance
    lat_lower_limit = my_lat - tolerance
    lng_upper_limit = my_long + tolerance
    lng_lower_limit = my_long - tolerance

    if lng_lower_limit < longitude_iss < lng_upper_limit and lat_lower_limit < latitude_iss < lat_upper_limit:
        return True





while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_send_email,
            msg="look up Panda\n\nUp above the world so high\n\nThe ISS is above you in the sky"
        )
