<!-- docker volume create --name=storage2
docker-compose up --build -->

# Afin de lancer notre projet 

Il vous faudra lancer les deux script d'initialisation présent dans le dossier fast_api/bdd/

En premier lieux lancer la scipt **init.sh** via la commande ./init.sh, cette commande lancera le docker-compose

Une fois le docker-compose lanceé, vous pourrez alors lancer le second script qui est celui d'initialisation de la bdd (cela consomme pas mal de ressources au niveau de l'ordinateur est prend du temps). Afin de le lancer exécuter la commande : ./init2.sh