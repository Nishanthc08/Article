# Import the requests module to make HTTP requests
import requests

# Define the URL for searching blog posts on Dev.to
DEV_TO_SEARCH_URL = "https://dev.to/search/feed_content"

# Function to search for blog posts related to a keyword
def search_blog_posts(keyword):
    # Define parameters for the search request
    params = {
        "per_page": 10,  # Limit the results to 10 posts
        "page": 1,  # Start from page 1
        "search_fields": keyword,  # Specify the keyword to search for
        "class_name": "Article"  # Specify the type of content to search for (articles)
    }
    # Send a GET request to the Dev.to search API with the specified parameters
    response = requests.get(DEV_TO_SEARCH_URL, params=params)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the list of blog posts
        return response.json()["result"]
    else:
        # If the request fails, print an error message and return an empty list
        print("Failed to fetch blog posts.")
        return []

# Function to display the blog posts
def display_blog_posts(posts):
    # Check if there are any posts returned
    if posts:
        # Iterate over each post and display its title and URL
        for post in posts:
            title = post["title"]
            url = post["path"]
            print(f"{title}\nRead more: {url}\n")
    else:
        # If no posts are found, print a message indicating that
        print("No posts found related to your keyword.")

# Main function to run the program
def main():
    # Prompt the user to enter a keyword to search for blog posts
    keyword = input("Enter a keyword to search for blog posts: ")
    # Search for blog posts related to the entered keyword
    posts = search_blog_posts(keyword)
    # Display the search results
    display_blog_posts(posts)

# Entry point of the script
if __name__ == "__main__":
    main()
