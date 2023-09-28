"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.
Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000

"""

import json
infile = open('school_data.json', 'r')

schools = json.load(infile)
conference_schools = [372, 108, 107, 130]


print(type(schools))
print(len(schools))

for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools and school["Graduation rate  women (DRVGR2020)"] > 75:
        print("School:",school["instnm"])
        print("Graduation Rate for Women:",school["Graduation rate  women (DRVGR2020)"],"\n")    

for school in schools:
    if isinstance(school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"], int):
        if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools and school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            print("School:", school["instnm"])
            print("Cost for in-state students living off-campus:",school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"],"\n")