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
     	##build up the properties dict you want to add to geojson (converting row to geojson)
		for entry in row:
     		##gets the column headers and assign them the associated row value
			columnName = header[propertyTracker]
     		#adding each column value to properties
			propertiesToAdd[columnName] = entry
			propertyTracker += 1
		print(propertiesToAdd)
     	#Convert the properties dict to a list
		propertiesToAddList = zip(propertiesToAdd.keys(), propertiesToAdd.values())
		for communityArea in features: 
			properties = communityArea['properties']
			if properties['community'] == row[1]:
				#adding each property to our community area Properties field
				for i in range(len(propertiesToAddList)):
					properties[propertiesToAddList[i][0]] = propertiesToAddList[i][1]
			# print(properties)
   #       	print(', '.join(row))

with open('new.geojson', 'w') as f:
    json.dump(features, f)


##now print just to see 
with open("new.geojson") as f:
    finished = geojson.load(f)
#print(finished)
# featuresNew = finished['features']
# for communityArea in featuresNew:
# 	print(communityArea['Properties'])




# populationCol = numpy.loadtxt("population.csv")
# print(populationCol)