# task 4  security incident manager
# kerr mcgettigan  b01746321  lanarkshire campus
# stores details about a security incident in a dictionary and updates them

# create the dictionary with the incident details
incident = {
    "username": "kerr",
    "ip_address": "192.168.1.25",
    "event_type": "Failed login",
    "risk_level": "Low"
}

# show the username and ip address
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

# add a new field called status
incident["status"] = "Under investigation"

# update the risk level
incident["risk_level"] = "High"

# remove a field chosen by the user
# try except stops the program crashing if the field doesnt exist
print("\nFields:", list(incident.keys()))
field = input("Enter a field to remove: ").strip()

try:
    del incident[field]
    print(field, "removed")
except KeyError:
    print("That field does not exist, nothing removed")

# show all of the keys and values left
print("\nIncident details:")
for key, value in incident.items():
    print(key, ":", value)

# show how many key value pairs there are
print("\nTotal number of fields:", len(incident))