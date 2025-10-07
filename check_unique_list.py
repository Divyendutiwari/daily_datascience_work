lst=["Emma Johnson", "Liam Smith", "Olivia Brown", "Emma Johnson", "Noah Davis", "Ava Wilson", "Liam Smith", "Sophia Miller"]
kl=set(lst)
if len(lst)==len(kl):
    print("All names are unique")
else:
    print("There are duplicate names in the list")