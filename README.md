# Real-estate-price-prediction
# Data scrapping

## Description
The goal of this project was to collect information from the [immoweb website](https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance). We had to gather information about at least 10,000 properties all over Belgium and create a CSV file with the following columns.
* __Locality__
* __Type of property__ (House/apartment)
* __Subtype of property__ (Bungalow, Chalet, Mansion, ...)
* __Price__
* __Type of sale__ (Exclusion of life sales)
* __Number of rooms__
* __Living Area__
* __Fully equipped kitchen__ (Yes/No)
* __Surface of the land__ (is none for each line, the information is given in the line : Surface area of the plot of land)
* __State of the building__ (New, to be renovated, ...)
* __...__


The dataset had to be clean in the sense of recording only numerical values. 


## Installation

The following packages were useful in order to make the project work: 

* json (built-in); 
* pandas (pip install pandas);
* bs4 (pip install bs4);
* selenium (pip install selenium);
* threading.
* matplotlib
* sklearn


## Structure of the code

Our program consists of three different parts. The first part of the program is responsible for gathering all the necessary links that will be used for data collection. The second part of the program uses the collected links to scrape information from those webpages. The final step of the program is to "clean" the data that has been collected. This includes removing duplicates and formatting data to have (mainly) numerical values. However, the data is not processed to remove any errors or inconsistencies. 

### 1) Collecting the links
The aim of the [links_collection.ipynb](./data_acquisition/links_collection.ipynb) file is to collect the links of all houses and apartment for sale on the immoweb website. In practice, the house and apartment sections are done in parallel (using threads) and both are following the same algorithm:
* __first__, The algorithm goes through the 333 pages that are available:
* __then__, scrapes these pages to get all the links it contains.
* <img title="333 pages" alt="immoweb picture" src="./images/333_pages.png" width="500">
* __lastly__, This part creates a csv file called [links.csv](./data_acquisition/links.csv) which stores all the links collected.

### 2) Scraping all the links
For all the links that are stored in the links.csv file, [house_scrapping.ipynb](./data_acquisition/house_scrapping.ipynb) will:
* open the link
* scrape the available information
* <img title="one page example" alt="immoweb picture2" src="./images/infos.png" width="300">
* store all the collected information into different csv files called all_info_TeamMember1_1-5000.csv, all_info_TeamMember1_1-10000.csv, all_info_TeamMember2_10000-15000.csv, etc. These files will be merged in the next step of the program. 

In this csv file, each line represents a new house/apartment. The column names are given in the Description section. In this part a special type of multithreading was implemented, which is called teamwork: 
- pip install nicePeople
- from nicePeople import teamwork 

 We have splitted the links (20000 in total) in three to collect the information in parallel. The reason for this was to minimize the risk of being blocked by the immoweb website if we'd have used 'real' concurrency. 

### 3) Cleaning the data

In this last part [merge_and_clean_data.ipynb](./data_acquisition/merge_and_clean_data.ipynb) we will merge all the csv files from the previous part. The dataframe is not clean yet. We only want to retrieve numerical values. So this part of code will include a mapping which is explained in the 'usage' of this 'readme' file.


## Usage

### 1) Collecting the data 
You can use any WebDriver through Selenium to get and extract the URL of each page. The Firefox WebDriver was used in this project with an additional option (headless) which doesn't show the process of opening and closing the pages. 

In order to collect the links of all houses and apartments for sale, we had a look on the website of immoweb and found 333 pages for each property type. This is something you need to check and change manually when running the program. You can also add an additional variable 'end_pagenumber' and scrape this information from the website. 

This workprocess will take about 1 hour. 

### 2) Scraping all the links

This (shared) workprocess can take up to 4 hours when divided between two or more computers. When there's a problem while running, the code will store the scraped information under a CSV file. The program will continue working with a new CSV file. You can add your name to distinguish between team members.

<img title="Saving information" alt="saving" src="./images/saving.png" width="800">

This will of course cause an additional task to merge all the CSV files. The [merge_and_clean_data.ipynb](./data_acquisition/merge_and_clean_data.ipynb) will execute this for you. 

### 3) Cleaning the data

The function 'create_df' will merge all the csv files into a single dataframe. This dataframe will have non-numerical values. In order to get only numerical values we have written the function clean_df. This part of the code will replace string values by numerical values (using mapping). 

## Visuals
In this part we would like to illustrate some visuals about the output of this program. After cleaning the data, the dataframe looks as follows:

<img title="Sample output data" alt="clean dataset" src="./images/cleaned_dataset.png" width="1000">

Here we can see that the dataframe consists only of numerical values like required. We can see that the data is (almost) evenly distributed between the two property types (house/apartment) as we see from the pie chart below:

<img title="Pie chart distribution of data" alt="pie chart" src="./images/piechart.png" width="1000">

# Analysis

On the folder data_analysis I tried to analyse the data that was scrapped during the previous part. You can have an overview of my analysis in the file [Main_analyse](./data_analysis/Main_analyse.ipynb). My main goal was to visualise the influence of the living area on the price of a property.

The following plot shows the price of a property in function of the living area, we do not see any relation between these two variabes.

<div style="text-align: center;">
<img title="Effect of the living area on the price" alt="effect living area" src="./data_analysis/variable_on_price/images/liv_area.jpg" width="550">
</div>

This is due to the fact that each locality has his own price per square meter. We can see on the following graph that there is a clear correlation between the living area of one property and his price, at least for the Locality tested.

<div style="text-align: center;">
<img title="Effect of the living area on the price" alt="effect living area" src="./data_analysis/area_analyse/images/area_1_loc.jpg">
</div>

Testing all the localities one by one would be impossible. This is why I used the following strategy:
* with 80% of the dataset compute the price per square meters for each localities
* with the 20% compare the 2 following thing:
* the price of the property
* the value of (price/sqaure_meter) * living area

The given strategy will gives us a graph comparing two prices, the more the dots will be close to the reference line x=y the more the variable living area is important in the price of a property.

<div style="text-align: center;">
<img title="prediction price" alt="prediction price" src="./data_analysis/area_analyse/images/prediction_price.png">
</div>

While there is still a great variations between the value of the supposed price and the value of the real price we can see that the living area has a great influence on the price

* dots __above__ the line y=x are properties which have a real price lower than expected, it can be caused by a huge propery which has to be renoved
* dots __under__ the line y=x are properties which havea real price higher than expected, it can be caused by a property which is as new,...

# Model
This part is divided in 3 different file:
* __create_csv__, this file will take the csv containing the data we scrapped and create a new csv file that will be used to train and test our model
* __model__, is a file containing my tests on the differents model, hyperparametters, ... (do not run it, it takes time)
* __model_opti__, this file is the model I used.

I used xgboost as regressor model and I got an efficiency of about 76-78%. Here are some visualisations of my results:
At first we can see the effect every features have on the model. We see that the living area and the median price per square meter for each localities and the type of property have the highest influence. We also see that the column price_squared_meter_was_missing has no effect. This is normal in my implementation, indeed the model is train witout missing values on this column.
<div style="text-align: center;">
<img title="effect of features" alt="effect of the features" src="./model_training/images/importance_features.png">
</div>

On the second plot, we see the efficiency of the model, the price the model predicted in function of the real price of the property.
<div style="text-align: center;">
<img title="efficiency" alt="efficiencys" src="./model_training/images/efficiency_model.png">
</div>

Now, let's zoom on the part where real price is under 700000 € (values that interest most of the people). We see that the model overestimate the price of these properties.
<div style="text-align: center;">
<img title="efficiency zoom" alt="efficiency zoom" src="./model_training/images/efficiency_model_zoom.png">
</div>

# API deployment
In this part the goal was to create and deploy an API which predict the price of a property in functions of its features. Also, this part isn't a sucess but I will anyway expose my work. The work was divided into 3 parts:

### Creation a a flask application
The First part is to create a flask application which will create an API which can work locally. You can find the code in the file [app.py](.\API_deployment\app.py). After running the app with python you can find the API with a Post method on the following path: "http://127.0.0.1:5000/predict". The following fields have to be in a dictionnary called _data_ in the request body to make the API work:
* __"Living_Area"__ : int
* __"Type_of_property"__: "HOUSE" or "APARTMENT"
* __"Number_of_rooms"__: int
* __"Locality"__: int
* __"Swimming_pool"__: 0 or 1 (optional)

Here is an example of a request you can make with your terminal:
_Invoke-WebRequest -Method POST -Uri "http://127.0.0.1:5000/predict" -Body '{"data":{"Living_Area": 90, "Type_of_property": "HOUSE", "Number_of_rooms": 4, "Locality": 6637, "Swimming_pool": 0}}' -ContentType "application/json" -Headers @{'Content-Type'='application/json'}_

If the prediction could proceed, the prediction value and the status code 200 will be in the response content. Here is an example of response you can get:
_Content: {"prediction": 215400.0,"status code": 200}_

### Docker
The next part consisted in creating a docker image. This was the tricky part for me. In the previous part of the project I was using  the XGBoost model to make my prediction but here it caused problem. I had hard time loading the model with docker. This is why in this part of the project you will see that I am using a RandomForest regressor. To create the image I had to add 2 files: [_requirements.txt_](.\API_deployment\requirements.txt) and [_Dockerfile_](.\API_deployment\Dockerfile).

As mentionned above this part caused me problems, it is in consequence the reason why I could not finish proprelly and totally all the parts of the project (html page, try except,..). 

### Render.com
The final part consisted in deploying this API online. I used the service render.com. The only steps required is to subscribe, connect his GitHub and deploy the app.
You can see the 'result' with the following [link](https://prediction-app-real-estate.onrender.com/)