#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string")
        return
    if not (isinstance(attendees, list) and all(isinstance(a, dict) for a in attendees)):
        print("Attendees must be a a list of dictionaries")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        data = {
        "name": attendee.get("name", "N/A"),
        "event_title": attendee.get("event_title", "N/A"),
        "event_date": attendee.get("event_date", "N/A"),
        "event_location": attendee.get("event_location", "N/A"),
        }
        text_invitation = template.format(**data)

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_invitation)
        print(f"Invitation pour l'index {index} : {text_invitation}")
