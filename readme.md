aller dans le dossier depuis une invite de commande puis utiliser ces commandes pour lancer le projet:
- (sudo) docker build . -t flaskbook:1
- (sudo) docker run -p 5000:5000 (-v $(pwd):/usr/src/app) flaskbook:1

- se connecter en copiant collant l'adresse IP afficher sur un navigateur web et ajouter /api/search/id/1933988673 pour voir le premier livre contenu dans le json.


- pour trouver un livre grace a son id taper /api/search/id/<id du livre> apres l'adresse IP.
- pour trouver un livre grace a son titre taper /api/search/title/<titre du livre> apres l'adresse IP.
