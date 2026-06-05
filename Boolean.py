# -----------------------------------------
#           <<    Boolean     >>
# -----------------------------------------
# [1]  In Programming You Need To Known Your If Your Code Output Is True Or False
# [2]  Boolean Values Are The Two Constant Objects False + True
# -----------------------------------------

Ultrasound = ""
print(Ultrasound.isspace())

Ultrasound = " "
print(Ultrasound.isspace())

print("_" * 50)

print(570 > 1000)
print(570 > 570)
print(1570 > 1000)

print("_" * 50)

# True Values

print(bool("Microscopes"))
print(bool(7777))
print(bool(34.6))
print(bool(True))
print(bool(["Light / Optical Microscopes", "Electron Microscopes - EM"]))

print("_" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))

print("_" * 50)

#------------------------------------------
#       <<    Boolean Operators    >>
# -----------------------------------------
# [1]  and
# [2]  or
# [3]  not
# -----------------------------------------

age = 25
country = "Egypt"
rank = 7 

print(age > 18 and country == "Egypt" and rank > 0)                                # True
print(age > 18 and country == "Egypt" and rank > 10)                               # False

print("_" * 50)

age = 25
country = "Egypt"
rank = 7 

print(age > 35 or country == "Egypt" or rank > 15)                                 # True
print(age > 30 and country == "Portugal" and rank > 10)                            # False

print("_" * 50)

print(age > 18)                                                                    # True
print(not age > 18)                                                                # False



