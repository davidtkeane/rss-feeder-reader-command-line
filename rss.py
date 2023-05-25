import os
import csv
import sys
import time
import feedparser
import pyttsx3

def load_rss_feed():
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
    url = input("Enter the RSS feed URL: ")
    with open('rss_feed/rss_feed.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([url])
    print("RSS feed added successfully.")

def remove_rss_feed():
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
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    for i, url in enumerate(urls):
        print(f"{i+1}. {url[0]}")

def open_rss_feed():
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

def fetch_titles(rss_feed_url):
    feed = feedparser.parse(rss_feed_url)
    titles = [entry.get('title', 'No Title') for entry in feed.entries]
    return titles

def news_ticker(titles, ticker_speed=0.1):
    console_width = 80
    padding = ' ' * console_width

    for title in titles:
        line = f"{title} | "
        line_with_padding = padding + line

        for i in range(len(line_with_padding) - console_width + 1):
            print(line_with_padding[i:i + console_width], end='\r')
            time.sleep(ticker_speed)

        print(' ' * console_width, end='\r')

def fetch_titles_progress(rss_feed_url):
    feed = feedparser.parse(rss_feed_url)
    titles = [entry.get('title', 'No Title') for entry in feed.entries]
    return titles

def option_5():
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    print("Select an RSS feed to display:")
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
    titles = fetch_titles_progress(url)

    for i, title in enumerate(titles):
        progress = (i+1)/len(titles)*100
        print(f"Loading... {progress:.2f}%", end='\r')
        time.sleep(0.1)

    print('\n\n')
    news_ticker(titles)

def option_6():
    urls = load_rss_feed()
    if not urls:
        print("No RSS feeds found.")
        return

    print("Select an RSS feed to display:")
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
    titles = fetch_titles(url)
    news_ticker(titles)

def main():
    while True:
        print("""
Select an option:

1. Add an RSS feed
2. Remove an RSS feed
3. Select a RSS feed to view stories
9. Exit
""")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_rss_feed()
        elif choice == '2':
            remove_rss_feed()
        elif choice == '4':
            option_6()
        elif choice == '3':
            option_5()
        elif choice == '9':
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

