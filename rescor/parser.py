
class Parser:
	def parse_articles(article_response):

		article_ids = []
		for article in top_article_response['data']['children']:
		    article_ids.append(article['data']['id'])

		return article_ids

	def parse_comments(comment_response):

		for comment in comment_response[1]['data']['children']:

    		print(comment['data']['body'])