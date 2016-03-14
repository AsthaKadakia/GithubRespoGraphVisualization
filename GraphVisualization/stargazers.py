import json
import requests
import sys
from github import Github
ACCESS_TOKEN = 'f924776365da664034f8b0ad26abbf4131b4e543'
# An unauthenticated request that doesn't contain an ?access_token=xxx query string
url = "https://api.github.com/repos/ptwobrussell/Mining-the-Social-Web/stargazers"
response = requests.get(url)
# Display one stargazer
print json.dumps(response.json()[0], indent=1)
print
# Display headers
for (k,v) in response.headers.items():
    print k, "=>", v


USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'
client = Github(ACCESS_TOKEN, per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)
# Get a list of people who have bookmarked the repo.
# Since you'll get a lazy iterator back, you have to traverse
# it if you want to get the total number of stargazers.
stargazers = [ s for s in repo.get_stargazers() ]
print "Number of stargazers", len(stargazers)



for i, sg in enumerate(stargazers):
# Add "follows" edges between stargazers in the graph if any relationships exist
    try:
        for follower in sg.get_followers():
            if follower.login + '(user)' in g:
                g.add_edge(follower.login + '(user)', sg.login + '(user)', type='follows')
    except Exception, e: #ssl.SSLError
        print >> sys.stderr, "Encountered an error fetching followers for", \
              sg.login, "Skipping."
        print >> sys.stderr, e

    print "Processed", i+1, " stargazers. Num nodes/edges in graph", \
          g.number_of_nodes(), "/", g.number_of_edges()

    print "Rate limit remaining", client.rate_limiting


