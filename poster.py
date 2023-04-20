import os
from instagrapi import Client
from db import Session, Reel, ReelEncoder
from datetime import datetime
import config
import time

session = Session()


# Update is_posted and posted_at field in DB
def update_status(code):
    session.query(Reel).filter_by(code=code).update({'is_posted': True, 'posted_at': datetime.now()})
    session.commit()


# Get Unposted reels from database
def get_reel():
    reel = session.query(Reel).filter_by(is_posted=False).first()
    return reel


# Magic Starts Here
def main():
    api = Client()
    try:
        api.login(config.USERNAME, config.PASSWORD)
        reel = get_reel()
        if os.path.exists(reel.file_path):
            media = api.clip_upload(
                reel.file_path,
                "Repost From Author : @" + reel.account + " , Caption : " + reel.caption + " " + config.HASHTAGS,
                extra_data={
                    # "custom_accessibility_caption": "alt text example",
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1,
                })

            if media:
                update_status(reel.code)
                #time.sleep(15 * 60)
            main()
            pass

    except Exception as e:
        print(f"Exception {type(e).__name__}: {str(e)}")
        exit()
        pass

if __name__ == "__main__":
    main()
    session.close()