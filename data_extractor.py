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

# Function to check if the post is related to MAC cosmetics
def is_mac_related(text):
    # keywords = [
    #     "MAC", "Mac cosmetics", "MAC lipstick", "MAC makeup",
    #     "MAC Studio Fix", "MAC Pro Longwear", "MAC Mineralize", "MAC Prep + Prime", "MAC Viva Glam",
    #     "Ruby Woo lipstick", "Cremesheen Lipstick", "Retro Matte", "MAC Eyeshadow", "MAC Foundation",
    #     "MAC Concealer", "Fluidline", "Fix+ Spray", "Strobe Cream",
    #     "MAC blush", "MAC mascara", "MAC eyeliner", "MAC brush", "MAC palette", "MAC skin", "MAC face",
    #     "Rihanna MAC", "Selena MAC", "MAC Holiday Collection", "MAC Summer Collection",
    #     "M·A·C", "M.A.C.", "mac makeup", "mac cosmetics", "mac beauty products",
    #     "#MACCosmetics", "#MACLovers", "#MACMakeup", "#MACArtist", "#MACAddict",
    #     "Professional makeup", "Cosmetic artistry", "Beauty influencer MAC", "Makeup tutorial MAC"
    # ]
    keywords = [
        ""
    ] 
    return any(keyword.lower() in text.lower() for keyword in keywords)

# Function to get comments from a post
def get_comments(submission):
    submission.comments.replace_more(limit=0)  # Load all comments
    comments = []
    for comment in submission.comments.list():
        if str(comment.author) != 'None':
            comments.append({
                'author': str(comment.author),
                'body': comment.body,
                'created_utc': datetime.utcfromtimestamp(comment.created_utc).isoformat(),
                'score': comment.score
            })
    return comments


# Function to get author details
def get_author_details(author_name):
    try:
        author = reddit.redditor(author_name)
        author_subreddit = author.subreddit  # Get the UserSubreddit object
        return {
            'name': author.name,
            'description': author_subreddit.public_description if author_subreddit else None,
            'total_karma': author.link_karma + author.comment_karma,  # Total karma (post + comment)
            'link_karma': author.link_karma,  # Link karma
            'comment_karma': author.comment_karma,  # Comment karma
            'account_created_utc': datetime.utcfromtimestamp(author.created_utc).isoformat(),  # Account creation date
            'is_employee': author.is_employee,  # Reddit employee status
            'has_verified_email': author.has_verified_email  # Whether the user has a verified email
        }
    except Exception as e:
        print(f"Error fetching author details: {e}")
        return None


# Function to get post details and comments
def get_posts(subreddit_name, keyword_limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    count = 0

    for post in subreddit.top(limit=None):  # Search through a larger pool of posts
        if is_mac_related(post.title) or is_mac_related(post.selftext) or (str(post.author) != 'None'):
            author_details = get_author_details(str(post.author))
            post_data = {
                'title': post.title,
                'score': post.score,
                'id': post.id,
                'url': post.url,
                # 'author': str(post.author),
                'author_details': author_details,
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
            count += 1
            if count >= keyword_limit:
                break
    return posts

# Extract MAC-related posts and comments from the subreddit
subreddit_name = 'BurgerKing'
data = get_posts(subreddit_name, keyword_limit=10)

# Save data to a JSON file
with open('reddit_data_lego.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data saved to 'reddit_data_lego.json'")
