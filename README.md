# python_rss_feeder_cli_with_file_list

# Instructions to Run RSS Feed Reader Script

This script combines the functionality of the three original scripts and adds the requested features. It includes a menu that allows you to choose which functionality to use. The descriptions of each option are included in the menu. The script also includes the ability to load RSS feed URLs from a CSV file, select a specific URL to display, or display a random URL. If the 'rss_feed' directory or 'rss_feed.csv' file do not exist, they will be created when the script is run.

## Prerequisites
- Python 3.6 or above.
- Required packages can be installed using the following command `pip install -r requirements.txt`

## Steps to run the script
1. Clone the repository using the command `git clone <repository-url>`
2. Navigate to the directory containing the script using the command `cd <directory-name>`
3. Install the required packages by running the command `pip install -r requirements.txt`
4. Run the script using the command `python rss.py`
5. Follow the prompts to add, remove, view and open RSS feeds. 
6. I have added a rss_feed/csv with some random rss links, like the BBC, CNN and others. Add your own rss urls there.

Note: When prompted to enter an RSS feed URL, please make sure to provide a valid URL.

Thank you for using the RSS Feed Reader script created by Genie!# Instructions to Run RSS Feed Reader Script

This script combines the functionality of the three original scripts and adds the requested features. It includes a menu that allows you to choose which functionality to use. The descriptions of each option are included in the menu. The script also includes the ability to load RSS feed URLs from a CSV file, select a specific URL to display, or display a random URL. If the 'rss_feed' directory or 'rss_feed.csv' file do not exist, they will be created when the script is run.

## Prerequisites
- Python 3.6 or above.
- Required packages can be installed using the following command `pip install -r requirements.txt`

## Steps to run the script
1. Clone the repository using the command `git clone <repository-url>`
2. Navigate to the directory containing the script using the command `cd <directory-name>`
3. Install the required packages by running the command `pip install -r requirements.txt`
4. Run the script using the command `python rss_feed_reader.py`
5. Follow the prompts to add, remove, view and open RSS feeds. 

Note: When prompted to enter an RSS feed URL, please make sure to provide a valid URL.

Thank you for using the RSS Feed Reader script created by Genie!

Here are some suggestions for improving the RSS Feed Reader script:

- **Implement error handling:** The current script assumes that every function operates successfully without any errors. However, it's always a good practice to implement error handling code that can gracefully handle unexpected errors.

- **Add support for more RSS feeds:** Currently, the script only supports one feed at a time. You could modify the script to allow for multiple RSS feeds to be processed at once.

- **Introduce command line arguments:** Consider implementing command-line arguments to allow the user to specify which RSS feed to process and how many articles to read at a time. This would make the script more flexible and customizable.

- **Add logging capabilities:** Including logging statements throughout your codebase is a great way to keep track of what's going on under the hood of your program. It also allows you to debug issues with greater ease.

- **Allow customization of output format:** Currently, the script outputs the article title, author, and summary in a specific format. This may not be ideal for all users. Consider adding an option to customize the output format to better suit different needs.

- **Implement caching**: To reduce the amount of requests made to the feed server, you could store the data locally and update it when needed. This will help reduce bandwidth usage and speed up your program as well.

These are just a few suggestions but I hope they help you improve your script!
