names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
#Added another name and cost:
names.append("Priscilla")
insurance_costs.append(8320.0)

#Adding the two lists together with zip():

medical_records = list(zip(insurance_costs, names))
print(medical_records)

#number of medical records

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " Medical records")

#first medical records:

first_medical_record = medical_records[0]
print("Here is the first medical record: " +str(first_medical_record))

#people with lowest insurance costs first: .sort tar som default ascending (stigende)

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

#cheapest three: dvs 0 -> 2 index

cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " +str(cheapest_three))

#three most expensive:

priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " +str(priciest_three))

#nr of times the name Paul shows up in our records:

occurences_paul = names.count("Paul")
print("There are " +str(occurences_paul) + " individuals with the name Paul in our medical records.")


#Extra: the five in the middle
#create a new zip starting with names this time:

medical_records = list(zip(names, insurance_costs))
middle_five_records = medical_records[3:7]
print(middle_five_records)

