#import numpy as np
#import pandas as pd
import ssl

from urllib.request import urlopen
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

# recupére le code html d'une page web
def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# récupére les liens des pages wiki de la démographie de chaque pays du monde dans le tableau de la page wiki "List_of_countries_and_dependencies_by_population"
def extract_Countries_links_list_from_Main_page():
    Countries_links_list=[]
    content = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    table = content.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')
    # List of all links
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            if cells[1].find('a'):
                country_link = cells[1].find('a')
                Countries_links_list.append (country_link.get('href'))
    return Countries_links_list

# Tronque la liste des liens de la démographie des pays du monde pour garder les n premiers
def Links_N_Pays_les_peuples(n):
    Countries_link_page_list=[]
    Links_pays_plus_peuples=[]
    Countries_link_page_list = extract_Countries_links_list_from_Main_page()
    cpt=0
    for pays_link in Countries_link_page_list:
        if cpt <n:
            Links_pays_plus_peuples.append(pays_link)
        cpt=cpt+1
    return Links_pays_plus_peuples


# Extrait le tableau d'évolution de la démographie des pays.
def Extract_Tableau_Population_Evolution_Of_Country(url,pays):

    table_list=[]
    content = getHTMLContent(url)

    if ((pays == India) or (pays == China) or (pays==Bangladesh) or (pays==Ethiopia) or (pays==Congo) or (pays==Iran)):
        table = content.find('table', {'class': 'wikitable'})
        table_list=extract_data_table(table)

    elif (pays == USA):

        tables = content.find_all('table', {'class': 'wikitable'})
        table=tables[5]
        table_list=extract_data_table(table)

    elif (pays == Philippines):

        tables = content.find_all('table', {'class': 'wikitable'})
        table=tables[6]
        table_list=extract_data_table(table)

    elif ((pays == Indonesia) or (pays == Brazil) or (pays== Nigeria) or
          (pays == Russia) or (pays == Mexico) or (pays == Japan) or
          (pays == Egypt) or (pays == Vietnam) or (pays == Germany) or (pays == Turkey)):

        table = content.find('table', {'class': 'toccolours'})
        table_list=extract_data_table(table)
    elif (pays== Pakistan):
        table = content.find('table',{'sortable wikitable'})
        table_list=extract_data_table(table)
    else:
        print("other country")
    return table_list


# Extrait table des données.
def extract_data_table(table):
    table_list=[]
    row_list=[]
    rows = table.find_all('tr')
    for row in rows:
        cells_th= row.find_all('th')
        cells = row.find_all('td')
        if len(cells_th) > 0:
            for cell_th in cells_th:
                row_list.append(cell_th.get_text().strip('\n'))
            table_list.append(row_list)
        row_list=[]
        if len(cells) > 0:
            for cell in cells:
                row_list.append(cell.get_text().strip('\n'))
            table_list.append(row_list)
        row_list=[]
    return table_list



China=0
India=1
USA=2
Indonesia=3
Brazil=4
Pakistan=5
Nigeria=6
Bangladesh=7
Russia=8
Mexico=9
Japan=10
Philippines=11
Egypt=12
Ethiopia=13
Vietnam=14
Congo=15
Germany=16
Iran=17
Turkey=18

def Main():


    wiki_url='https://en.wikipedia.org'
    N=20
    Links_Vingt_pays_les_plus_peuples = []
    Links_Vingt_pays_les_plus_peuples = Links_N_Pays_les_peuples(N)
    Url_China_page = wiki_url+Links_Vingt_pays_les_plus_peuples[China]
    Url_India_page = wiki_url+Links_Vingt_pays_les_plus_peuples[India]
    Url_USA_page = wiki_url+Links_Vingt_pays_les_plus_peuples[USA]
    Url_Indonesia_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Indonesia]
    Url_Brazil_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Brazil]
    Url_Pakistan_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Pakistan]
    Url_Nigeria_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Nigeria]
    Url_Bangladesh_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Bangladesh]
    Url_Russia_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Russia]
    Url_Mexico_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Mexico]
    Url_Japan_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Japan]
    Url_Philippines_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Philippines]
    Url_Egypt_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Egypt]
    Url_Ethiopia_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Ethiopia]
    Url_Vietnam_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Vietnam]
    Url_Congo_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Congo]
    Url_Germany_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Germany]
    Url_Iran_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Iran]
    Url_Turkey_page = wiki_url+Links_Vingt_pays_les_plus_peuples[Turkey]
    #Table_China=Extract_Tableau_Population_Evolution_Of_Country(Url_China_page,China)
    #Table_India=Extract_Tableau_Population_Evolution_Of_Country(Url_India_page,India)
    #Table_USA=Extract_Tableau_Population_Evolution_Of_Country(Url_USA_page,USA)
    #Table_Indonesia=Extract_Tableau_Population_Evolution_Of_Country(Url_Indonesia_page,Indonesia)
    #Table_Brazil=Extract_Tableau_Population_Evolution_Of_Country(Url_Brazil_page,Brazil)
    #Table_Pakistan=Extract_Tableau_Population_Evolution_Of_Country(Url_Pakistan_page,Pakistan)
    #Table_Nigeria=Extract_Tableau_Population_Evolution_Of_Country(Url_Nigeria_page,Nigeria)
    #Table_Bangladesh=Extract_Tableau_Population_Evolution_Of_Country(Url_Bangladesh_page,Bangladesh)
    #Table_Russia=Extract_Tableau_Population_Evolution_Of_Country(Url_Russia_page,Russia)
    #Table_Mexico=Extract_Tableau_Population_Evolution_Of_Country(Url_Mexico_page,Mexico)
    #Table_Japan=Extract_Tableau_Population_Evolution_Of_Country(Url_Japan_page,Japan)
    #Table_Egypt = Extract_Tableau_Population_Evolution_Of_Country(Url_Egypt_page,Egypt)
    #Table_Vietnam = Extract_Tableau_Population_Evolution_Of_Country(Url_Vietnam_page,Vietnam)
    #Table_Congo = Extract_Tableau_Population_Evolution_Of_Country(Url_Congo_page,Congo)
    #Table_Germany = Extract_Tableau_Population_Evolution_Of_Country(Url_Germany_page,Germany)
    #Table_Iran = Extract_Tableau_Population_Evolution_Of_Country(Url_Iran_page,Iran)
    Table_Turkey = Extract_Tableau_Population_Evolution_Of_Country(Url_Turkey_page,Turkey)
    #print(Table_China)
    #print(Table_India)
    #print(Table_USA)
    #print(Table_Indonesia)
    #print(Table_Brazil)
    #print(Table_Pakistan)
    #print(Table_Nigeria)
    #print(Table_Bangladesh)
    #print(Table_Russia)
    #print(Table_Japan)
    #print(Table_Philippines)
    #print(Table_Egypt)
    #print(Table_Ethiopia)
    #print(Table_Vietnam)
    #print(Table_Congo)
    #print(Table_Germany)
    #print(Table_Iran)
    print(Table_Turkey)
    print("modifications")





Main()
