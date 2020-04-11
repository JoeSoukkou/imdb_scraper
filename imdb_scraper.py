#Python web scraping vidal

from requests import get
from bs4 import BeautifulSoup







def search(movies): 
	plage_ = []
	url = "https://www.imdb.com/search/title/?title="+movies+""
	response = get(url)
	textR = response.text
	our_soup = BeautifulSoup(textR, 'html.parser')
	mv_div_containers = our_soup.find_all('div', class_= 'lister-item mode-advanced') 
	if (len(mv_div_containers) == 0) : 
		print("No Movies were found with the title" + str(movies[0]))
	else :
		plage_.append(mv_div_containers[0])
		title = str(plage_[0].h3.a.text)
		time = str(plage_[0].h3.find_all('span')[1].text)
		rating = str(plage_[0].strong.text)
		duration = str(plage_[0].find_all('span',class_='runtime')[0].text)
		dr_hours = (int(duration[:-4])) / 60
		category = str(plage_[0].find_all('span',class_='genre')[0].text)
		votes = str(plage_[0].find_all('p',class_='sort-num_votes-visible')[0].select('span[name="nv"]')[0].text)
		desc = str(plage_[0].find_all('p',class_='text-muted')[1].text)
		out = " Title : "  + title +" " + time + " \n Genre :  "+ category[1:]+ " \n Rating ("+ rating +"/10) \n Duration "+ duration+" ("+str(format(dr_hours, '2.2g'))+ " Hours) \n Votes : " + votes + " \n Plot : " + desc
		print(out)
		
		answer = str(input("\n Wanna save this ? (y/n) => "))
		if (answer and answer == "y") :
			file = open(title+".txt", "w")
			file.write(out)
			file.close()
			print("Saved[+]! \n")
			start()
		elif (answer == "n")  :
			print("Okay! \n")
			start()
		else :
			start()
			

def start():
		
	input_mv  = input("What movie/series/tv-show you're looking for ? \n ")
	if (len(input_mv) >= 2 ) :
		movies = str(input_mv)
		search(movies)
	else : 
		print("Please enter a valid movie name")
start()


