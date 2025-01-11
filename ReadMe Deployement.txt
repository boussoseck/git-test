
#  lancer mon projet dans guithub a travers git
# Créez un compte sur GitHub :
# Si vous n'avez pas déjà un compte sur GitHub, créez-en un sur GitHub.
# Créez un nouveau référentiel (repository) sur GitHub :
# Connectez-vous à votre compte GitHub.
# Cliquez sur le signe "+" en haut à droite de la page et sélectionnez "New repository" (Nouveau référentiel).
# Donnez un nom à votre référentiel, ajoutez une description si vous le souhaitez, et cochez l'option pour initialiser le référentiel avec un fichier README si nécessaire.
# Cliquez sur "Create repository" (Créer le référentiel).
# Initialisez un référentiel Git local :
# Ouvrez un terminal (ou une invite de commandes) sur votre machine.
# Accédez au répertoire de votre projet en utilisant la commande cd chemin/vers/votre/projet.
# Exécutez les commandes suivantes pour initialiser un référentiel Git, ajouter tous les fichiers, faire un premier commit, et lier le référentiel local à votre référentiel GitHub :

git init
git add .
git commit -m "Premier commit"
git remote add origin https://github.com/votre-utilisateur/votre-repo.git
git branch -M main  
# ou git branch -M master si vous utilisez une ancienne version de Git

# Poussez vos fichiers sur GitHub :

git push -u origin main  # ou git push -u origin master si vous utilisez une ancienne version de Git

# Vérifiez sur GitHub :
# Rafraîchissez la page de votre référentiel GitHub sur votre navigateur. Vous devriez voir vos fichiers téléchargés.
# Travaillez sur votre projet :
# Continuez à travailler sur votre projet localement.
# Chaque fois que vous souhaitez enregistrer vos modifications sur GitHub, exécutez les commandes 

git add .
git commit -m "Description de vos modifications"
git push

#Pull (tirer) les modifications du référentiel distant (GitHub) :
#Si vous travaillez sur plusieurs machines ou avec d'autres collaborateurs, assurez-vous de tirer les modifications avant

git pull origin main  
# ou git pull origin master si vous utilisez une ancienne version de Git






#Vous pouvez créer un fichier requirements.txt à la racine de votre projet GitHub pour spécifier les dépendances nécessaires. Voici comment le contenu de votre fichier requirements.txt pourrait ressembler pour les bibliothèques que vous avez 
streamlit==1.25.0
numpy
pandas
matplotlib
plotly
scikit-learn
seaborn

#Assurez-vous d'ajouter ce fichier à la racine de votre projet sur GitHub. Vous pouvez le créer manuellement en utilisant un éditeur de texte, ou vous pouvez exécuter les commandes suivantes dans votre terminal ou invite de commandes à la racine de 

echo "streamlit==1.25.0" > requirements.txt
echo "numpy" >> requirements.txt
echo "pandas" >> requirements.txt
echo "matplotlib" >> requirements.txt
echo "plotly" >> requirements.txt
echo "scikit-learn" >> requirements.txt
echo "seaborn" >> requirements.txt

#Ces commandes créent le fichier requirements.txt et y ajoutent les dépendances nécessaires.
#Ensuite, ajoutez et engagez ces modifications dans votre dépôt GitHub :

git add requirements.txt
git commit -m "Ajouter le fichier requirements.txt avec les dépendances"
git push origin main

#Installez les dépendances localement :
#Ouvrez une fenêtre de terminal et accédez au répertoire de votre projet. Exécutez la commande suivante pour installer les dépendances :

pip install -r requirements.txt
Vérifiez l'installation :

#Vous pouvez vérifier que les dépendances sont correctement installées en exécutant les commandes suivantes dans le terminal :
#streamlit --version

python -c "import pandas; print(pandas.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import seaborn; print(seaborn.__version__)"
python -c "import plotly; print(plotly.__version__)"
python -c "import matplotlib; print(matplotlib.__version__)"

#Ajoutez et engagez les modifications dans Git :

git add requirements.txt
git commit -m "Ajout des dépendances dans requirements.txt"

#Poussez les changements vers GitHub :

git push origin main

#Déployez sur Streamlit Sharing :
#Si vous utilisez Streamlit Sharing, ajoutez un fichier Procfile à la racine de votre projet avec le contenu suivant :

web: streamlit run <nom_de_votre_script>.py


Remarque:" si vous ne parvener pas a lancer le projet essayer sa "
#Remplacez <nom_de_votre_script> par le nom de votre script principal Streamlit.
#Ensuite, poussez les changements vers GitHub :

git add Procfile
git commit -m "Ajout du fichier Procfile"
git push origin main

















