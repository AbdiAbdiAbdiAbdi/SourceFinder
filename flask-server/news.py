import groq
import json
import urllib.request
from AI_portion import AISum
from dotenv import load_dotenv
import os





def News_Getter(user_search):
    load_dotenv()
    newsAPIKey = os.getenv('newsAPIKey')
    user_search = user_search.replace(" ", "")
    user_search = user_search.lower()
    NewsURL = f"https://gnews.io/api/v4/search?q={user_search}&lang=en&country=us&max=10&apikey={newsAPIKey}"

    with urllib.request.urlopen(NewsURL) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
        article_list = []

        for i in range(len(articles)):
            article_list.append([articles[i]['title'], AISum(articles[i]['url']), articles[i]['url']])
    
    return article_list


if __name__ == "__main__":
    print(News_Getter('investmentbanks'))