import yaylib
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()
# 環境変数を取得
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

async def search_users(gender, nickname, title, biography, from_timestamp,
                        similar_age, not_recent_gomimushi, recently_created,
                        same_prefecture,save_recent_search,number):
    """

    ユーザーを検索します

    Parameters
    ----------
        - gender: int = None 0:男性 1:女性
        - nickname: str = None
        - title: str = None
        - biography: str = None
        - from_timestamp: int = None
        - similar_age: bool = None
        - not_recent_gomimushi: bool = None
        - recently_created: bool = None
        - same_prefecture: bool = None
        - save_recent_search: bool = None

    """
    # from_timestamp= int(datetime.strptime(from_timestamp, "%Y-%m-%d").timestamp()) if from_timestamp else from_timestamp

    bot = yaylib.Client()
    result = bot.search_users(
        gender=1,
        nickname=nickname,
        biography=biography,
        from_timestamp=  int(datetime.strptime(from_timestamp, "%Y-%m-%d").timestamp())
        if from_timestamp else None,
        # similar_age ='true',
        # same_prefecture ='true',
        # recently_created ='true',
        number=number)
    users = [
        {
            'id': user['id'],
            'url': f"https://yay.space/user/{user['id']}",
            'nickname': user['nickname'], 
            'biography': user['biography'], 
            'followers_count': user['followers_count'], 
            'posts_count': user['posts_count'], 
            'profile_icon_thumbnail': user['profile_icon_thumbnail'], 
            'cover_image_thumbnail': user['cover_image_thumbnail'], 
            'last_loggedin_at': datetime.fromtimestamp(user['last_loggedin_at']).strftime('%Y/%m/%d %H:%M:%S'),
            # 'is_private': user['is_private'], 
            # 'title': user['title'], 
            # 'groups_users_count': user['groups_users_count'], 
            'reviews_count': user['reviews_count'], 
            'age_verified': user['age_verified'], 
            # 'country_code': user['country_code'], 
            # 'vip': user['vip'], 
            # 'hide_vip': user['hide_vip'], 
            'online_status': user['online_status'], 
            # 'profile_icon': user['profile_icon'], 
            # 'cover_image': user['cover_image'],  
            # 'recently_kenta': user['recently_kenta'], 
            # 'dangerous_user': user['dangerous_user'], 
            'new_user': user['new_user'], 
            # 'interests_selected': user['interests_selected'], 
        }
        for i, user in enumerate(result.data['users'])
    ]

    return users

async def follow(user_id):
    """

    ユーザーをフォローします

    Parameters
    ----------
        - user_id: str = None

    """
    bot = yaylib.Client()
    bot.login(email=email,password=password)
    bot.follow_user(user_id=user_id)

async def follow_users(users):
    """

    ユーザーをフォローします

    Parameters
    ----------
        - user_id: str = None

    """
    bot = yaylib.Client()
    bot.login(email=email,password=password)
    bot.follow_users(user_ids=users)
