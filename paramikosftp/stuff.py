farm = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def validate_name(validation, element):
    try:
        return validation.index(element)
    except:
        return -1

def extract_farms_from_list(farms):
    location = []
    for farm in farms:
        location.append(farm["name"].lower())
    return location

def nightmare(farm, exclusion, query): 
    location = extract_farms_from_list(farm)
    where = validate_name(location, query.lower())
    if where < 0:
        print("Not a valid location")
        return
    for animal in farm[where]["agriculture"]:
        if animal in exclusion: continue
        print(animal)

def nightmare_carnivore(farm, query):
    nightmare(farm, ["carrots", "celery"], query)

def nightmare_vegitarian(farm, query):
    nightmare(farm, ["sheep", "cows", "pigs", "chickens", "llamas", "cats"],query)

#query_veg = input("enter secret farm location: ")
#nightmare_vegitarian(farm, query_veg)

query = input("Enter NE farm, W farm, or SE farm to see its anaimls: ")
nightmare_carnivore(farm, query)

