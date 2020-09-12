# NCDC Covid -tracker
Serverless web scraper for real-time covid-19 data in Nigeria. 

- Data gotten from [NCDC's](https://covid19.ncdc.gov.ng/) official website
- Web scraper built with python using `BeautifulSoup` and `requests` modules
- Scheduled scraping with **AWS lambdas** and **AWS CloudWatch**

## Requirements

You can install requirements using the pip package manager by running
```
pip3 install datetime beautifulsoup4 requests lxml
```

## Command line usage
To manually scrape the data from NCDC, run
```
python3 naijacovidscraper.py
```

### AWS Setup
1. Create an S3 bucket.
2. Create AWS `LambdaExecute` policy to access S3 bucket.
3. Create a new AWS Lambda and upload zipped python script (with dependencies)
4. Create a Lambda function (see lambda_function.py) and add layer in Step 4.
5. Create new Event/rule using **AWS CloudWatch**
 > cron expression for 12 hourly schedule: `0 */12 * * ? *`
 
