
from apiscraper import APIScraper
from django.utils.text import slugify
import urlparse
import os

scraper = APIScraper()

def scrape_etapa(url, directory=""):
              data = scraper.scrape_url(url)
              try:
                     print "\t", data['etapa']
                     file = slugify(data['etapa']) + '.txt'
                     with open(os.path.join(directory, file), 'w') as f:                            
                                   f.write(data['etapa'].encode('utf-8'))
                                   tramos = data['tramos']
                                   tramo_titles = data['tramo-title']
                                   prev = 0
                                   for title in tramo_titles:
                                                 found = tramos.find(title)
                                                 f.write(data['tramos'][prev:found].encode('utf-8'))
                                                 f.write("\n\n")
                                                 prev = found
              except:              
                     pass

              next = data.get('next', None)
              return next
              
              
if __name__ == '__main__':
       caminos = [   ['camino-primitivo', 'http://caminodesantiago.consumer.es/etapa-de-oviedo-a-san-juan-de-villapanada'],
                     ['camino-frances', 'http://caminodesantiago.consumer.es/etapa-de-saint-jean-pied-de-port-a-roncesvalles'],
                     ['camino-aragones', 'http://caminodesantiago.consumer.es/etapa-de-somport-a-jaca'],
                     ['camino-vasco', 'http://caminodesantiago.consumer.es/etapa-de-irun-a-hernani'],
                     ['camino-norte', 'http://caminodesantiago.consumer.es/etapa-de-irun-a-donostia-san-sebastian'],
                     ['via-plata', 'http://caminodesantiago.consumer.es/etapa-de-sevilla-a-guillena'],
                     ['camino-sanabres', 'http://caminodesantiago.consumer.es/etapa-de-granja-de-moreruela-a-tabara'],
                     ['camino-portugues', 'http://caminodesantiago.consumer.es/etapa-de-tui-a-o-porrino'],
                     ['camino-catalan', 'http://caminodesantiago.consumer.es/etapa-de-montserrat-a-igualada'],
                     ['camino-baztanes', 'http://caminodesantiago.consumer.es/etapa-de-bayona-a-ustaritz'],
                     ['camino-ingles', 'http://caminodesantiago.consumer.es/etapa-de-ferrol-a-neda'],
                     ['fisterra-muxia', 'http://caminodesantiago.consumer.es/etapa-de-santiago-de-compostela-a-negreira']
                     ]

       print "Los Caminos a Santiago"
       ii = 0
       for camino in caminos:
              next = camino[1]
              directory = './%s' % camino[0]
              print "\n> %s" % camino[0]

              if not os.path.exists(directory):
                     os.makedirs(directory)

              i = 0
              try:
                     while next:
                                   next = urlparse.urljoin('http://caminodesantiago.consumer.es/', next)
                                   next = scrape_etapa(next, directory)
                                   i += 1
              except Exception as e:
                     print "\t error: %s" % str(e)
              print "< done ", i, " etapas"
              ii += i
       print "done ", ii, " etapas"
              