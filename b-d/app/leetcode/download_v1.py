from instagrapi import Client

import os
username = 'caterina__rossetti'
password = 'Goodvibes@0564'
cl = Client()
# cl.login(username, password)
# cl.dump_settings("session.json")
try:
    cl.load_settings("session.json")
    cl.login(username, password)

except:
    print("Session expired. Logging in again.")
    cl.login(username, password)
    cl.dump_settings("session.json")
#
#
# # # Get posts for a hashtag
# def get_recent_posts(hashtag, count=2):
#     medias = cl.hashtag_medias_v1(hashtag, amount=count, tab_key='top')
#     post_links = [f"https://www.instagram.com/p/{media.code}/" for media in medias]
#     return post_links
#
# # Example usage
# hashtags = ["Modi"]
# for tag in hashtags:
#     links = get_recent_posts(tag, count=2)
#     print(f"Recent posts for #{tag}:")
#     for link in links:
#         print(link)
#     print("-" * 40)
profile_name = "DK Suresh"  # Replace with the desired profile name
user_info = cl.user_info_by_username(profile_name)

# Display User Info
print(f"Username: {user_info.username}")
print(f"Full Name: {user_info.full_name}")
print(f"Followers: {user_info.follower_count}")
print(f"Bio: {user_info.biography}")

# 3️⃣ Fetch Recent Posts
user_id = user_info.pk
posts = cl.user_medias(user_id, amount=5)  # Get the latest 5 posts

# 4️⃣ Display Recent Posts
for post in posts:
    print(f"Post URL: https://www.instagram.com/p/{post.code}/")
    print(f"Caption: {post.caption_text}")
    print(f"Likes: {post.like_count}, Comments: {post.comment_count}")
    print("-" * 40)