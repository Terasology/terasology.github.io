import os
import json

DIR="./meta-data/"
DST="./modules/"
os.mkdir(DST)

for folders in  os.listdir(DIR):
    moduleFile=DIR+folders+"/module.txt"
    if(os.path.isfile(moduleFile)):
        getModuledata = open(moduleFile,"r")
        readModuleData=getModuledata.read()
        parseData=json.loads(readModuleData)
        moduleName=parseData['id']
        moduleDescription=parseData['description']
        
        moduleLogo="logo.jpg"
        moduleReadme=DIR+folders+"/README.md"

        os.mkdir(DST+moduleName)
        IndexMd=open(DST+moduleName+"/index.md","a+")
        IndexMd.write('---\n')
        IndexMd.write('posttype: "module" \n')
        IndexMd.write('title: '+moduleName+'\n')
        IndexMd.write('description: "'+moduleDescription+'"\n')

        if(os.path.isfile(moduleLogo)):
            print("yes")
            IndexMd.write('cover: "./logo.jpg"'+'\n')
            sourceImage=open(moduleLogo, "rb")
            readImage=sourceImage.read()
            ImageFile = open(DST+moduleName+"/logo.jpg", "wb+")    
            ImageFile.write(readImage)
            ImageFile.close()
            sourceImage.close()

        Tags=[]

        if (parseData['isGameplay']):
            Tags.append("Gameplay")
        if(parseData['isServerSideOnly']):
            Tags.append("Server")
        if (parseData['isWorld']):
            Tags.append("World")
        if (parseData['isAugmentation']):
            Tags.append("Augment")
        if(parseData['isLibrary']):
            Tags.append("Library")
        if(parseData['isAsset']):
            Tags.append("Asset")
        if(parseData['isSpecific']):
            Tags.append("Specific")
        
        
        IndexMd.write("tags: "+"["+','.join(f'"{w}"' for w in Tags)+"]\n")
        IndexMd.write('---\n')

        if(os.path.isfile(moduleReadme)):
            readmedata=open(moduleReadme,"r")
            IndexMd.write(readmedata.read())
        else:
            IndexMd.write("No info available")





        # if "isGameplay" in parseData:
        #     if (parseData['isGameplay']):
        #         Tags.append("Gameplay")

        # if "isServerSideOnly" in parseData:
        #     if(parseData['isServerSideOnly']):
        #         Tags.append("Server")

        # if "isWorld" in parseData:
        #     if (parseData['isWorld']):
        #         Tags.append("World")

        # if "isAugmentation" in parseData:
        #     if (parseData['isAugmentation']):
        #         Tags.append("Augment")
        
        # if "isLibrary" in parseData:
        #     if(parseData['isLibrary']):
        #         Tags.append("Library")
       
        # if "isAsset" in parseData:
        #     if(parseData['isAsset']):
        #         Tags.append("Asset")

        # if "isSpecific" in parseData:
        #     if(parseData['isSpecific']):
        #         Tags.append("Specific")