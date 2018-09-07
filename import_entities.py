import csv

birthday = [
	"occasions",
	"birthday",
	"bd-day"
	"bday",
	"b'day",
	"bdday",
]

anniversery = [
	"occasions",
	"anniversery",
	"wedding anniversery",
	"anniversery",
	"marriage anniversery",
	"first anniversery",
]

father = [
	"relationships",
	"father",
	"papa",
	"daddy",
	"dad",
	"pops",
]

mother = [
	"relationships",
	"mother",
	"mummy",
	"mommy",
	"mom",
	"moms",
]

girlfriend = [
	"relationships",
	"girlfriend",
	"gf",
	"girl",
	"fiance",
	"girl friend",
]

boyfriend = [
	"relationships",
	"boyfriend",
	"bf",
	"boy",
	"boy friend",
]

aunt = [
	"relationships",
	"aunt",
	"aunty",
	"relative"
]

uncle = [
	"relationships",
	"uncle",
	"uncl",
	"relative"
]

funeral = [
	"occasion",
	"funeral",
	"funrl",
	"funeral function",
	"fnrl"
]

valentines = [
	"occasions",
	"valentine's day",
	"valentines",
	"valentines day",
	"valntn"
	"valntn day"
]

entities = [valentines, funeral, birthday, anniversery, father, mother, girlfriend, boyfriend, aunt, uncle]

with open('flower_shop_entities.csv', 'w', newline='') as csvfile:
	reader = csv.reader(csvfile)
	writer = csv.writer(csvfile)

	count = 0
	for entity in entities:
		writer.writerow(entity)
