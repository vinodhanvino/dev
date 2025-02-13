import instaloader
import os
username = os.getenv('caterina__rossetti')
password = os.getenv('Goodvibes@0564')

loader = instaloader.Instaloader()

# Load session if exists, else login and save
try:
    loader.load_session_from_file('caterina__rossetti')

    print("✅ Session loaded successfully!")
except FileNotFoundError:

    loader.login(username, password)
    loader.save_session_to_file()
    print("✅ Logged in and session saved!")

    loader.context._default_http_header.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept-Language': 'en-US,en;q=0.9',
    })


hashtag = 'fitness'
hashtag_posts = instaloader.Hashtag.from_name(loader.context, hashtag).get_posts()

count = 0
for post in hashtag_posts:
    loader.download_post(post, target=f'#{hashtag}')
    count += 1
    if count >= 100:
        break

print(f"Downloaded {count} posts with hashtag #{hashtag}.")
