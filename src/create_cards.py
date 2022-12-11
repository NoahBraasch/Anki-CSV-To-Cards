import requests
import json
import time
import pyautogui
import keyboard
from threading import Thread

global terminate # Global flag for kill switching
terminate = False

def check_for_kill(): # Kill switch
	global terminate 
	while True:
		if keyboard.read_key() == 'k':
			terminate = True
			break

def main():
	string = '' # words from csv to be added to list
	word_list = [] # list of words from csv
	running_total = 1

	with open('../files/Netflix_95%_12K.csv', 'r', encoding='UTF-8') as csv_file: # Parses csv word list into dictionary
		csv_string = csv_file.read()
		for member in csv_string:
			if member != '\n':
				string += member
			else:
				word_list.append(string)
				string = ''

	index = 0
	for word in word_list:
		api = 'https://jisho.org/api/v1/search/words?keyword=' + word_list[index] # Reads words from lists, appends to API string and returns JSON dictionary
		try:
			response = requests.get(api)

		except:
			print("FAILED TO GET RESPONSE")
	# The API throws a 429 and forces us to sleep so we can start fetching more data
		try:
			json_dict = response.json()
		except:
			print('Probably got another 429')
			time.sleep(5)

		try:
			json_index_1= 0
			json_index_2= 0
			print(running_total, end=' ')
			print(json_dict['meta']['status'], end=' ')
			print(json_dict['data'][json_index_1]['slug'], end=' ')
			print(json_dict['data'][json_index_1]['japanese'][json_index_2]['reading'], end=' ')
			for definiton in json_dict:	
				try:
					for definiton in json_dict['data'][json_index_1]['senses'][json_index_2]['english_definitions']:
						if terminate == True:
							break
						print(json_dict['data'][json_index_1]['senses'][json_index_2]['english_definitions'][json_index_2], end=' ')
						print(json_dict['data'][json_index_1]['senses'][json_index_2]['parts_of_speech'][json_index_2], end=' ')
						json_index_2+=1
				except:
					json_index_2 = 0
					json_index_1 += 1
				if terminate:
					break
			print('ADDED', end='')
		except:
			json_index_1 = 0
		print()
		index+=1
		running_total += 1
		if terminate:
			break

kill_thread = Thread(target=check_for_kill) #Threading for kill switchiong
kill_thread.start()

main()