from quart import Quart, render_template, request
import datetime
import search_users
import json

app = Quart(__name__, static_folder='./templates/images')

@app.route('/')
async def hello():
    return await render_template('first.html', title='search_yay')

# /scrapingをGETメソッドで受け取った時の処理
@app.route('/scraping', methods=['GET', 'POST'])
async def get():
    gender = request.args.get("channel-id", "")
    nickname = request.args.get("nickname", "")
    title = request.args.get("from", "")
    biography = request.args.get("biography", "")
    from_timestamp = request.args.get("from_timestamp", "")
    similar_age = int(request.args.get("subscribercount-level", "") or 0)
    not_recent_gomimushi = int(request.args.get("video-count", "") or 0)
    recently_created = request.args.get("comments", "")
    same_prefecture = request.args.get("comments", "")
    save_recent_search = request.args.get("comments", "")
    number = int(request.args.get("number", "") or 0)
    
    # 非同期関数を呼び出すためにawaitを使用
    sorce = await search_users.search_users(gender, nickname, title, biography, from_timestamp,
                        similar_age, not_recent_gomimushi, recently_created,
                        same_prefecture,save_recent_search,number)
    
    print(datetime.datetime.now())
    user_ids = [user['id'] for user in sorce]
    if sorce is None:
        return await render_template('first.html', title='search_youtube')

    if request.method == 'GET': # GETされたとき
        print('出力')
        return await render_template('template.html', sorce=sorce, user_ids=user_ids)
        
    elif request.method == 'POST': # POSTされたとき
        return 'POST'
    
@app.route('/follow_user', methods=['GET', 'POST'])
async def follow():
    user_id = request.args.get("user_id", "")
    
    # 非同期関数を呼び出すためにawaitを使用
    await search_users.follow(user_id)
    
    print(datetime.datetime.now())
    return "", 204  # 204 No Content ステータスを返す

@app.route('/follow_users', methods=['GET', 'POST'])
async def follow_users():
    user_ids = await request.json
    await search_users.follow_users(user_ids)
    return "", 204  # 204 No Content ステータスを返す

if __name__ == "__main__":
    app.run(debug=True)

