import requests 
import pandas as pd
#cria uma chamada de api e verifica a resposta
url = "https://api.github.com/search/repositories"
url += "?q=sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

#converte o objeto de resposta em um dicionário
response_dict = r.json()
print(f"total de repositorios: {response_dict['total_count']}")
print(f"resultados completos: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f'repositorios retornados: {len(repo_dicts)}')

"""#examina o primeiro repositorio
repo_dict = repo_dicts[0]
print(f"\n chaves: {len(repo_dict)}")
for chave in sorted(repo_dict.keys()):
    print(chave)
#processa os resultados
print(response_dict.keys())"""
lista = []
for repo_dict in repo_dicts:
    if repo_dict['language']  == 'JavaScript':
        print("\nSelected information about first repository:")
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")
        print(f"Language: {repo_dict['language']}")

    repos_js = {
        'Nome': repo_dict['name'],
        'Descrição': repo_dict['description'],
        'Linguagem': repo_dict['language']
    }


    lista.append(repos_js) 
    
df = pd.DataFrame(lista)
print(df)   