import praw
import config
def Reddit_login():
    log=praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "pogmaciek's bot test v0.1" )
    return log
def Run_bot(log,comments_replied_to):
    
    for comment in log.subreddit('testofredditbot321').comments(limit=25):
         if ("dog" in comment.body.lower()
            and comment.id not in comments_replied_to
            and comment.author != log.user.me()):
            comment.reply("what the dog doin")
            comments_replied_to.append(comment.id)
        


log=Reddit_login()
comments_replied_to = []
while True:
    Run_bot(log,comments_replied_to)
