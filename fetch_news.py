from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_5792240c0c63be345810def276d2c4add312f")

# You can paginate till last page by providing "page" parameter

page=None

with open('titles.txt', 'w', encoding='utf-8') as file:
    while True:
        response = api.latest_api(page = page, country="kr")

        if response['status'] == 'success':
            # Extract titles
            titles = [article['title'] for article in response['results']]

            # Write the titles to the file in real-time
            for title in titles:
                file.write(title + '\n')
        else:
            print(response['message'])
            break
        page = response.get('nextPage',None)

        if not page:
            break