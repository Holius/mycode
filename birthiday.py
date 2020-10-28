import requests

def convert_month(month):
    month = month.lower()
    month_dictionary = { "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug" : 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
    month =  month_dictionary.get(month)
    if month == "None": return "error"
    return month

def check_day(day):
    if not day.isnumeric(): return "error"
    return int(day)

api_key = "9606880197aeaab40442f8635092fca4918bf5"
base_url = "https://api.festdays.dev/v1/holidays"
year = "2020"
month = convert_month(input("Enter 3 Letter Birth Month like jan for january: ")) 
day = check_day(input("Enter your day of birth like 1 for the first of the month: "))
headers = {"Authorization": api_key}
query= {"year": year} 
endpoint = f"{base_url}"

#free version of this API is terrible
#cuts amount of holidays received down to only 100 results
#cannot query years before 2000
def main(month, day, endpoint, headers, query): 
    r = requests.get(endpoint, headers=headers,params=query)
    data = r.json()
    results = data['results']
    
    if month == "error" or day == "error": 
        print("Silly User Results are for Valid Entries!")
        return
    month_holiday = {}
    for x in results:
        if x["month"] == month: month_holiday = x
        if x["month"] == month and x["day"] == day:
            print(f"Your holiday is {x.get('name')}.")
            return
    print("No results. Your birthday is not cool enough for a holiday.")
    if isinstance(month_holiday.get("name"), str):
        print(f"Here is a holiday in the same month: {month_holiday['name']}.")
main(month, day, endpoint,headers, query)



