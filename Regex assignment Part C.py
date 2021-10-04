"""Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one!). 
Each line of the log has the following items:

a host (e.g., '146.204.224.152')
a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:

example_dict = {"host":"146.204.224.152", 
                "user_name":"feest6811", 
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}

"""
import re
def logs():
    data=[]
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
    pattern="""(?P<host>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)
                    (\ - \ )
                    (?P<user_name>(\w*)(\S))
                    (\  \S)
                    (?P<time>\d+\S\w*\S\d+\S\d+\S\d+\S\d+\s\S\d+)
                    (\S\s\S)
                    (?P<request>\w*\s\S*\s\w*\S\d.\d*)
                 """
    for item in re.finditer(pattern,logdata,re.VERBOSE): 
        data.append(item.groupdict())
    return data 
    raise NotImplementedError()
    
assert len(logs()) == 979
one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
