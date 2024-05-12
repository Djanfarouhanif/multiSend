import tweepy


api_key = "DIS2RIvaWkMP9Dyq5eot1ikpr"
api_secret = "hFAYZLFuCo520WgBbHtoKuN0lTsHMaaCLhP6CTsiFVhsoA2hnt"

access_token = "1716570629871431680-yVw0XN7flPEbholQR90byCVseWRsXc"

access_secret = "mfXCDEE6z3yj1KeoPRbpoXGhjajDR2noZYP6haH8sGTc4"
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

print(f"******{auth}*******")
def SendMessage(api_k, api_s, access_t, access_s):
    try: 
        auth = tweepy.OAuthHandler(api_k, api_s)
        auth.set_access_token(access_t, access_s)
        print("*************")
        api = tweepy.API(auth)
    except:
        return None
    if auth is not None:
        image_path = "./image/1.jpg"

        tweet_text = "DEVOPS"

        video_path = 'chemin ver video'

        if video_path:
           
            media = api.media_uplod(video_path)

            while media_video.processing_info['state'] == 'pending':
                pass
            tweet = api.update_status(status=tweet_text, media_ids=[media.media_id])
        else:
          
            media_image = api.media_upload_image(image_path)
            tweet = api.update_status(status_tweet_text, media_ids=[media_image.media_id])

send = SendMessage(api_key,api_secret, access_token, access_secret)

print(send)
