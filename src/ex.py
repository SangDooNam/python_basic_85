


#Task 1
# with open(file='data/task1.txt', mode='r') as task1:
#     content = task1.read()
#     print(content)
    
    
#Task 2
# with open(file='data/task2.txt', mode='r') as task2:
#     content = task2.readlines()
#     re_1 = [i.replace(':', '') for i in content]
#     re = [i.replace('\n', '') for i in re_1]
#     key = re[0] + re[1]
#     todo = {key: [i for i in re[2:]]}
#     print(todo)
#     print(len(todo[key]))


#Task 3
with open(file='data/task3.txt', mode='r') as task3:
    content = task3.readlines()
    odd = [content[i] for i in range(len(content)) if bool((i+1)%2)]
    even = [content[i] for i in range(len(content)) if not bool((i+1)%2)]
    combined = odd + even
    result = ''.join(combined)
    print(result)


#Task 4

# with open(file='data/task4.txt', mode='r') as task4:
#     content = task4.readlines()
#     txt = ''.join(content)
#     print(txt[1622:1634+1])


#Task 5

# with open(file='data/task5.txt', mode='r') as task5:
#     content = task5.readline(70)
#     pointer = task5.tell()
#     print(content)
#     print(pointer)




#Task 6

# with open(file='data/task6.txt', mode='r') as task6:
#     result = []
#     while True:
#         line = task6.readline()
#         if not line:
#             break
#         count = 0
        
#         for i in line:
#             count += 1
        
#         if line.endswith('\n'):
#             count -= 1
#         result.append(count)
#     print(result)
        
