'''
This is a simple python script that checks if two pdf files are identical or not

'''

#First we read the content of both files



try:

    with open("data1.pdf", "r") as f:

        data1 = f.read()


    with open("data2.pdf", "r") as f:

        data2 = f.read()



    if data1 == data2:

        print(f"Both pdf files are identical\n {data2}\n {data1} ")


    else:

        print(f"Both are different \n {data1} \n {data2}")


#What if file not found... 
except Exception as e: 

    raise FileNotFoundError
