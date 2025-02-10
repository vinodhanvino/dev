import instaloader

# Initialize Instaloader
loader = instaloader.Instaloader()

# Login to Instagram
username = "caterina__rossetti"
password = "Goodvibes@0564"

try:
    loader.login(username, password)
    print("✅ Logged in successfully!")
except Exception as e:
    print("❌ Login failed:", e)

# Instagram post URL
post_url = input("Enter the Instagram post URL: ")
shortcode = post_url.strip().split("/")[-2]

# Download the video
try:
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target='/storage/downloads')
    print("✅ Video downloaded successfully!")
except Exception as e:
    print("❌ Error:", e)
