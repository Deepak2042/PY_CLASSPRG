def delchar(str,chr):
    val=""
    for i in str:
        if chr!=i:
            val+=i
    return val

value=input("Enter the string: ")
c=input("Enter a character to be deleted: ")

new_str=delchar(value,c)
print("String after character removed: ",new_str)
            
