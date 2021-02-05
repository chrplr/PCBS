Title: **Course 00: Software Installation**  
 Tuesday Sept. 4th, 2018


**Objective:**

Each student should end up with a bundle of softwares which are needed for the courses of the Cogmaster:

  * Anaconda Python 3.6 distribution from  https://www.continuum.io/downloads
  * expyriment from http://www.expyriment.org/
  * Atom (text editor) from https://atom.io/
  * R from https://cran.r-project.org/
  * Rstudio Desktop from https://www.rstudio.com
  * Git from https://git-scm.com/
  * Meld from http://meldmerge.org/


# Important informations

This document contains detailed instructions on how to install these software on your computer. Please read them. You should try and follow them before coming to the first lectures. In case you encounter difficulties, we offer an install party to help you setup your computer.

Install party: The **only** slot in the schedule dedicated to installation of softwares is on _Tuesday September 4 from 10am to 13pm_. We will **not** answer any installation questions during the following lectures.

Before coming to the install party, you have one important thing to do:

 **free at least 5 GB on your hard drive**

Note: It may also be a good opportunity to perform a backup of your hard drive if you do not do this regularly.

Some installations will require an Internet access. Don't forget to bring your login and password for the install party.

Installation procedures have been successfully tested on computers running Windows (7 64bits), MacOS
(10.13 High Sierra), and Ubuntu linux 16.04. We have have few years of experience with usual install problems on various Operating System versions (Mac OS 10.6 to 10.11, Windows XP, 8 and 10, various linux flavors), but there are always some computers on which the usual procedures and fixes fail. We will try our best, if it happens to you, please be patient.

** Non-standard equipment (typically tablets or some mini-PC) or OS (Chrome, iOS,...) are not supported. **

** Note that you must have administrator rights to install some of the software. It you are using a computer from an institution, this is not always the case. Check with your IT team.

** If you are using Windows 10, make sure your user name doesn't include characters that don't belong to the english alphabet (accents, ideograms,...**


The download and installation instructions are specified below. Before the install party, unless you have an unsupported equipment or OS or don't have access to internet, or don't own a laptop, please download the software installers. The ENS wifi is usually very slow and prone to disconnections.

If you are using a debian-based Linux distribution, most of the install will be made using the `apt` package manager, thus is way safer to try the installation at your home than at the ENS if you have a decent Internet connection.

You might skip the `Atom` download and install if you are already using an advanced text editor such as wim, emacs, sublimetext...  
Beware: Microsoft Office Word, LibreOffice and other document formatting softwares are **not** text editors.

# Download instructions

When you download an installer file for a software, it is very important to:

1. make sure you know in which folder the installer file is saved
2. just download the file, not execute it, so please de-activate any internet browser preference that would automatically execute a file upon download completion, and for Windows users, make sure you always select the `save the file as` option when the usual dialog window pops up for a download.

Select the download instructions for your operating system:  
[Downloads for Windows](#downloads-for-windows)  
[Downloads for Mac OS](#downloads-for-mac-os)  
[Downloads for Ubuntu 16.0.4](#downloads-for-ubuntu)


# Installation instructions

First, read the installation instructions relative to your operating system. Yes, I mean it, read all the installation instructions before trying to install anything.

Now, if what you've just read makes sense, you can try to install the softwares by following carefully the instructions **step by step, not skipping any**.

If you feel unsure, don't worry, just wait until the install party.

Some installations, especially components for pygame on Mac OS, are rather tricky, If you are not 100% sure of what some instruction for one step means, stop right before this step. It is much easier to prevent a misinstallation than to fix it. Don't install anything after this step as there are some dependencies.

Same if something does not work as expected, stop there and ask for our help on Tuesday morning.

Select the installation instructions for your operating system:  
[Installations for Windows](#installations-for-windows)  
[Installations for Mac OS](#installations-for-mac-os)  
[Installations for Ubuntu (version >= 16.04)](#installations-for-ubuntu)


__________________________________________________

# Downloads for Windows

First, you need to check that you are using a 64 bits version of Windows,
follow the instructions [on this website](http://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/). If your system is an old 32 bits, tell us quickly: the following instructions work for 64 systems.
If you are using Windows 7 or earlier, it will be useful to know the full name of your files, so open a file explorer (window key + e), then select the `Organize` menu, then `Folder and search options`, then the second tab `View`, uncheck the box `Hide extensions for known file types`, and finally click the `OK` button.

## Text Editor
Download the Atom installer file `AtomSetup.exe`, using [this link](https://atom.io/download/windows). You can alternatively download the installer file directly by clicking on the big red `Download Windows Installer` button on http://atom.io

## Meld Merge tool

Download the windows installer for meld from  http://meldmerge.org/, or directly from https://download.gnome.org/binaries/win32/meld/3.18/Meld-3.18.2-win32.msi

## R and RStudio
* Download the lattest R package installer `R-3.5.1-win.exe` using [this link](https://cran.rstudio.com/bin/windows/base/R-3.5.1-win.exe) or directly from https://cran.rstudio.com/bin/windows/base/
* Download the lattest RStudio installer `RStudio-1.1.456.exe` using [this link](https://download1.rstudio.org/RStudio-1.0.153.exe) or directly from https://www.rstudio.com/products/rstudio/download/

## Git
Download the `Git` installer from https://git-scm.com/download/win

## Python
If you have a 64 bits Windows, download the Windows 64-Bit Python 3.6 Graphical Installer `Anaconda3-5.2.0-Windows-x86_64.exe` from [this link](https://repo.continuum.io/archive/Anaconda3-5.2.0-Windows-x86_64.exe) of directly from https://www.continuum.io/download

__________________________________________________

# Downloads for Mac OS

## Warming up

0. Make sure you know the administrator password for your computer (the password of your main account, i.e. the one you use to install new software) and that you are able to type it blind (i.e. even if you don't see little stars for each character).

1. Know you system version, so you can chose which file to download
 * First go to the "apple" menu by clicking on the apple icon at the upper-left corner of the screen.
 * Select "About This Mac", and look at the Version number, the first two numbers are the major releases:

  | 10.4 | 10.5 | 10.6 | 10.7 | 10.8 | 10.9 | 10.10 | 10.11 |10.12|10.13|
  |------|------|------|------|------|------|-------|-------|-----|-----|
  | Tiger | Leopard | Snow Leopard | Lion | Mountain Lion | Mavericks | Yosemite | El Capitan |Sierra| High Sierra|
  | 2005 | 2007 | 2009 | 2011 | 2012 | 2013 | 2014 | 2015 |2016|2017|
 * Check that your version of Mac OS X is 10.9 or higher (for example 10.9.5 or 10.11.2 are higher, but 10.6.10 is lower).  
 If not or if you can't or don't want to risk an upgrade this evening, or if you are not sure, **stop right now, don't download or install anything, and come see us tomorrow at 2:00 pm**: you might be in one of the most complicated situations regarding software installations.

## Command Line Tools
1. Installation
   * open a terminal: type `terminal` in the Spotlight search field. Alternatively, you can open a `Finder` window and select the `Application` folder, then the `Utilities` folder, then double-click on the `Terminal` icon..
   * in this terminal window, copy and paste the following text then press on the `Enter` key (from now on this will be called **executing a command in the terminal**)

     ```
     xcode-select --install
     ```

   * this should make a window pop up to ask you if you want to install the "Command Line Tools", answer `Yes`, you might have to type your password, then wait until completion of the installation

   * If you can't perform this step, don't worry, come at 10:00 on Tuesday, we will help you do it.
2. Configuration
   * In your terminal, type the following commands
   ```
   echo "export LC_ALL=en_US.UTF-8" >> ~/.bash_profile
   ```
   ```
   echo "export LANG=en_US.UTF-8" >> ~/.bash_profile
   ```
   ```
   source ~/.bash_profile
   ```

## XQuartz
Download `XQuartz-2.7.11.dmg` by clicking on [this link](https://dl.bintray.com/xquartz/downloads/XQuartz-2.7.11.dmg) or from https://www.xquartz.org

## Python
 Download the Python 3.6 Graphical Installer for Mac OS X from the Anaconda distribution with [this link](https://repo.anaconda.com/archive/Anaconda3-5.2.0-MacOSX-x86_64.pkg), or from http://continuum.io/downloads but then beware of selecting the correct version

## Git
Download the stable `git for mac` installer using [this link](https://git-scm.com/download/mac) or from https://sourceforge.net/projects/git-osx-installer/files/git-2.18.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect.

## Atom
Download the Atom installer by clicking on [this link](https://atom.io/download/mac), or on the big `Download` button on the webpage [http://atom.io]


## R and RStudio
 * Selecting the correct R version
   * If your system version is 10.11 (El Capitan), 10.12 (Sierra) or 10.13 (High Sierra), Download the R package installer `R-3.5.1.pkg` using [this link](https://cran.rstudio.com/bin/macosx/R-3.5.1.pkg) or directly from https://cran.rstudio.com/bin/macosx/
   * If your system version is 10.9 (Maverick) or 10.10 (Yosemite), Download the R package installer `R-3.3.3.pkg` using [this link](https://cran.rstudio.com/bin/macosx/R-3.3.3.pkg) or directly from https://cran.rstudio.com/bin/macosx/
   * If your system version is older but at least 10.6 (Snow Leopard), Download the R package installer `R-3.2.1-snowleopard.pkg` using [this link](https://cran.rstudio.com/bin/macosx/R-3.2.1-snowleopard.pkg) or directly from https://cran.rstudio.com/bin/macosx/
 * Installing RStudio: Download the lattest RStudio installer `RStudio-1.0.153.dmg` using [this link](https://download1.rstudio.org/RStudio-1.0.153.dmg) or directly from https://www.rstudio.com/products/rstudio/download/


__________________________________________________

# Downloads for Ubuntu

As the linux installation requires on-line access to the Internet, the software downloads are part of the [Installations for Ubuntu 16.0.4](#installations-for-ubuntu)

You can nevertheless download, in advance, Atom, Anaconda3 and Rstudio installers:

    wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
    wget https://github.com/atom/atom/releases/download/v1.30.0/atom-amd64.deb
    wget https://download1.rstudio.org/rstudio-xenial-1.1.456-amd64.deb

(you may have to install `wget` with `sudo apt-get install wget`)

__________________________________________________



# Installations for Windows


## Text Editor

* If you are using a 64 bits version of Windows, install `atom`
 * use a file explorer (windows key + e) to open the directory in which you downloaded the installer file `AtomSetup.exe`
 * double-clicking on the installer file icon
 * if a pop-up dialog window ask you to install the `.NET Framework`, proceed by clicking on the `Install` button, then accept the installation and wait for the files to be downloaded and installed
 * Check the installation by starting the program `Atom` (e.g. using the Search Tool)

## Meld

* Double-click on the Meld installer that you downloaded from http://meldmerge.org/ (
https://download.gnome.org/binaries/win32/meld/3.18/Meld-3.18.2-win32.msi). During the install, accept the default installation directory which is proposed. Note that you need to be administrator on the machine.
* Check the installation by starting the program `Meld` (e.g. using the Search Tool)

## Git

Click on git's installer (`git-2.18.0-64bits.exe`) and accept all the defaults that are proposed during the installation (It is especially important to select "Use git from the Windows command prompt").

Start the program "git bash" and type (replacing the nom/prénom/email by the relevant text):

    git config --global user.name "Prénom Nom"
    git config --global user.email prenom.nom@server.com
    git config --global core.editor nano

    git config --global merge.tool meld
    git config --global mergetool.meld.cmd '"C:\Program Files (x86)\Meld\meld.exe" "$LOCAL" "$BASE" "$REMOTE" --output="$MERGED"'


If you have internet access, type:

    git clone https://github.com/expyriment/expyriment-stash.git

You should then have a new folder `expyriment-stash`, containing example of python scripts running experiments.

## Python

1. Installation of the Anaconda distribution
 * go to your download folder and double click on the Anaconda3 file installer icon to initiate the installation process
 * on the Anaconda Setup Wizard, beware, pay attention to the following options option:
 * verify that you Install for `Just Me (recommended)`, then click on `Next`
 * Accept the default Destination folder and click on `Next`
 * Accept the defaults (uncheck "Add Anaconda to my PATH" and  checl "Register Anaconda as my default Python 3.6" and click on `Install`
 * upon completion, click on 'Next', then `Finish`
2. Test
* Start the `Anaconda Prompt` program (use the search tool)
 * this launches a DOS command window.  
 * type `ipython` and press `enter`
 * then, type each of those lines one by one followed by a stroke on the `Enter` key

   ```
   import numpy as np
   import matplotlib.pyplot as plt
   from scipy import stats
   x=np.arange(-5,5,.1)
   y=stats.norm.pdf(x)
   plt.plot(x,y)
   plt.show()
   ```

 * you should see a graphic window. If not, there is a problem with the installation or the command you just typed.
 * Close the graphics window.
 * close the ipython shell by typing `quit()` or the keyboard shortcut `ctrl + D`

3. Installing expyriment
 * In the 'Anaconda Prompt' terminal.
 * at the prompt, type the following text and then press on the `Enter` key (this is called "executing a command", more on that in the first Info lectures!):

   ```
    pip install expyriment
   ```

 * you will see some text messages during the installation of some python modules, in particular, messages about installing pygame and its dependencies.
 * when you are asked `Proceed ([y]/n)`, press on the `Enter` key (because yes is the default).

 * Now, type the command

   ```
   python expyriment-stash\examples\behavioral\simon_task.py
   ```
   
  * wait
  * hit `Enter` to validate the subject number
  * Hit `Enter` to start the test: you must press the left arrow key when you see a green square, the right arrow key when you see a red one.



## R and RStudio

 1. Installation
  * open a file explorer (windows key + e) and open the directory in which you downloaded the installer file `R-?.?.?-win.exe` (the `?` stands for any character).
  * install R by double-clicking on the downloaded file and following the steps on the typical Windows installer pop-up windows (as usual, you just have to click on `Install`, then `Yes` to "Allow modifications by an unknown program editor", then agree with the licence agreement if needed, then click the `Next` and/or `Finish` buttons using either default options or a different option when instructed to do so as you can see on the next lines).
  * when asked to "Select Start Menu ", check the `Don't create a Start Menu folder`, as we will use RStudio by default
  * when asked to "Select Additional Tasks", uncheck the `Create a desktop icon`, for the same reason
  * then install RStudio by double-clicking on the `RStudio-?.?.???.exe` icon in your the download directory. It should be straight forward as you know the usual install process now.

 2. Verification
  * if you want to create a RStudio desktop icon, open the Windows Start Menu by clicking on the taskbar window icon or hitting the windows key on your keyboard, look for the RStudio program icon, then drag and drop the RStudio icon to your desktop.
  * launch RStudio from the Windows Start Menu or with a double click the icon on your desktop, or using the search or side panel for Windows 8 users
  * in the `Console` panel, type 'demo(graphics)' and hit the `Enter` key


__________________________________________________




# Installations for Mac OS

## Configuration
 * make sure you know the administrator password for your computer (password used to install new software) and that you are able to type it blind.
 * click on the `Finder` icon on your dock then click on the `Finder` text next to the `Apple` logo on the top left corner of your screen to get the menus, then on `Preferences`, then on the `Side Bar` tab, check the first unchecked box under `DEVICES`. Now you can close the `Finder Preferences` window.
 * click on the apple logo on the top left of your screen, then on `System Preferences`, the select the `Security & Privacy` icon and on the `General` tab, if available, select the option `Anywhere` regarding `Allow apps downloaded from:`. You might have to click on the littke locker icon on the bottom left of the window and type your pasword if your preferences are protected.
 * open a `Finder` window and select the `Application` folder, then the `Utilities` folder, then drag the `Terminal` icon and drop it on the second position of your "Dock", right after the `Finder` icon. No you have and easy access to the most powerful application of your mac.

## XQuartz
* Installation
 * double click on `XQuartz-?.?.?.dmg` (the `?` stands for any character) in your `Downloads` folder or wherever you downloaded it.
 * double click on the `XQuartz.pkg`
 * click on `Continue` and `Agree` until you can click on `Install`
 * log out and back in if requested to do so

## Git
1. Installation
 * Go to your `Downloads` folder
 * double-click on the `git-2.18.0-intel-universal-mavericks.dmg` disk image icon
 * double-click on the `git-2.18.0-intel-universal-mavericks.pkg` icon
 * if you see a pop-up message "“git-2.18.0-intel-universal-mavericks.pkg” can’t be opened because it is from an unidentified developer", click `OK`, then in `System Preferences`, select the `Security & Privacy` icon and on the `General` tab, click on `Open anyway`, then click on `Open` on the confirmation pop-up
 * On the installer window, click on `Continue`, then on `Install`. You can close the installer at the end of the installation.
 * On nay finder window, dismount the disk image
2. Configuration
 * Open a terminal if needed
 * Execute the following commands (type the text, then press on the `Enter` key), replacing dummy values for your indentity and email by real ones:
   ```
   source ~/.bash_profile
   ```
   ```
   git config --global user.name "Prénom Nom"
   ```
   ```
   git config --global user.email prenom.nom@server.com
   ```
   ```
   git config --global core.editor nano
   ```
3. Test
 * Open a terminal if needed
 * Execute the following commands (type the text, then press on the `Enter` key):
   ```
   cd ~/Documents
   ```
   ```
   git clone https://github.com/expyriment/expyriment-stash.git
   ```

## Atom
 * Go to your `Downloads` folder
 * decompress the `.zip` archive if needed by double-cliking its icon
 * drag the `GitHub Desktop.app` and drop it in your `Application` Folder


## R and RStudio
1. R installation
 * in the Finder open the folder in which you downloaded the `R-?.?.?.pkg` R package
 * double-click on the package icon
 * the package installer window will open, click on `Next`
 * `Agree` to the terms of the licence
 * select the `Install for all users of this computer` option and click on `Continue`
 * click on `Install`

2. RStudio installation
 * go to the download folder then double-click on `RStudio-?.?.???.dmg`. In the window that pops up, slide the RStudio icon into the Applications folder

3. Verification
 * Launch RStudio from the icon on your desktop
 * in the `Console` panel, type

    ```
     demo(graphics)
    ```

then, hit the `Enter` key.


## Python
1. Install the Anaconda python distribution
 * go to your `Downloads` folder and double click on the file `Anaconda3-?.?.?-MacOSX-x86_64.pkg` in order to start the installation.
 * click on `Continue` several times and `Agree` on licence terms until the installation is completed, if at some point you see the error "You cannot install Anaconda in this location", then just click on `Install for me only` and you should be able to continue.
 * when you see the message "The installation was successful", click on the `Close` button

2. Log out, then log back in
 * quit the Terminal application, using the top menu `Terminal` > `Close Terminal` or the `CMD + Q` keyboard shortcut. You should not see the terminal anymore when navigating between applications using the `Alt + Tab` keyboard shortcut.
 * close your session using the `apple menu` (clic on the apple icon on the top left of your screen), then `Log Out your_user_name`, or using the `Shift Cmd Q` keyboard shortcut
 * log in

3. Test python
 * lauch the `Terminal` application from your "Dock"
 * just after the `$` sign, type `ipython` then press on the `Enter` key in order to lauch a ipython interpreter
 * in the ipython shell, type each of those lines one by one followed by enter

   ```
   import numpy as np
   ```
   ```
   import matplotlib.pyplot as plt
   ```
   ```
   from scipy import stats
   ```
   ```
   x=np.arange(-5,5,.1)
   ```
   ```
   y=stats.norm.pdf(x)
   ```
   ```
   plt.plot(x,y)
   ```
   ```
   plt.show()
   ```

 * close the window with the graph
 * close the ipython shell by typing `quit()` or the keyboard shortcut `ctrl + D`
 * you are now back to the command line in the Terminal application.


4. Install expyriment
  1. install expyriment from the terminal, which installs dependencies
     * launch a terminal if it's not done already
     * execute the following command (type the text, then press on the `Enter` key):

       ```
       pip install expyriment
       ```

    * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default
    * wait

  2. Test your expyriment installation
    * open a `Terminal` if needed
    * just after the `$` sign, type `ipython` then press on the `Enter` key in order to lauch a ipython interpreter
    * in the ipython shell, execute the following command

     ```
     import expyriment
     ```

  3. **Warning!** If you get any error during the expyriment installation or module import, the procedure starts to be tricky, stop rigth now, we will carry on Tuesday morning.  



5. Test expyriment
  * open a Terminal if needed
  * execute the following command

     ```
    python ~/Documents/expyriment-stash/examples/check-audio-visual-timing.py
     ```
  * wait
  * hit `Enter` to validate the subject number
  * the windows should now diplay some instructions. Hit `Enter` to start the test
  * hit `Escape` to stop the audio-visual stimulation
  * hit the `y` key to exit


__________________________________________________



# Installations for Ubuntu


First of all, you must determine if your system is 32 or 64 bits. Open
a terminal (Ctrl-Alt-T) and type the command

    arch

If you see `x86_64`, your operating system is 64 bits, if you see
`i386` or `i686`, it is 32 bits.

Second, you must make sure to have `wget`:

	sudo apt install wget


## Text Editor

Note: If you are already using a decent text editor under linux
(gedit, emacs, vim,...) you won't need Atom or Sublime Text.

 * if your linux is 64 bits:

    wget https://github.com/atom/atom/releases/download/v1.30.0/atom-amd64.deb
	sudo dpkg -i atom-amd64.deb


* if your linux is 32 bits, download the latest build package (currently 3114) from
[this link](https://download.sublimetext.com/sublime-text_build-3114_i386.deb) or the `Ubuntu 32 bits` link on https://www.sublimetext.com/3

## Meld

    sudo apt-get install meld

## Git

    sudo apt install git-core

Configuration:

     git config --global user.name "your_user_name"
     git config --global user.email your_email@example.com

     git config --global merge.tool meld
     git config --global mergetool.meld.cmd meld '$BASE $LOCAL $REMOTE $MERGED'
     git config --global mergetool.meld.trustExitCode false

     git config --global diff.tool meld
     git config --global difftool.meld.cmd meld '$LOCAL $REMOTE'

	 cd
     git clone https://github.com/expyriment/expyriment-stash.git

Check that you now have a folder  expyriment-stash  in your home directory.



## Python

if you system is 64 bits:

    wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh

if your system is 32 bits:

    wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86.sh


Then, run the installer:

    bash Anaconda*.sh


Accept the modification to the .bashrc to add anaconda3/bin to the PATH. Otherwise, you will need to do it yourself later:

     echo "PATH=$HOME/anaconda3/bin:$PATH" >> ~/.bashrc

Open a new terminal so that the change in .bashrc is taken into account and type the following line to check the version of python that you access to by default:

	which python

It should display $HOME/anaconda3/bin, not /usr/bin/python

Then install the additional module expyriment

	 pip install expyriment

To check the installation, enter the command:

    python expyriment-stash/examples/behavioural/simon_task.py

  * wait
  * hit `Enter` to validate the subject number
  * Hit `Enter` to start the test: you must press the left arrow key when you see a green square, the right arrow key when you see a red one.


## R

The instructions to install R are available here:
https://cran.r-project.org/bin/linux/ubuntu/README.html#installation

In a nutshell:

	sudo echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | sudo tee -a /etc/apt/sources.list

	gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9


	gpg -a --export E084DAB9 | sudo apt-key add -

	sudo apt-get update
	sudo apt-get install r-base r-base-dev r-cran-lme4 r-cran-plyr r-cran-ggplot2 r-cran-multcomp r-cran-nlme r-cran-lattice r-cran-multicore


## Rstudio

If you have a 64 bits system (arch = `x86_64`)

	wget https://download1.rstudio.org/rstudio-1.1.456-amd64.deb
	sudo apt install libjpeg62
    sudo dpkg -i rstudio-*-amd64.deb


Then, launch `rstudio` in a terminal, and in the rstudio console, type

	demo(graphics)

And press 'enter' to display graphs in the `plots` panel.
