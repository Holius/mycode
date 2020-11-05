import json

file= open("mommas.json", "r").read()

mommas= json.loads(file)

#db = <type dictionary> | query = <type str> | prop = <type str> RETURNS <type None> or <type list>
def get_mommas_property(db, query, prop):
    mommas_list = []
    mommas = db.get(query)
    # handles the case of an invalid query by returning None
    if not isinstance(mommas, list):
        return None
    for momma in mommas:
        mommas_list.append(momma.get(prop))
    return mommas_list


# db = <type dictionary> | query = <type str> | prop = <type str> RETURNS <type None> or <type list>
def query_mommas(db, query, prop):
    if (
        not isinstance(db, dict)
        or not isinstance(query, str)
        or not isinstance(prop, str)
    ):
        return print("query_mommas got a type that it was not expecting.")
    if query != "all":
        return get_mommas_property(db, query, prop)
    # code below handles when query == "all"
    mommas_list = []
    mommas_location = db.keys()
    for location in mommas_location:
        mommas_list.extend(get_mommas_property(db, location, prop))
    return mommas_list


def query_mommas_name(db, query):
    prop = "name"
    return query_mommas(db, query, prop)


# db = <type dict> RETURNS <type list>
def query_mommas_size(db):
    if not isinstance(db, dict):
        return print("query_mommas_size did not receive a dictionary.")
    max = 0
    all_mommas = []
    results = []
    # get all mommma names
    names = query_mommas_name(db, "all")
    # get all momma sizes
    size = query_mommas(db, "all", "estimated_diameter")
    # enumerate gives access to both the index and value in <list names>
    for i, momma in enumerate(names):
        all_mommas.append([names[i], size[i]])
    for momma in all_mommas:
        name, size = momma
        momma_size = size["kilometers"]["diameter_max"]
        if momma_size > max:
            max = momma_size
            results = [[name, momma_size]]
        elif momma_size == max:
            results.append([name, momma_size])
    return results


def main(data):
    valid_location_queries = ["all"]
    valid_location_queries.extend(data.keys())
    response = ""
    while response != "names" and response != "size":
        response = input(
            f"Please type 'names' to query names or 'size' to get biggest momma(s). "
        )
    if response == "names":
        query = ""
        while not query in valid_location_queries:
            query = input(f"Please type " + " or ".join(valid_location_queries) + ". ")
        mommas = query_mommas_name(data, query)
        if query == "all":
            return "All mommas are name " + " ".join(mommas)
        return "The mommas in " + query + " are " + " ".join(mommas)
    elif response == "size":
        query = query_mommas_size(data)
        if len(query) == 1:
            return f"Momma {query[0]} is {query[1]} kilometers big!"
        result = "Mommas "
        for momma in query:
            result += " " + momma[0] + " "
        return result + " at size " + str(query[0][1]) + " kilometers big!"


print(main(mommas))

