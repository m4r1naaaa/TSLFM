import os
from colorama import Fore
from zipfile import ZipFile
import shutil

if os.path.exists(os.path.expanduser('~') + "/recycbin") == False:
    os.makedirs(os.path.expanduser('~') + '/recycbin', exist_ok=True)
else:
    pass

version = "tfm v0.4 (reimu)"
def ls(dir):
    try:
        f = os.listdir(dir)
    except FileNotFoundError:
        print(Fore.RED + dir + ": No such file or directory" + Fore.WHITE)
    except PermissionError:
        print(Fore.RED + dir + ": Permission denied" + Fore.WHITE)
    try:
        for i in f:
            if os.path.isdir(dir+"/"+i) == True:
                print(Fore.GREEN + i + Fore.WHITE)
            else:
                print(i)
    except:
        pass
def touch(action, type, dir):
    try:
        i = os.getcwd() + "/" + dir
    except FileNotFoundError:
        print(Fore.RED + dir + ": No such file or directory" + Fore.WHITE)
    try:
        if action == "mk":
            if type == "dir":
                os.mkdir(os.getcwd() + "/" + dir)
            elif type == "file":
                open(os.getcwd() + "/" + dir, "x")
        elif action == "rm":
            if type == "dir":
                os.rmdir(os.getcwd() + "/" + dir)
            elif type == "file":
                os.remove(os.getcwd() + "/" + dir)
    except:
        pass


print(version+"\nRun 'help' for help.")
while True:
    i = input(">>>")
    if i.startswith("ls ") == True:
        d = i.replace("ls ", "")
        if d == "cwd":
            print(Fore.BLUE + os.getcwd() + Fore.WHITE + ":")
            ls(os.getcwd())
        elif d == "bin":
            print(Fore.BLUE + os.path.expanduser('~') + '/recycbin' + Fore.WHITE + ":")
            ls(os.path.expanduser('~') + '/recycbin')
        else:
            print(Fore.BLUE + d + Fore.WHITE + ":")
            ls(d)
    elif i.startswith("cd ") == True:
        d = i.replace("cd ", "")
        try:
            os.chdir(d)
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("rmdir ") == True:
        d = i.replace("rmdir ", "")
        try:
            touch("rm", "dir", d)
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("mvbin ") == True:
        d = i.replace("mvbin ", "")
        try:
            shutil.move("./" + d, os.path.expanduser('~')+"/recycbin/"+d)
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("rmbin") == True:
        try:
            shutil.rmtree(os.path.expanduser('~') + '/recycbin')
            os.mkdir(os.path.expanduser('~') + '/recycbin')
        except PermissionError:
            print(Fore.RED + d + ": Permission denied! Check permissions for ~/recycbin." + Fore.WHITE)
    elif i.startswith("mkdir ") == True:
        d = i.replace("mkdir ", "")
        try:
            touch("mk", "dir", d)
        except FileExistsError:
            print(Fore.RED + d + ": Directory already exists" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("rm ") == True:
        d = i.replace("rm ", "")
        try:
            touch("rm", "file", d)
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("mk ") == True:
        d = i.replace("mk ", "")
        try:
            touch("mk", "file", d)
        except FileExistsError:
            print(Fore.RED + d + ": File already exists" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("uz ") == True:
        d = i.replace("uz ", "")
        try:
            with ZipFile(d, 'r') as f:
                f.extractall()
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("prn ") == True:
        d = i.replace("prn ", "")
        try:
            f = open(d, 'r')
            print(f.read())
        except FileNotFoundError:
             print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
             print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("app ") == True:
        d = i.replace("app ", "")
        try:
            i = input("Append> ")
            f = open(d, 'a')
            f.write(i)
        except FileNotFoundError:
             print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
             print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i.startswith("rn ") == True:
        d = i.replace("rn ", "")
        i = input("New name>")
        try:
            os.rename(d, i)
        except FileNotFoundError:
            print(Fore.RED + d + ": No such file or directory" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + d + ": Permission denied" + Fore.WHITE)
    elif i == "clear":
        os.system("clear")
        print(version + "\nRun 'help' for help.")
    elif i == "help":
        print(version + "help: Displays this message.\nclear: Clears the screen.\nbye: Exits.\nmk(dir): Makes a file/directory.\nrm(dir): Removes a file/directory.\nls: Lists the directory (do 'ls cwd' to list current working directory and 'ls bin' to list the recycling bin).\ncd: Changes current working directory.\nuz: Unzips a zip file.\napp: Appends text to a file.\nprn: Prints the contents of a file.\nrn: Renames a file.\nmvbin: Moves to the recycling bin (/recycbin).\nrmbin: Empties the recycling bin.")
    elif i == "bye":
        exit()
