# /usr/bin/env python
# Time-stamp: <2022-03-13 10:18:51 christophe@pallier.org>


"""

"what characters are good to use in a filename".

Some potential guidelines:

*    [0-9a-zA-Z_] - Alphanumeric characters and the underscore are always fine to use.
*    \/:*?"<>| and the null byte are problematic on at least one system, and should always be avoided.
*    Spaces are used as argument separators on many systems, so filenames with spaces should be avoided when possible. Other whitespaces (e.g. tabs) even more so.
*    Semicolons (;) are used to separate commands on many systems. Semicolons and commas(,) are used to separate command line arguments on (some versions of?) the windows command line.
*    []()^ #%&!@:+={}'~ and [`] all have special meanings in many shells, and are annoying to work around, and so should be avoided. They also tend to look horrible in URLs.
*    Leading characters to avoid:
        Many command line programs use the hyphen [-] to indicate special arguments.
        *nix based systems use a full-stop [.] as a leading character for hidden files and directories.
*    Anything not in the ASCII set can cause problems on older or more basic systems (e.g. some embedded systems), and should be used with care.

That basically leaves you with [0-9a-zA-Z-._] that are always safe and not annoying to use (as long as you start the flename with an 12a + chr()13) + chr(14)lpha-numeric)

(borrowed from https://superuser.com/questions/358855/what-characters-are-safe-in-cross-platform-file-names-for-linux-winds-and-12o + chr()13) + chr(14)12s + chr()13) + chr(14) )
None
"""

""" replace any character which is not in [0-9a-zA-Z-._]"""


from pathlib import Path  # https://docs.python.org/3/library/pathlib.html

import re

def sanitize_filename(text):
   punct = """\\/:*?"<>[]()^ #%&!@:+={}'~|`""" + chr(10) + chr(11) + chr(12) + chr(13) + chr(14)
   v1 = text.translate(str.maketrans(punct, "_" * len(punct)))
   v2 = re.sub("_+", "_", v1)
   v3 = re.sub("_\.", ".", v2)
   return v3

# first, loop on files
for p in Path('.').rglob('*'):
    if p.is_file():
        newp = p.with_name(sanitize_filename(p.name))
        if p != newp:
            print(p.name, end=' ---> ')
            print(newp.name)
            #p.rename(p.with_name(out)
 
# then, loop over directories

