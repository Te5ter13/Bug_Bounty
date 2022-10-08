a = 2
b = ("")

stringname = ["Hithere", "hellothere", "sexythere"]
source = "there"



def replaceString(stringname, source, dest, j):
        stringname[j] = dest
        return stringname

def list_to_string(stringList):
    return (",".join([str(elem) for elem in stringList]))


for i in range(0, len(stringname)):
    output_value = replaceString(stringname, source, "'a'", i)
    print(output_value)
    print(list_to_string(output_value))
    stringname[i] = source
