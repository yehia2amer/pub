import json
import yaml

fileObject = open("af.json", "r")
jsonContent = fileObject.read()
afList = json.loads(jsonContent)
combined = {}
combinedfree = {}
combinedreq = {}

for n in afList:
  if "Name" in n.keys():
    tmp = n["Name"]
    tmp = ''.join(filter(str.isalnum, tmp))
    print(tmp.encode("utf-8"))
    
    n.pop("downloads", "")
    n.pop("downloadtrend", "")
    n.pop("stars", "")
    n.pop("trending", "")
    n.pop("trends", "")
    n.pop("trendsDate", "")
    n.pop("templatePath", "")
    n.pop("Shell", "")
    n.pop("CPUset", "")
    
    if "Config" in n.keys() and n["Config"]:
      hold = {}
      hold["Port"] = {}
      hold["Variable"] = {}
      hold["Path"] = {}
      hold["Device"] = {}
      hold["Label"] = {}
      if isinstance(n["Config"], list):
        for a in n["Config"]:
          name = a["@attributes"]["Name"]
          type = a["@attributes"]["Type"]
          a.update(a["@attributes"])
          a.pop("@attributes", "")
          hold[type][name] = a
      else:
          name = n["Config"]["@attributes"]["Name"]
          type = n["Config"]["@attributes"]["Type"]
          n["Config"].update(n["Config"]["@attributes"])
          n["Config"].pop("@attributes", "")
          hold[type][name] = n["Config"]
      n.pop("Config", "")
      n["Config"] = hold
      
    
    globals()['%s' % tmp] = n
    
    if "Plugin" in n.keys() and n["Plugin"]:
      print("skipping "+tmp+" is a unraid plugin...")
    else:
      combined[tmp] = n
      if "Requires" in n.keys() and n["Requires"]:
        combinedreq[tmp] = n
        jsonString = json.dumps(n)
        jsonFile = open("apps/"+"req/"+"json/"+tmp+".json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        yamlString = yaml.dump(n)
        yamlFile = open("apps/"+"req/"+"yaml/"+tmp+".yaml", "w")
        yamlFile.write(yamlString)
        yamlFile.close()
      else:
        combinedfree[tmp] = n
        jsonString = json.dumps(n)
        jsonFile = open("apps/"+"json/"+tmp+".json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        yamlString = yaml.dump(n)
        yamlFile = open("apps/"+"yaml/"+tmp+".yaml", "w")
        yamlFile.write(yamlString)
        yamlFile.close()

jsonString2 = json.dumps(combinedfree)
jsonFile2 = open("apps-free.json", "w")
jsonFile2.write(jsonString2)
jsonFile2.close()

yamlString2 = yaml.dump(combinedfree)
yamlFile2 = open("apps-free.yaml", "w")
yamlFile2.write(yamlString2)
yamlFile2.close()


jsonString3 = json.dumps(combinedreq)
jsonFile3 = open("apps-req.json", "w")
jsonFile3.write(jsonString3)
jsonFile3.close()

yamlString3 = yaml.dump(combinedreq)
yamlFile3 = open("apps-req.yaml", "w")
yamlFile3.write(yamlString3)
yamlFile3.close()

jsonString4 = json.dumps(combined)
jsonFile4 = open("apps.json", "w")
jsonFile4.write(jsonString4)
jsonFile4.close()

yamlString4 = yaml.dump(combined)
yamlFile4 = open("apps.yaml", "w")
yamlFile4.write(yamlString4)
yamlFile4.close()