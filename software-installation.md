PCBS: Software Installation
===========================

Time-stamp: <2019-02-17 22:16:12 christophe@pallier.org>

For the PCBS lectures, you will need the following software:

  * **Python3**. We strongly recommend the Anaconda distribution from  https://www.continuum.io/downloads
  * The Python library **Expyriment** from http://www.expyriment.org/
  * **Git** from https://git-scm.com/
  * **Sublime Text** (text editor) from [Sublime Text](https://www.sublimetext.com/)  (Unless you are already using a text editor that you are happy with)
  * **R** from https://cran.r-project.org/
  * **Rstudio Desktop** from https://www.rstudio.com

Remarks:

* You will need to download about 1GB of software from the Internet. Therefore, make sure to have a decent connection.
* Make sure that you have at least 5GB of free space on your hard drive to unpack the softwares.
* You might need to have administrator rights to install some of the softwares. If you are using a computer from an Institution, this is not always the case. Check with your IT team.
* If you are using Windows 10, make sure your user name doesn't include spaces or characters that don't belong to the English alphabet (accents, ideograms,...). If you do, better create a new user with a 

## Anaconda Python3

* Download the Anaconda Python3 distribution Python from https://www.continuum.io/download.
* Go to your download folder and execute the Anaconda3 file installer.
* on the Anaconda Setup Wizard, beware, pay attention to the following options option:
   - verify that you Install for `Just Me (recommended)`, then click on `Next`
   - Accept the default Destination folder and click on `Next`
   - Accept the defaults (uncheck "Add Anaconda to my PATH" and  check "Register Anaconda as my default Python" and click on `Install`
   - upon completion, clvick on 'Next', then `Finish`

## Expyriment

1. Open a Terminal:

* Under Linux, launch `Terminal` from your applications menu or use `Ctrl-Alt-T`. 
* under MacOS: type `terminal` in the Spotlight search field. Alternatively, you can open a `Finder` window and select the `Application` folder, then the `Utilities` folder, then double-click on the `Terminal` icon..
* Under Windows, launch `Anaconda Prompt`
 
 
2. Type:

    pip install expyriment


## Git

* **Ubuntu Linux** : Just run     `sudo apt install git`
* **Windows**: Download `Git for windows` from <https://git-scm.com/download/win> and execute it. Accept all the defaults.
* **MacOS***:  Download the  `Git for Lac` installer from <https://git-scm.com/download/mac> and execute it. Accept all the defaults.

To configure git, open a Terminal (or launch *Git Bash* under Windows) 

    git config --global user.name "your_first_and_last_names_here"
    git config --global user.email your_email_here
    git config --global core.editor nano


## Sublime Text Editor

Unless you already master a text editor, we recommend that you download and install Sublime Text from <https://www.sublime text.com/>. Follow the instructions for your OS on this site. 


## R


 * **Windows** Download and install the latest  version of R from <https://cran.rstudio.com/bin/windows/base/>
 * **MacOS**: Download and install the latest  version of R from <https://cran.rstudio.com/bin/macosx/>
 * **Linux**: Follow the instructions at 
https://cran.r-project.org/bin/linux/ubuntu/README.html#installation


## Rstudio Desktop

Download and install the latest version of RStudio Desktop from <https://www.rstudio.com/products/rstudio/download/>


