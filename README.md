# Nagios data parser

This is a simple parser for Nagios OMD data, the data in the OMD file is in a raw format and this script parses it into a JSON format and viceversa.  
It's written in Python 3 and uses the [pandas](https://pandas.pydata.org/) library to convert the JSON data into excel to work easily.  
It also adds the official images to the JSON data and then parses it back to the OMD file format so you can update the file in your server (or maybe just run the script on your server with all the paths correctly configured).  

## Usage
I recommend using this script with a virtual environment, you can create one by running:  
```bash
python -m venv venv
or
pipenv shell # This will create a virtual environment and install the requirements , but you have to install pipenv first by running:
pip install pipenv
```
Install the requirements:  
```bash
pip install -r requirements.txt
```

Run the script:  
```bash
python raw_data_processing.py
```
This may not work if you didn't provide the raw data to the script. You can found some example data in 'raw.txt' file.  
(This is not real data and wont work if you try to use it in your OMD server you have to adjust the data)  

Once you have run at least once the script, you can edit the excel file and then run the `excel_to_raw.py` script to update the file `updated_data.txt`, then you'll be able to copy paste this file into your server `hosts.cfg` file, also you can run the script from your server and change the `updated_data_path` variable in the script to save it in your configuration folder directly.  

## Configuring script
You can 'configure' the script to your needs by changing the variables in the script:  
```python
# Variables
raw_file_path = 'raw.txt' # Path to the raw data file
json_file_path = 'parsed.json' # Path to the JSON file
excel_file_path = 'data.xlsx' # Path to the excel file
updated_data_path = 'updated_data.txt' # Path to the updated data file
```

Other than that, you can add more images by adding more lines in this format to the dictionary `official_images` in the script:  
```python
# Images
official_images = {
        'host_name': 'image.png'
    }
```
Note that you have to also add the images to the `images` folder in the server.  (You have the basic type images in the  `logos` folder)

Also please add the official keys to the list `official_keys` in the script:  
```python
# Keys
official_keys = ['host_name','alias','parents','use','address','contact_groups','icon_image']
```
This is used to check if the data is valid or not and also to fix some errors with non filled fields.  

## License
Afa Systems © [Afa](http://www.afasystems.it/)
