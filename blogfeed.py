import feedparser
uri = "https://developer-r.tistory.com/rss"
feed = feedparser.parse(uri)

markdown_text = """
#### Hi there 👋
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frhjdev&count_bg=%23555555&title_bg=%231F354A&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Blog Badge](https://img.shields.io/badge/Reminder-1f354a?logo=Tistory&logoColor=white&link=https://developer-r.tistory.com)](https://developer-r.tistory.com)

[![rhjdev's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=rhjdev&theme=github&bg_color=939195&line=728192&point=fe8071&area=true&radius=20)](https://github.com/rhjdev/github-readme-activity-graph)
[![rhjdev's GitHub stats](https://github-readme-stats.vercel.app/api?username=rhjdev&count_private=true&custom_title=rhjdev's&nbsp;Github&nbsp;Stats👀&hide_rank=false&rank_icon=github&bg_color=30,939195,1f354a&title_color=fff&text_color=fff&border_radius=10)](https://github.com/rhjdev)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=rhjdev&count_private=true&bg_color=30,1f354a,939195&title_color=fff&text_color=fff&border_radius=10&layout=compact)
[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=rhjdev)](https://solved.ac/rhjdev)

#### 📚Latest Blog Posts
"""
for i in feed['entries'][:5]:
    markdown_text += f"[{i['title']}]({i['link']}) <br>"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
