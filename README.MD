# Frame Work Setup #
<br>Developed based on py unit testing framework </br>
Project structure

```bash
├── README.MD
├── allure_report
├── data
├── reports
├── requirements.txt
├── resources
├── tests
├── utils


```

## Pre prerequisites ##
Install  python latest version https://www.python.org/downloads/
```
python --version
```

**Project set up**
<br>Create a project folder with virtual env
<br>More about virtual env https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ </br>
<br>Clone the project from the repo</br>
<br>Go to terminal and install all required dependencies using requirements.txt </br>
<br> Use your prefred editor </br>
```
pip install -r requirements.txt
```
<br> Open the properties.ini and provide your file paths</br>

```commandline
input_file_path = /data/input/input_file.1630412935.1658413040.txt
output_file_path = /data/output/ouput_file.1630412935.1658413040.txt
report_file_path = /reports/
```

## Execute the tests ##
* All test cases resides in the tests folder
* Navigate to the rood folder and execute the below command
* Reports will be generated in the reports folder as a text file
```
python -m unittest tests/CoordinateTests.py
```
* Reports will look like below


<img width="317" alt="Screenshot 2022-08-13 at 12 52 27" src="https://user-images.githubusercontent.com/5151534/184473609-7b44dae0-5c48-4cea-9d6f-364952cdabe7.png">

### Generating Allure Report ###
* Below command will generate the allure report, but in our case we have to check multiple points report body contains the detail results
```
 py.test tests/CoordinateTests.py --alluredir=allure_report 
```
```commandline
allure serve allure_report 
```
* Report will look like below

<img width="1792" alt="Screenshot 2022-08-13 at 12 48 15" src="https://user-images.githubusercontent.com/5151534/184473545-f4710e01-0242-4472-b3d4-5636fe78002d.png">
<img width="1791" alt="Screenshot 2022-08-13 at 12 48 59" src="https://user-images.githubusercontent.com/5151534/184473542-e7c4996e-a078-4018-8931-28e89d5a96db.png">