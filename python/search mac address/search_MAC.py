import string

hex = list(string.hexdigits)


mac = input("Enter MAC_ADDRESS:\t")  # Takes the mac-address as input
oui = mac[0:8]  # extract the mac-address prefix
found = 0  # if there is no match in mac address then value unchanged

with open("mac-vendors-export.csv", "r") as f:
    for rows in f.read().splitlines():
        mac_suf = rows.split(",")[0]
        if mac_suf == oui:
            print(rows)
            found += 1
if found == 0:
    print("Opps the mac address is wrong or it's not in the list ")
