from notebook import Notebooks
import asyncio

test_data = {1: ['result=10','result2 = result * 10','print("result2 should be 100 and it is= ",result2)'], 
             2:['result=222', 'result2 = result * 10','print("result2 should be 2220 and it is= ",result2)']}

codeInter = Notebooks()

n = len(list(test_data.values())[0])

for i in range(n):
    for k in test_data.keys():
        print("Code result for test: ", k)
        result =  asyncio.run(codeInter.execute_new_code(test_data[k][i],k))

        print(result)