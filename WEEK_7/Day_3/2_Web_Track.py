#!/usr/bin/env python3

# import sys library to use command line input
import sys

# import requests library to use a get request
import requests

# save the URL in this variable
URL = sys.argv[1]

# add the extension to the url above
extension = 'product/'

# product number to navigate to different pages
product_num = 1

# boolean for a while loop
flag_not_found = True

# keep looping until the flag is not found
while flag_not_found:

  # append the URL to an extension and add a product number at the end
  new_url = URL + extension + str(product_num)

  # make a get request on the new url
  response = requests.get(new_url)
  
  # save the response as a text
  response = response.text

  # check if the 'RCN' is on the page
  if 'RCN' in response:

    # if yes, change the boolean to false
    flag_not_found = False
    #print(response)
  else:
    
    # otherwise add 1 to the product number
    product_num += 1

# fine the index of R
find_R = response.find('R')

# find the index of }
find_ending_curly_bracket = response.find('}')

# use list slicing to get the flag
print(response[find_R:find_ending_curly_bracket + 1])