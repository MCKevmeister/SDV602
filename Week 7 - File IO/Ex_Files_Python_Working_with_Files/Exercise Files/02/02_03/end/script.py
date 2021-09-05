import json

def display_json():
	with open('monster.json') as f:
		content_json = json.load(f)
		print(content_json)

def display_name_from_json():
	with open('monster.json') as f:
		content_json = json.load(f)
		print("Welcome", content_json['monsterName'])

if __name__ == "__main__":
	# display_json()
	display_name_from_json()