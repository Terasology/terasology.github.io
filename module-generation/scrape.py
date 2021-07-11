import os
import json
import requests
from github import Github

indexDir = "./scrape-data/"
os.mkdir(indexDir)

accessToken = os.environ.get('GIT_TOKEN')
g = Github(accessToken)

user = g.get_user('Terasology')
repo = user.get_repo("Index")
allModules = repo.get_contents("/distros/omega/gradle.properties")
getModules = allModules.decoded_content.decode()
for line in getModules.split():
    if  line.startswith('extraModules='):
        filterData=line[13:]
        modules=filterData.split(",")

# Collect modules 
for module in range(len(modules)):
    if(module<len(modules)):
        repository=user.get_repo(modules[module])

        #Fetch module information
        try:
            moduleContent=repository.get_contents("module.txt")
            getModuleData=moduleContent.decoded_content.decode()
            parseModuleData=json.loads(getModuleData)
            moduleName=parseModuleData['id']
            moduleDir=os.mkdir(indexDir+moduleName)
            moduleDirSrc=indexDir+moduleName
            moduleFile= open(moduleDirSrc+"/module.txt", "a")
            moduleFile.write(getModuleData)
            moduleFile.close()
        except:
            print("Repository is not a Module "+moduleName)

        #Fetch readme file
        try:
            readmeContent=repository.get_contents("README.md")
            getReadmeData=readmeContent.decoded_content.decode()
            moduleReadmeFile= open(moduleDirSrc+"/README.md", "a")
            moduleReadmeFile.write(getReadmeData)
            moduleReadmeFile.close()
        except:
            print("No Readme Found "+moduleName)
            moduleDefaultReadme= open(moduleDirSrc+"/README.md", "a")
            moduleDefaultReadme.write("No information available of "+ moduleName)
            moduleDefaultReadme.close()

        #Fetch banner image
        bannerImage="https://raw.githubusercontent.com/Terasology/"+moduleName+"/develop/docs/_media/banner.png"
        response = requests.get(bannerImage)
        if(response.ok):
            imageFile = open(moduleDirSrc+"/cover.png", "wb")
            imageFile.write(response.content)
            imageFile.close()
        else:
            print("No banner found on "+ moduleName+",resolving with default banner")
            sourceImage=open("./module-generation/defaultBanner.png", "rb+")
            readSourceImage=sourceImage.read()
            defaultImageFile = open(moduleDirSrc+"/cover.png", "wb+")
            defaultImageFile.write(readSourceImage)
            defaultImageFile.close()
            