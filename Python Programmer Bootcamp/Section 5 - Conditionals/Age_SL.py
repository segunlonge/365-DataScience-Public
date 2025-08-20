age = 16
has_permission = True

if age >= 18 and has_permission == True:
    print("Can drive")
elif age < 18 and has_permission == True:
    print("Can drive with permission")
else:
    print("Cannot drive")