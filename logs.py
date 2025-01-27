from colorama import Fore, Style
import instaloader

print(Style.BRIGHT + Fore.GREEN + " ")
print("   _____            _       ____  ___         ___            __                ")
print("  / ___/____  _____(_)___ _/ /  |/  /__  ____/ (_)___ _     / /___  ____ ______")
print("  \__ \/ __ \/ ___/ / __ `/ / /|_/ / _ \/ __  / / __ `/    / / __ \/ __ `/ ___/")
print(" ___/ / /_/ / /__/ / /_/ / / /  / /  __/ /_/ / / /_/ /    / / /_/ / /_/ (__  ) ")
print("/____/\____/\___/_/\__,_/_/_/  /_/\___/\__,_/_/\__,_/____/_/\____/\__, /____/ ")
print(Fore.YELLOW + "  | - >" + Fore.WHITE + "  version 1.0" + Fore.GREEN + "                               /_____/       /____/")
print(Fore.YELLOW + "  | - - >" + Fore.GREEN + "  CATCH ALL USER LOGS INTO SOME SOCIAL MEDIA")
print(Fore.YELLOW + "  | - - - >" + Fore.WHITE + "  www.github.com/joaoguilhermemendes/SociaMedia_logs")
print(" ")
print(" ")
print(Fore.YELLOW + "[ 1 ]" + Fore.WHITE + " INSTAGRAM")
print(Style.DIM + "[ 2 ]" + Fore.WHITE + " TWITTER")
print(Style.DIM + "[ 3 ]" + Fore.WHITE + " FACEBOOK")
print(Style.RESET_ALL + " " + Style.BRIGHT)

social_media = int(input(Fore.YELLOW + "Select the social media: (e.g. 1) - " + Fore.WHITE))
user = str(input(Fore.YELLOW + "Username: (e.g. username) - " + Fore.WHITE))

print("-----------------------------------------------------------------------------")
print(Style.RESET_ALL + " " + Style.BRIGHT)

loader = instaloader.Instaloader() # Create an instance of Instaloader class

profile = instaloader.Profile.from_username(loader.context, user) # Get the profile of the user
full_name = profile.full_name
bio = profile.biography
followers = profile.followers
followees = profile.followees
posts = profile.mediacount

print(Fore.GREEN + "User: " + Fore.WHITE + f"{user}")
print(Fore.GREEN + "Name: " + Fore.WHITE + f"{full_name}")
print(Fore.GREEN + "Bio: " + Fore.WHITE)
print(f"{bio}")

print(" ")
print(" ")

print(Fore.GREEN + "Followers: " + Fore.WHITE + f"{followers}")
print(Fore.GREEN + "Following: " + Fore.WHITE + f"{followees}")
print(Fore.GREEN + "Posts: " + Fore.WHITE + f"{posts}")
posts = []
print(Fore.YELLOW + "|") 
for index, post in enumerate(profile.get_posts(), 1): # Get the posts of the user
    posts.append(post)
    print(Fore.YELLOW + "| - - - >" + Fore.GREEN + f" [{index}]" + Fore.WHITE + f" {str(post.date)[:10]}")

print(" ")
print(" ")

more_info = str(input("More info (Y/N)? ")).upper()
while more_info == 'Y':    
    post_index = int(input("Select the log index number: "))

    print("-----------------------------------------------------------------------------")
    print(" ")

    print(Fore.GREEN + "DESCRIPTION: " + Fore.WHITE + f"{posts[post_index-1].caption}")
    print(" ")
    print(Fore.GREEN + "POST: " + Fore.WHITE + f"{post_index}")
    print(Fore.GREEN + "LIKES: " + Fore.WHITE + f"{posts[post_index-1].likes}")
    print(Fore.GREEN + "COMMENTS: " + Fore.WHITE + f"{posts[post_index-1].comments}")
    print("|")

    loader.login('usename', 'password') # Login with your user and password
    for comment in posts[post_index-1].get_comments(): # Get the comments of the selected post
        print("| - - > " + Fore.RED + f"@{comment.owner.username}: " + Fore.WHITE + f"{comment.text}")

    print(" ")
    print("-----------------------------------------------------------------------------")
    print(" ")
    more_info = str(input("More info (Y/N)? ")).upper()

print(" ")
print(" ")
print(" ")
print(Fore.YELLOW + "----------------------------------------- END ------------------------------------")
print(" ")
print(" ")
print(" ")