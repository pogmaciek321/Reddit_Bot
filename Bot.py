import praw
import config
import os
import time
def Reddit_login():
    log=praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "pogmaciek's bot test v0.1" )
    return log
def Run_bot(log,comments_replied_to):
    my_name = str(log.user.me())
    print("Bot username:", my_name)
    comments = list(log.subreddit('testingground4bots').comments(limit=20))
    print("Pobrano komentarzy:", len(comments))
    for comment in comments:
        print("Komentarz:", comment.body)
        author_name = str(comment.author) if comment.author else ""
        if ("dog" in comment.body.lower()
            and comment.id not in comments_replied_to
            and author_name.lower() != my_name.lower()):
                try:
                    comment.reply("what the dog doin")
                    print("comment found"+comment.id)
                    comments_replied_to.append(comment.id)
                    with open("comments_replied_to.txt","a")as f:
                        f.write(comment.id+"\n")
                    print(f"Zapisano do pliku: {comment.id}")
                except Exception as e:
                    print(f"nie udalo sie odpowiedziec")
        
def read_comments_from_file():
    if not os.path.isfile("comments_replied_to.txt"):
        return []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = [line.strip() for line in f if line.strip()]
    return comments_replied_to

log=Reddit_login()
comments_replied_to = read_comments_from_file()
while True:
    Run_bot(log,comments_replied_to)
    print("czekam troche")
    time.sleep(30)