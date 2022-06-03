from multipage import MultiPage
from pages import Analytics_page,Main_page,Info_page,Generate_known_data

app=MultiPage()






app.add_page("Live",Main_page.app)
app.add_page("Analytics",Analytics_page.app)
app.add_page("Individual",Info_page.app)
app.add_page("Generate Known-data",Info_page.app)

app.run()