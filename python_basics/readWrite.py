# Read test.txt
# Reverse lines
# write
with open('python_basics/test.txt', 'r') as file:
    content = file.read()
    print(content)


# Reverse the content
reversed_content = content[::-1]
print (reversed_content)

# Write the reversed content to a new file
with open('python_basics/test.txt', 'w') as file:
    file.write(reversed_content)



   
  
