import wikipedia



def getWikipedia():
		result =  wikipedia.page('python')
		print(result.summary)



		for link in result.links:
			print(link)






#wikipedia information
getWikipedia()			
