import os
import json

moduleDirs = "./scrape-data/"
moduleDst = "./modules/"
os.mkdir(moduleDst)

for moduleDir in os.listdir(moduleDirs):
    moduleFile = moduleDirs+moduleDir+"/module.txt"
    getModuledata = open(moduleFile, "r")
    readModuleData = getModuledata.read()
    parseData = json.loads(readModuleData)
    # Fetch module information and write on index.md file
    try:
        moduleName = parseData['id']
        moduleDescription = parseData['description']
        os.mkdir(moduleDst+moduleName)
        indexMd = open(moduleDst+moduleName+"/index.md", "a+")
        indexMd.write('---\n')
        indexMd.write('posttype: "module" \n')
        indexMd.write('title: '+moduleName+'\n')
        indexMd.write('description: "'+moduleDescription+'"\n')

        # get module cover image, write on index.md file and copy to paticular module folder
        moduleLogo = moduleDirs+moduleDir+"/cover.png"
        indexMd.write('cover: "./cover.png"'+'\n')
        sourceImage = open(moduleLogo, "rb")
        readImage = sourceImage.read()
        imageFile = open(moduleDst+moduleName+"/cover.png", "wb+")
        imageFile.write(readImage)
        imageFile.close()
        sourceImage.close()

        # collect tags and append to index.md
        Tags = []
        if "isGameplay" in parseData:
            if (parseData['isGameplay']):
                Tags.append("Gameplay")

        if "isServerSideOnly" in parseData:
            if(parseData['isServerSideOnly']):
                Tags.append("Server")

        if "isWorld" in parseData:
            if (parseData['isWorld']):
                Tags.append("World")

        if "isAugmentation" in parseData:
            if (parseData['isAugmentation']):
                Tags.append("Augment")

        if "isLibrary" in parseData:
            if(parseData['isLibrary']):
                Tags.append("Library")

        if "isAsset" in parseData:
            if(parseData['isAsset']):
                Tags.append("Asset")

        if "isSpecific" in parseData:
            if(parseData['isSpecific']):
                Tags.append("Specific")

        indexMd.write("tags: "+"["+','.join(f'"{w}"' for w in Tags)+"]\n")
        indexMd.write('---\n')

        # append readme information to module
        moduleReadme = moduleDirs+moduleDir+"/README.md"
        readmedata = open(moduleReadme, "r")
        indexMd.write(readmedata.read())
        indexMd.close()
    except Exception as e:
        print(e)
