from decouple import config

SETTINGS_TYPE=config("SETTINGS_TYPE",default="PRODUCTION")

if(SETTINGS_TYPE=="DEV"):
    from .dev import *      # NOQA
    print("Using Development Settings")

elif(SETTINGS_TYPE=="PRODUCTION"):
    from .production import *       # NOQA
    print("Using Production Settings")

elif(SETTINGS_TYPE=="HEROKU"):
    from .heroku import *       # NOQA
    print("Using HEROKU Settings")

else:
    from .production import *       # NOQA
    print("!! SETTINGS_TYPE not defined properly in environment. Fallback to Production settings !!")
