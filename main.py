from random import randint
from requests import get
from json import loads
from webbrowser import open
from sys import argv, exit
from os import listdir, system
from os.path import isfile, join

if len(argv) < 3:
	print("")
	print("usage: <imbDB api key> <providers> <true | false, has personnal_movie (should be in the same file as the program)> [log]")
	print("providers example: Disney_Plus-Amazon_Prime_Video ...")
	print("can be requested with: https://api.themoviedb.org/3/watch/providers/movie?language=fr-FR&watch_region=Fr&api_key=key")
	print("")
	# Disney_Plus-Amazon_Prime_Video-Sixplay-France_TV-Arte-TF1-Amazon_Video
	exit()

key = argv[1]
providers = argv[2].replace("_", " ").split("-") #https://api.themoviedb.org/3/watch/providers/movie?language=fr-FR&watch_region=Fr&api_key={key}
personnal_movie = (len(argv) >= 4 and argv[3] == "true")
log_option = (len(argv) == 5 and argv[4] == "log")

def log(value):
	if log_option == True:
		print(value)

def discover(page):
	return get(
		f"https://api.themoviedb.org/3/discover/movie?page={page}&language=fr&api_key={key}", 
		headers={"accept": "application/json"}
	)

def watch(id):
	return get(
		f"https://api.themoviedb.org/3/movie/{id}/watch/providers?api_key={key}",
		headers={"accept": "application/json"}
	)

def find_movie():
	datas = loads(discover(randint(1, 500)).text) # pages start at 1 and max at 500
	results = datas["results"]

	movie = results[randint(0, len(results)-1)]
	return (movie["id"], movie["title"])

def search():
	found = False
	while not found:
		log("")
		movie = find_movie()
		datas = loads(watch(movie[0]).text)
		result = datas["results"]
		log("searching for " + movie[1])

		if "FR" not in result:
			log("movie not found in france")
		else:
			if "flatrate" not in result["FR"]:
				log("movie not found")
			else:
				for provider in result["FR"]["flatrate"]:
					if provider["provider_name"] not in providers:
						log("movie not found with in your providers")
					else:
						found = True
						open(result["FR"]["link"])
					log(provider["provider_name"])

if (personnal_movie):
	if randint(1, 2) == 2:
		log("searching in your movies")
		files = [f for f in listdir("./") if (isfile(join("./", f)))]
		system(r'start ./\"' + files[randint(0, len(files)-1)] + '\" \"')
	else:
		search()
else:
	search()