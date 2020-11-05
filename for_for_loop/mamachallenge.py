import json

file= open("mommas.json", "r").read()

mommas= json.loads(file)

# db = <type dictionary> | query = <type str>
def get_mommas_property(db, query, prop):
    # todo no error handling for types here
    mommas_list = []
    mommas = db.get(query)
    if not isinstance(mommas, list):
        return None
    for momma in mommas:
        mommas_list.append(momma.get(prop))
    return mommas_list


# db = <type dictionary> | query = <type str>
def query_mommas(db, query, prop):
    # todo no error handling for types here
    if query != "all":
        return get_mommas_property(db, query, prop)
    mommas_list = []
    mommas_location = db.keys()
    for location in mommas_location:
        mommas_list.extend(get_mommas_property(db, location, prop))
    return mommas_list


def query_mommas_name(db, query):
    prop = "name"
    return query_mommas(db, query, prop)

print(query_mommas_name(mommas, "west_coast_mommas"))
print(query_mommas_name(mommas, "all"))

def query_mommas_size(db):
    max = 0
    all_mommas = []
    results = []

    names = query_mommas_name(db, "all")
    size = query_mommas(db, "all", "estimated_diameter")
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

