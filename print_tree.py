import os

# adopted and modified from here:
# http://stackoverflow.com/a/120701/241852
#

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    # for subdirname in dirnames:
        # print "----" + os.path.join(dirname, subdirname)
    print dirname + "+"
    # print path to all filenames.
    for filename in filenames:
        print " " *len(dirname) + "|->" + os.path.join(filename)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
