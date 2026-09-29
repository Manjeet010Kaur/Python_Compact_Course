#Create a dictionary with the events in Dortmund and the date of the event. List all events that were running during the Night of Museums in Dortmund on 19th September 2026. 


dortmund_events = {
    "Dortmund Museumsnacht": "19 September 2026",
    "Museum Ostwall": "19 September 2026",
    "DASA Arbeitswelt Ausstellung": "19 September 2026",
    "Deutsches Fußballmuseum": "19 September 2026"
}


for event, date in dortmund_events.items():
    if date == "19 September 2026":
        print(event)