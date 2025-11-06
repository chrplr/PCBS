PROJect
=======

Choose a programming project with a topic related to cognitive science, e.g data analysis, simulations or creating an experiments. A list of papers are available at <https://github.com/chrplr/PCBS/tree/master/pdfs/papers-for-projects>, but you can select your own topic. 
 
Rules of the game:

* your code should work and be **portable**, i.e., use relatives paths, so that anyone can run it **
* your code should be **readable**, following, as much a possible, [Clean Code](https://pcbs.readthedocs.io/en/latest/tips-to-write-clean-code.html). (do not be overambitious, ~30~200 lines of code (not including comments) is fine)
* You have to use the **Git** versionning system to keep track of the progress of your code.


---
* your project must contain a readable documentation written in  [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

      
* You project must be publicly available on http://github.com   

Examples:

<https://github.com/chrplr/PCBS-LexicalDecision>, <https://github.com/sepehr-rasouli/PCBS-ITRL/>, 
<https://github.com/doriguzmn/PCBS-DataAnalysis>


---

Git
===

Check <https://pcbs.readthedocs.io/en/latest/tools-for-reproducible-science.html>

The reference <https://git-scm.com/book/en/v2>

Github
======

1. Create an account on github.com

2. Create an ssh key on your local computer, using the command ``ssh-keygen`` and copy it on github.com. DEtailed instructions are available at <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>

2. Create a new repository named `project` selecting 'Public' and 'Add a README file'.

3. Clone it on your local computer:

    -  PRess the green button 'Code' and copy the ssh url (for me:git@github.com:chrplr/test.git )
    - in a terminal (git bash for windows), type:
    
        git clone URL
        
        where URL is the address you copied on the previous step 

4. edit the file ``README``, adding a line.

5.
    git add README
    git commit -m test
    git push


Different authentifcation methods in github:

https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/#what-you-need-to-do-today
