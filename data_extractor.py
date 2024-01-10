import praw
import json
from datetime import datetime

# Function to read credentials from a JSON file
def load_credentials(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load credentials
credentials = load_credentials('reddit_secrets.json')

# Initialize PRAW with credentials from the JSON file
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent=credentials['user_agent'])

# Function to get comments from a post
def get_comments(submission):
    submission.comments.replace_more(limit=0)  # Load all comments, remove limits for more comments
    comments = []
    for comment in submission.comments.list():
        comments.append({
            'author': str(comment.author),
            'body': comment.body,
            'created_utc': datetime.utcfromtimestamp(comment.created_utc).isoformat(),
            'score': comment.score
        })
    return comments

# Function to get post details and comments
def get_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.top(limit=limit):
        post_data = {
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'url': post.url,
            'author': str(post.author),
            'created_utc': datetime.utcfromtimestamp(post.created_utc).isoformat(),
            'num_comments': post.num_comments,
            'selftext': post.selftext,
            'link_flair_text': post.link_flair_text,
            'upvote_ratio': post.upvote_ratio,
            'subreddit': str(post.subreddit),
            'all_awardings': post.all_awardings,
            'permalink': post.permalink,
            'stickied': post.stickied,
            'locked': post.locked,
            'domain': post.domain,
            'comments': get_comments(post)
        }
        posts.append(post_data)

    return posts

# Extract posts and comments from the subreddit
subreddit_name = 'BeautyGuruChatter'  # Replace with the subreddit you're interested in
data = get_posts(subreddit_name, limit=10)

# Save data to a JSON file
with open('reddit_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data saved to 'reddit_data.json'")
