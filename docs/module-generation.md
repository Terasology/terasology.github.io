# Module Generation Automation

The automation focuses on automating the [ModuleSite](https://github.com/MovingBlocks/ModuleSite) for gathering information about modules from [Index repository](https://github.com/Terasology/Index/blob/master/distros/omega/gradle.properties) and
exhibit their generated information on ModuleSite.This uses an automation tool called [Jenkins](https://www.jenkins.io/), which provides stages and steps in the
pipeline to perform different operations

This will be a [Pipeline](https://www.jenkins.io/doc/book/pipeline/) job that will run periodically so that if there will be any changes in module information present in the Index repository that information can be updated on ModuleSite easily.Let's try to understand Automation part deeply

### File Structure

```
├── Jenkinsfile           - Jenkins pipeline text file
├── scrape.py             - File to scrape and sort modules and Non modules repository and to collect require information
├── frontMatter.py        - File to generate frontmatter form scraped modules
├── loadModules.sh        - supporting bash script to perform git operations
```

### Module Generation Diagram

<img src="./images/Module-Generation.png" width="450" height="500">

## Collecting Data

At the starting stage of the pipeline some scripts will be triggered which will create API calls to Github Index repository to fetch all the required information i.e. `module.txt, Readme, cover image` if `Readme, cover image` will not be available we will fallback to default image and default readme text.Next step will be to prepare Readme file to display that collected infromation on ModuleSite.An new script will br triggered that will prepare information that are going to displayed on ModuleSite. As you see above file structure we have `scrape.py` and `frontmatter.py` which will perform this opertaions. `scrape.py` uses [PyGithub](https://pygithub.readthedocs.io/en/latest/) to create API calls

## Generate Artifact

This stage tries to copy the [artifact](https://www.jenkins.io/doc/pipeline/tour/tests-and-artifacts/) of last successful build, if it does not found any artifact it create
new artifact of current build and create pull request to the ModuleSite using the supporting bash script `loadModules.sh`. If it gets the last successful build
, it compares the current build and the last successful build, if their is anu changes between the build, the last successful build is removed and current build is archived and create pull request to ModuleSite.

## Clean Workspace

At last the workspace is cleared so that we don't run into errors next time when the pipeline is executed.The same process is repeated periodically
