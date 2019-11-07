import csv
import geojson
import json



with open("communityAreas.geojson") as f:
    gj = geojson.load(f)
features = gj['features']


with open('languageAndPop.csv', newline='') as csvfile:
	languageData = csv.reader(csvfile, delimiter=',')
	header = []
	for row in languageData: 
		header = row #just asssigns the first row as header
		break
	for row in languageData:
		propertiesToAdd = {}
		propertyTracker = 0
		totalNonEnglish = 0
     	##build up the properties dict you want to add to geojson (converting row to geojson)
		for entry in row:
     		##gets the column headers and assign them the associated row value
			columnName = header[propertyTracker].lower()
     		#adding each column value to properties
			propertiesToAdd[columnName] = entry.lower()
			#only want to add up the columns with language counts
			if(propertyTracker > 2 and propertyTracker < len(row) - 1):
				totalNonEnglish += int(entry)
			propertyTracker += 1
		#add a property for the total non=english speakers 
		propertiesToAdd["Total Non-English Speakers"] = totalNonEnglish

		

		for communityArea in features: 
			properties = communityArea['properties']
			#find the matching community area
			if properties['community'] == row[1].upper():
				#combine the new and old properties and reassign it
				properties = dict(list(properties.items()) + list(propertiesToAdd.items()))
				communityArea['properties'] = properties


gj['features'] = features
with open('langAndGeography.geojson', 'w') as f:
    json.dump(gj, f)

