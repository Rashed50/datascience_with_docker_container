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

### I think till this step everything fine.
    but here you have to create everytime new container becasue if container exist system will 
    show duplicate container when you run above container run command. So we can do other way where
    you don't need to execute everytime docker build and run command. Now create another bash file
    which name is "run.sh". inside the file write the below programe 

```
    # Stop and remove existing container if it exists
    docker rm -f docker_container_name 2>/dev/null

    # Build the image
    docker build -t docker_image_name .

    # Run the container
    docker run --name docker_container_name docker_image_name

    # Copy output from container to host
    docker cp docker_container_name:/app/output.csv .

    # Optional: remove container after run
    docker rm docker_container_name

```

# Now run the run.sh bash file from bash terminal
    Above all command we excute using cmd terminal. But bash command  run in ubuntu,
    linux or macos system.So how to run bash command in window. To do this just 
    open you terminal from your project folder (How you can do , I already descibe
     in above description). Then type just "wsl" and press enter command that will changed
    you cmd terminal to bash command. where you will "root/your_computer_user_name"
     instead of your project  folder name. Now you have to give excute permission 
     on your "run.sh" file. Now you can execute below command
     
```
    chmod +x run.sh  
    bash run.sh or ./run.sh
```

First line is for giving excution permission to the login user
Second line will run the run.sh file where we mentioned to build docker image
then run docker container using builded docker image. After successfully run every things 
docker container will remove by excuting last line.





