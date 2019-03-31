from request import Request
from parser import Parser
import json

request = Request()
parser = Parser()

parsed_data = []

subreddits = [
	"r/politics", "r/conservative", "r/liberal", "r/worldpolitics"
]



for subreddit in subreddits:

	top_article_response = request.get(endpoint='{}/top'.format(subreddit))
    article_ids = parser.parse_articles(top_article_response)

	for article_id in top_article_ids:
		comment_json
	    comment_response = request.get(
	    	endpoint='r/politics/comments/{}/_'.format(article_id)
	    )
	    
	    comment_body_list = parser.parse_comments(comment_response)

	    comment_dict = {
			"subreddit": "r/politics"
			"article_id": article_id,
			"comments": comment_body_list
		}