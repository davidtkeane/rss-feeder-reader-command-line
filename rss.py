import os
import csv
import sys
import time
import feedparser
import pyttsx3
import webbrowser

def load_rss_feed():
    """Loads RSS feed URLs from a CSV file.

    Ensures 'rss_feed' directory and 'rss_feed.csv' file exist.
    If the CSV file doesn't exist, it's created with a 'url' header.
    Reads URLs from 'rss_feed/rss_feed.csv'.

    Returns:
        list: A list of lists, where each inner list contains a URL string.
              Returns an empty list if the file is empty or contains only the header.
    """
    if not os.path.exists('rss_feed'):
        os.makedirs('rss_feed')

    if not os.path.isfile('rss_feed/rss_feed.csv'):
        with open('rss_feed/rss_feed.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['url'])

    with open('rss_feed/rss_feed.csv', 'r') as f:
        reader = csv.reader(f)
        urls = list(reader)

    return urls

def add_rss_feed():
    """Adds a new RSS feed URL to the CSV file.

    Prompts the user to enter an RSS feed URL.
    Appends the entered URL to 'rss_feed/rss_feed.csv'.
    Prints a success message after adding the feed.
    """
    url = input("Enter the RSS feed URL: ")
    with open('rss_feed/rss_feed.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([url])
    print("RSS feed added successfully.")

def remove_rss_feed():
    """Removes an RSS feed URL from the CSV file.

    Loads the list of RSS feeds. If none are found, prints a message and returns.
    Displays the available RSS feeds with a number for selection.
    Prompts the user to choose a feed to remove.
    Validates the user's choice. If invalid, prints an error and returns.
    Removes the selected URL from 'rss_feed/rss_feed.csv'.
    Prints a success message after removing the feed.
    """
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    print("Select an RSS feed to remove:")
    for i, url in enumerate(urls):
        print(f"{i+1}. {url[0]}")

    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(urls):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return

    url = urls[choice-1][0]
    with open('rss_feed/rss_feed.csv', 'w') as f:
        writer = csv.writer(f)
        for u in urls:
            if u[0] != url:
                writer.writerow(u)
    print("RSS feed removed successfully.")

def view_rss_feed():
    """Displays the list of saved RSS feed URLs.

    Loads the list of RSS feeds. If none are found, prints a message and returns.
    Prints each URL with its corresponding number.
    """
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    for i, url in enumerate(urls):
        print(f"{i+1}. {url[0]}")

def open_rss_feed():
    """Opens a selected RSS feed URL in a new web browser tab.

    Loads the list of RSS feeds. If none are found, prints a message and returns.
    Displays the available RSS feeds with a number for selection.
    Prompts the user to choose a feed to open.
    Validates the user's choice. If invalid, prints an error and returns.
    Opens the selected URL in a new browser tab using the `webbrowser` module.
    """
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    print("Select an RSS feed to open:")
    for i, url in enumerate(urls):
        print(f"{i+1}. {url[0]}")

    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(urls):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return

    url = urls[choice-1][0]
    webbrowser.open_new_tab(url)

def fetch_titles(rss_feed_url: str):
    """Fetches and parses titles from an RSS feed URL.

    Args:
        rss_feed_url: The URL of the RSS feed to fetch.

    Returns:
        list: A list of strings, where each string is a title from the RSS feed.
              Returns an empty list if an error occurs during fetching or parsing,
              or if the feed contains no titles.
    """
    try:
        feed = feedparser.parse(rss_feed_url)
        titles = [entry.get('title', 'No Title') for entry in feed.entries]
        return titles
    except Exception as e:
        print(f"Error fetching or parsing RSS feed: {e}")
        return []

def news_ticker(titles: list[str], ticker_speed: float = 0.1):
    """Displays a list of titles as a scrolling news ticker in the console.

    Args:
        titles: A list of strings, where each string is a title to be displayed.
        ticker_speed: The speed of the ticker, in seconds per character.
                      Defaults to 0.1.
    """
    console_width = 80
    padding = ' ' * console_width

    for title in titles:
        line = f"{title} | "
        line_with_padding = padding + line

        for i in range(len(line_with_padding) - console_width + 1):
            print(line_with_padding[i:i + console_width], end='\r')
            time.sleep(ticker_speed)

        print(' ' * console_width, end='\r')

def display_feed_titles(show_progress: bool):
    """Displays RSS feed titles with an optional progress bar and news ticker.

    Loads RSS feeds, prompts the user to select a feed.
    Fetches titles from the selected feed.
    If `show_progress` is True, displays a loading progress bar while fetching.
    Then, displays the fetched titles using the `news_ticker` function.

    Args:
        show_progress: A boolean indicating whether to display the progress bar.
    """
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    print("Select an RSS feed to display:")
    for i, url_item in enumerate(urls): # Renamed url to url_item
        print(f"{i+1}. {url_item[0]}") # Use url_item

    choice_str = input("Enter your choice: ") # Renamed choice to choice_str
    try:
        choice_idx = int(choice_str) # Renamed choice to choice_idx
        if choice_idx < 1 or choice_idx > len(urls):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return

    selected_url = urls[choice_idx-1][0] # Renamed url to selected_url
    titles = fetch_titles(selected_url) # Use selected_url

    if show_progress:
        for i, title in enumerate(titles):
            progress = (i+1)/len(titles)*100
            print(f"Loading... {progress:.2f}%", end='\r')
            time.sleep(0.1)
        print('\n\n')
    
    news_ticker(titles)

def main():
    """Main function to run the RSS feed reader application.

    Presents a menu of options to the user:
    1. Add an RSS feed.
    2. Remove an RSS feed.
    3. View titles with progress & ticker.
    4. View titles with ticker only.
    5. List all RSS feeds.
    6. Open an RSS feed in browser.
    9. Exit.

    Continuously prompts the user for input and calls the appropriate
    function based on the choice until the user chooses to exit.
    """
    while True:
        print("""
    Select an option:

    1. Add an RSS feed
    2. Remove an RSS feed
    3. View titles with progress & ticker
    4. View titles with ticker only
    5. List all RSS feeds
    6. Open an RSS feed in browser
    9. Exit
    """)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_rss_feed()
        elif choice == '2':
            remove_rss_feed()
        elif choice == '3':
            display_feed_titles(show_progress=True)
        elif choice == '4':
            display_feed_titles(show_progress=False)
        elif choice == '5':
            view_rss_feed()
        elif choice == '6':
            open_rss_feed()
        elif choice == '9':
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
