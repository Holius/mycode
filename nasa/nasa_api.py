#!/usr/bin/env python3
from dummy_data import api_data

def validate_answer(acceptable, answer):
    answer = answer.lower()
    if answer in acceptable:
        return answer
    return "none"


def get_current_key(keys, lookup):
    for key in keys:
        if key in lookup:
            return key


def get_parameter_results(parameters, entity):
    iterations = len(parameters)
    current = entity
    while iterations > 0:
        key = get_current_key(parameters, current.keys())
        current = current[key]
        if isinstance(current, list):
            current = current[0]
        iterations -= 1
        if iterations == 0:
            return current


def get_records(parameters, dates):
    records = []
    for date in dates:
        # record = [date]
        record = []
        for entity in dates[date]:
            # record.append(entity)
            record.append(get_parameter_results(parameters, entity))
        records.extend(record)
    return records


def main(api_data):
    stages = {
        "intro": [
            "query diameter or distance",
            {
                "diameter": ["diameter", "estimated_diameter"],
                "distance": ["distance", "close_approach_data"],
            },
        ],
        "diameter": [
            "largest or smallest",
            {
                "largest": ["unit_diameter", "estimated_diameter_max"],
                "smallest": ["unit_diameter", "estimated_diameter_min"],
            },
        ],
        "distance": [
            "largest or smallest",
            {
                "largest": ["unit_distance", "miss_distance"],
                "smallest": ["unit_distance", "miss_distance"],
            },
        ],
        "unit_diameter": [
            "kilometers, meters, miles, or feet",
            {
                "kilometers": ["outro", "kilometers"],
                "meters": ["outro", "meters"],
                "miles": ["outro", "miles"],
                "feet": ["outro", "feet"],
            },
        ],
        "unit_distance": [
            "astronomical, lunar, kilometers, or miles",
            {
                "astronomical": ["outro", "astronomical"],
                "lunar": ["outro", "lunar"],
                "kilometers": ["outro", "kilometers"],
                "miles": ["outro", "miles"],
            },
        ],
    }
    current = stages["intro"]
    dates = api_data["near_earth_objects"]
    # parameters = ["estimated_diameter", "miles", "estimated_diameter_max"]
    parameters = []
    mode = ""
    while True:
        question, responses = current
        response = validate_answer(responses.keys(), input(f"{question}: "))
        if response != "none":
            if response == "largest" or response == "smallest":
                mode = response
            stage, parameter = responses[response]
            if stage == "outro":
                parameters.append(parameter)
                break
            current = stages.get(stage)
            parameters.append(parameter)
    records = get_records(parameters, dates)
    print(records)
    print(len(records))


main(api_data)

