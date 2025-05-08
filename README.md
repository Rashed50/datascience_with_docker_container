## Run a Python programe using Docker in Windows Computer
    

### Create a Project folder where all your project files will exist.
    after creating project folder open your computer terminal. Crate a file called Dockerfile.
    For creating this just open your notepad application and save the file by giving name is Dockerfile,
    One thing you have to remaind here this file has no extention.Then write below programe.
    Here I used "pandas-csv-app" as project folder 

```
    FROM python:3.10-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    CMD ["python", "main.py"]
```

### details of the above programe
    Here first line used becasue this docker_image will use python 3.10 version when will create 
    docker_image 
    
    Second line means inside docker a folder is exist called  "app" folder that will 
    be used as workdirectory for this project.
    
    Third line for requirements of library that will use for this program. 
    
    Fourth line will install all the required library that already have mentioned inside the 
    "requirements.txt" file last line for run the  python program file from your terminal.
     After next step, here I will create a python file that name is "main.py"

### Now create requirements.txt 
    Inside this  file write all your required library that you need. Here I just used the "pandas"
    library , so I just typed pandas.If you need more just type more below pandas name


```
   pandas
``` 


### Create python programe called "main.py"
    Now here you have to create any python program file that will run on docker environment. 
    Here I created "main.py" file that contains below programe.I written the programe with comments 
    so it will be easy for you to understand.Here you have to ensure that inside your project
    folder there are two csv files one is called "input.csv" and another one is 
    "data_ecommerce_customer_churn.csv". You can also use excel file but in that case you must
    have to input the excel format instead of "csv". 

```
    import pandas as pd

    # Correct function name: read_csv, not read.csv
    df = pd.read_csv('input.csv')
    print(df)  # print the data that read from input.csv file

    print("Processed data written to output.csv:")
    ccd = pd.read_csv('data_ecommerce_customer_churn.csv')
    # write the reading data to output.csv file
    ccd.to_csv('output.csv', index=False)

    # print the reading data to output. After successfully run the programe you will the
    data in terminal that exist inside your csv file.
    print(ccd.head(5))
 
```

### Now time Build Docker Image and Contaiter and then Run 

    To run this python programe using docker first of all you need to install Docker Desktop
    in your desktop computer if you don't have.For installing docker you can see any installation
    tutuorial. For opening, just Open your Docker Desktop in windows machine. All other functions
    will run using command from terminal. Now open you cmd command promt. then go to your project 
    folder by using below command. you can do this by two way one is open cmd terminal and using cd 
    command. another is you can go to project folder then from address bar , select your address 
    and remove the address then just you can type "cmd" and presss ente It will open terminal from 
    inside your folder. you will see project folder in the terminal . Then run the below command


```
    docker built -t docker_image_name .
```
    Her I use pandas-image as docker_image_name . you can use any name that you like .But just remember
    the name becasue later on you will need that name to build container. Do not forget to give space 
    then dot(.) after docker image name. otherwise you will get error.now run belwo command to build
    docker container

```
    docker run --name docker_container_name docker_image_name
```






