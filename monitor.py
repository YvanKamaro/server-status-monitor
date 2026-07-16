#Read and store server information  from the user into servers list.
from datetime import datetime
def data():
    servers= []
    print("\nEnter server details(e.g Mail01 online/offline/manage)")
    print("When finished enter q\n")
    while True:
        user=input(">")
        if user.lower()=="q":
            break
        valid_status = ["online", "offline", "manage"]
        parts = user.strip().split()
        if len(parts) == 2 and parts[1] in valid_status and user.strip() not in servers:
            servers.append(user)
        else:
            print("Please enter a valid server name and status")
    
    return servers
    
# Categorizes Servers into 3 lists
def categorize(servers):
    online = []
    offline = []
    manage = []
    for n in servers:
        if "online" in n:
            online.append(n)
        elif "offline" in n:
            offline.append(n)
        elif "manage" in n:
            manage.append(n)
    return online, offline, manage

# Writes each list to its own file
def write(online, offline, manage):
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if online:
        with open("online.txt", "a") as f:
            f.write(f"# Report generated: {timestamp}\n")
            f.write("\n".join(online) + "\n")
    if offline:
        with open("offline.txt", "a") as f:
            f.write(f"# Report generated: {timestamp}\n")
            f.write("\n".join(offline) + "\n")
    if manage:
        with open("manage.txt", "a") as f:
            f.write(f"# Report generated: {timestamp}\n")
            f.write("\n".join(manage) + "\n")

# Summary
def summary(online, offline, manage):
    return (
        f"\n=======SERVER STATUS REPORT========\n"
        f"Online:      {len(online)} server(s)\n"
        f"Offline:     {len(offline)} server(s)\n"
        f"Manage:      {len(manage)} server(s)\n"
        f"================================\n"
        f"Written to online.txt, offline.txt, manage.txt\n"
    )

if __name__ == "__main__":
    print("======================")
    print("SERVER STATUS MONITOR")
    print("======================\n")
    servers=data()
    print(f"\n➤{len(servers)} Servers.\n")
    online,offline,manage=categorize(servers)
    write(online,offline,manage)
    print("\n",summary(online,offline,manage))
