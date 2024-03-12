import os
from flask import Flask, request

from constants import menu_list, medical_facilities, accommodation_options, food_options, transport_options, hospitals, \
    pharmacies, clinics, hotels, lodges, guest_houses, restaurants, fast_foods, cafeterias, taxis, buses, boda_bodas, \
    endpoints

app = Flask(__name__)


@app.route("/ussd", methods=["POST"])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", None)

    if text == "":
        # This is the first request. Note how we start the response with CON
        response = "CON What service do you need? \n"
        i = 0
        for service in menu_list:
            response += f"{i}. {menu_list[i]}\n"
            i += 1

    elif text == "0":
        # Business logic for first level response
        response = "CON Choose medical service you need: \n"
        i = 0
        for service in medical_facilities:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "1":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose accommodation service you need: \n"
        i = 0
        for service in accommodation_options:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "2":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Food service you need: \n"
        i = 0
        for service in food_options:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "3":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Transport service you need: \n"
        i = 0
        for service in transport_options:
            response += f"{i}. {service}\n"
            i += 1

    # SECOND LAYER
    # MEDICAL FACILITIES
    elif text == "0*0":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose hospital you need: \n"
        i = 0
        for service in hospitals:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "0*1":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Pharmacy you need: \n"
        i = 0
        for service in pharmacies:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "0*2":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Clinic you need: \n"
        i = 0
        for service in clinics:
            response += f"{i}. {service}\n"
            i += 1

    # ACCOMMODATION FACILITIES
    elif text == "1*0":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Hotel you need: \n"
        i = 0
        for service in hotels:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "1*1":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Lodge you need: \n"
        i = 0
        for service in lodges:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "1*2":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Guest House you need: \n"
        i = 0
        for service in guest_houses:
            response += f"{i}. {service}\n"
            i += 1

    # FOOD FACILITIES
    elif text == "2*0":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Restaurant you need: \n"
        i = 0
        for service in restaurants:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "2*1":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Fast Food you need: \n"
        i = 0
        for service in fast_foods:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "2*2":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Cafeteria you need: \n"
        i = 0
        for service in cafeterias:
            response += f"{i}. {service}\n"
            i += 1

    # TRANSPORT OPTIONS
    elif text == "3*0":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Taxi you need: \n"
        i = 0
        for service in taxis:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "3*1":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Bus you need: \n"
        i = 0
        for service in buses:
            response += f"{i}. {service}\n"
            i += 1

    elif text == "3*2":
        # This is a terminal request. Note how we start the response with END
        response = "CON Choose Bus you need: \n"
        i = 0
        for service in boda_bodas:
            response += f"{i}. {service}\n"
            i += 1
        
    elif text in endpoints:
        response = f"END Thank you for reaching out.\n Your service has been booked. \n"

    else:
        response = "END Invalid choice"

    # Send the response back to the API
    return response


if __name__ == "__main__":
    app.run(debug=True)
