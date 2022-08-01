### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(intent_request, slots):
    """
    Defines a delegate slot type response.
    """
    session_attributes = intent_request['sessionAttributes']
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(intent_request, message):
    """
    Defines a close slot type response.
    """

    session_attributes = intent_request['sessionAttributes']
    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": 'Fulfilled',
            "message": {
                'contentType': 'PlainText',
                'content': message
            },
        },
    }
    return response


def validate(age, investment_amount, risk_level):
    if (age is not None) and (parse_int(age) <= 0):
        return build_validation_result(False, 'age', 'Age must be greater than 0 years old. Please try again.')
    elif (age is not None) and (parse_int(age) >= 65):
        return build_validation_result(False, 'age', 'Age must be less than 65 years old. Please try again.')
    elif (investment_amount is not None) and (parse_int(investment_amount) < 5000):
        return build_validation_result(False, 'investmentAmount', 'Investment amount must be greater or equal to 5000. Please try again.')
    elif (risk_level is not None) and (risk_level.lower() not in ['none', 'low', 'medium', 'high']):
        return build_validation_result(False, 'riskLevel', 'Risk level must be None, Low, Medium, or High. Please try again.')
    else:
        return build_validation_result(True, None, 'valid')


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    source = intent_request["invocationSource"]
    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]

    if source == 'DialogCodeHook':

        slots = get_slots(intent_request)
        validated = validate(age, investment_amount, risk_level)
        if not validated["isValid"]:
            slots[validated["violatedSlot"]] = None
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validated["violatedSlot"],
                validated["message"],
            )

        return delegate(intent_request, get_slots(intent_request))

    elif source == "FulfillmentCodeHook":
        # The bot should respond with an investment recommendation based on the selected risk level
        res = 'Based on your personal risk profile, I\'d recommend investing in '
        if risk_level.lower() == 'none':
            res += '100% bonds (AGG) and 0% equities (SPY)'
            return close(intent_request, res)
        elif risk_level.lower() == 'low':
            res += '60% bonds (AGG) and 40% equities (SPY)'
            return close(intent_request, res)
        elif risk_level.lower() == 'medium':
            res += '40% bonds (AGG) and 60% equities (SPY)'
            return close(intent_request, res)
        elif risk_level.lower() == 'high':
            res += '20% bonds (AGG) and 80% equities (SPY)'
            return close(intent_request, res)

### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "recommendPortfolio":
        return recommend_portfolio(intent_request)
    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    return dispatch(event)
