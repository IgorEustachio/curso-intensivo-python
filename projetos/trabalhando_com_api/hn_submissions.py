from operator import itemgetter
import requests

#cria uma chamada de API e verifica a resposta
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status code: {r.status_code}")

#processa as informações sobre cada contribuição de artigo
submission_ids = r.json()
submission_dicts = []

print(submission_ids)

for submission_id in submission_ids[:5]:
    #cria uma nova chamada de API para cada contribuição no artigo
    url = f"https://hacker-news.firebaseio.com/v0/item/%7Bsubmission_id%7D.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #cria um dicio para cada artigo  
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
    
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")