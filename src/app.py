import os
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv,find_dotenv

# load the .env file variables
load_dotenv(".env", override=True)

# CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
#el client ID y secret lo tuve que agregar asi porque por alguna razon me arrojaba error. Parece no estar leyendo el .env y lo revise con Fran pero no encontramos la solucion
CLIENT_ID = "49d2102c1b2b4446b7d19b8ee510d6bc"
CLIENT_SECRET = '2dbfa00683184b14a94fb3939060e2b3'

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#realizar solicitudes Api

conociendo_rusia_uri = '79R7PUc6T6j09G8mJzNml2'

results = spotify.artist_top_tracks(conociendo_rusia_uri)

def infoartista():
    for track in results['tracks'][:10]:
        print('cancion: ' +track['name'])
        print('popularidad: ' +str(track['popularity']))
        print('duracion: ' +(str(round(track['duration_ms']/60000,1)) + ' minutos'))
        print('--------------------------------------------------------')

infoartista()

#diccionario 

def x():
    data = []
    for track in results['tracks'][:10]:
        data.append({'cancion ': track['name'],'popularidad: ': str(track['popularity']), 'duracion: ': (str(round(track['duration_ms']/60000,1))) })
    return data 

print(x())

#transformar a dataframe 
df = pd.DataFrame.from_dict(x())
print(df)

#df ordenado por popularidad creciente 

ascend_pop = df.sort_values(by='popularidad: ',ascending= False)

print(ascend_pop)

#top 3 resultante despues del sort por  popularidad 

top3 = df.head(3)

print(top3)

#scatter graph correlacion entre duracion y popularidad 
x = df['duracion: ']
y = df['popularidad: ']

plt.scatter(x,y)
plt.title('Correlación entre duración y popularidad')
plt.xlabel('Duración')
plt.ylabel('Popularidad')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.show()

#la correlacion entre el tiempo de duracion y la popularidad es positiva. Es decir, mientras mas dura la cancion, mas popular es. Sin embargo, hay tramos en los que la relacion es constante.

