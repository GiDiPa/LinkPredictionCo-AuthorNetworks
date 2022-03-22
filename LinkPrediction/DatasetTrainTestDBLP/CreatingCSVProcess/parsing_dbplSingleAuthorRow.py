import xml.sax
import csv
import re

class DBLPHandler(xml.sax.ContentHandler):
    def __init__(self): #qui vengono istanziate tutte le variabili
        self.CurrentData = ''
        self.author = ''
        self.journal = ''
        self.parent = ''
        self.child = False

#su startElement gli elementi vengono gestiti in base alla corrispondeza del tag. Se si hanno alcuni tag nelle successive funzioni si andranno ad effettuare le operazioni di cui necessitiamo
#tutti i nodi definiti qua, sono di primo livello come scritto dall'autore stesso in una sua pubblicazione.
    def startElement(self,tag,attributes):
        self.CurrentData=tag
        global articles
        global inproceedings
        global authorsList
        global journ
        if tag == 'article':
            if (articles < 1): 
                self.child = True
                self.parent = tag
                articles = articles + 1
            else:
                if authorsList:
                    for auth in authorsList:
                        writer.writerow([articles, journ, auth])
                self.child = True
                self.parent = tag
                articles = articles + 1
                authorsList = []
        elif tag == 'inproceedings':
            self.child = False
            #self.child = True
            #self.parent = tag
            #inproceedings = inproceedings + 1
        elif tag == 'proceedings':
            self.child = False
        elif tag == 'book':
            self.child = False
        elif tag == 'incollection':
            self.child = False
        elif tag == 'phdthesis':
            self.child = False
        elif tag == 'mastersthesis':
            self.child = False
        elif tag == 'www':
            self.child = False

    
    def endElement(self,tag):
        global authInArticles
        global authInInproceedings
        global journ
        if self.child == True:
            if self.CurrentData=='author' and self.author != '':
                authorsList.append(self.author)
                #if self.author not in authors and re.match("[[\w[0-9]+\s[\w[0-9]+]*", self.author):
                if self.author not in authors and ' ' in self.author:
                    authors.add(self.author)
                    if self.parent == 'article':
                        authInArticles = authInArticles + 1
                    #else:
                    #    authInInproceedings = authInInproceedings + 1
                self.author = ''
            elif self.CurrentData=='journal':
                if self.journal not in journals:
                    journals.add(self.journal)
                journ = self.journal
                self.journal = ''
            self.CurrentData=''

    def characters(self,content):
        if self.child == True:
            if self.CurrentData=='author':
                for c in content:  
                    self.author = self.author + c
                self.author.strip()
            elif self.CurrentData=='journal':
                for c in content:
                    self.journal = self.journal + c

    

if __name__=='__main__':
    authInArticles = 0
    #authInInproceedings = 0
    articles = 0
    inproceedings = 0
    authorsList = []
    journ = ''
    authors = set() #thanks for the tip
    journals = set()
    #with open('co-authorNetwork.csv', 'w', newline='') as file:
    with open('OutputData/co-authorNetworkSingleAuthorRow.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Id Article", "Journal", "Authors"])
        parser=xml.sax.make_parser() #creating an XMLReader
        parser.setFeature(xml.sax.handler.feature_namespaces, 0) #non serve lavorare con gli XML Namespace al momento
        parser.setFeature(xml.sax.handler.feature_external_ges, True) #comando che permette di far gestire i file esterni, ad esempio il DTD associato
        Handler=DBLPHandler()
        parser.setContentHandler(Handler) #ContentHandler impostato per la nostra classe DBLPHandler()
        parser.parse('../dblp/dblp.xml')
        #parser.parse('../dblp/dblp_test.xml') #file xml per prove tecniche più snelle
        #scrittura a video dei risultati richiesti!
        for auth in authorsList:
            writer.writerow([articles, journ, auth]) #ultima riga da scrivere fuori dal parser

    print ("The number of articles is:", articles)
    print ("The number of inproceedings is:", inproceedings)
    print ("The number of different Authors is", len(authors))
    print ("The number of different Journal is", len(journals))
    print ("The number of different Authors in Articles is", authInArticles)
    #print ("The number of different Authors in Inproceedings is:", authInInproceedings) 
