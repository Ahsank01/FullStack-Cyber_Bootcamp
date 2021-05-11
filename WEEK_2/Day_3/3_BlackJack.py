
import sys
import requests


def print_flag(response):
    # Change the response into a dictionary 
    resp_json = response.json()
    print(resp_json['flag'])


#   Brute force method: Deal new games until we've one three times
def brute_force(url):
    with requests.Session() as sess:
        # Create a session to play the game
        resp = sess.get(url)

        # Create the URL that will be used to post data
        post_url = url + '/bj.php'

        # Dictionary representing the data we are sending to the URL
        action = { 'do_what': 'deal' }

        # Keep hitting deal the cards until the flag has appeared
        while resp.text.find('RCN{') == -1:
            resp = sess.post(post_url, data=action)

        print_flag(resp)

def main():
  url = sys.argv[1]

  # Both of the below functions will retrieve the flag
  brute_force(url)
main()