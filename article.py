import requests

DEV_TO_SEARCH_URL = "https://dev.to/search/feed_content"

def search_blog_posts(keyword):
    params = {
        "per_page": 10,
        "page": 1,
        "search_fields": keyword,
        "class_name": "Article"
    }
    response = requests.get(DEV_TO_SEARCH_URL, params=params)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print("Failed to fetch blog posts.")
        return []

def display_blog_posts(posts):
    if posts:
        for post in posts:
            title = post["title"]
            url = post["path"]
            print(f"{title}\nRead more: {url}\n")
    else:
        print("No posts found related to your keyword.")

def main():
    keyword = input("Enter a keyword to search for blog posts: ")
    posts = search_blog_posts(keyword)
    display_blog_posts(posts)

if __name__ == "__main__":
    main()