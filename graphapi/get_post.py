from facepy import GraphAPI
import json

APP_TOKEN="EAAE9AbZBm7CkBAJZAScS1lbZCxHY7r4LdiZCGn6hF3xYTrllM5NN4o4sN4nOxFZCQv4qUTyOV5EZCDZAKnn2jdQI6hcHLmQpPupQ6buZANxU9AtB6PLvVrMCOT0nfFZCKRUZBBXZBZCx3YrEbUs8msjDz8TsXEz7FmJYZCRG1ZCEExA4PNKoJn5Nfqnjlbf6ZAyLhUIkaLgTjqbBZBtJziL6b1b988lKrCEqrWKZBTitNUd7Yiykj5LYEFXPSzbjU"

graph = GraphAPI(APP_TOKEN)

groupIDs = ["1520033134985553"]

outfile_name ="teacher-groups-summary-export-data.csv"

for gID in groupIDs:
  groupData = graph.get(gID + "/feed", page=True, retry=3, limit=500)
  for data in groupData:
        json_data=json.dumps(data, indent =4)
        decoded_response = json_data.decode("UTF-8")
        data = json.loads(decoded_response)
        print ("Paging group data...")

