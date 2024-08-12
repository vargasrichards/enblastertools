'''
User-configurable Python plugin allowing for advanced functionality.
To use this plugin, you must specify

    plugin : "TRUE"

in the primary configuration ('config.yaml') file. The plugin will be produces as part of the reproducibility file,
which contains everything needed to re-perform the fetching/analysis. 

------------------------------------------------------------------------------------------------------------
Security Note: be careful before running an untrusted plugin; if in doubt do not run before vetting the code.

A. Vargas Richards, 12.08.2024, <ar2185@cam.ac.uk>
'''

#-----------------BEGIN USER MODIFIABLE-------------------------
# These define the 
def include1():
    return 

def include2():
    return

def constructor1():

    return

def constructor2():
    return 

#-------------------END USER MODIFIABLE----------------------------


#---------------------BEGIN IMMUTABLE------------------------------
# The function below performs reporting.

#---------------------END IMMUTABLE--------------------------------











#--------------------------------------------------------------------
'''

[...] constructor3() etc ... 

can call as many constructors as  the user writes, to for example generate multiple files under different
filters. 

'''

def main(): 
    constructor1()
    constructor2()
    return 

main()