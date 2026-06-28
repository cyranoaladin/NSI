# -*- coding: utf-8 -*-
"""
Script de Scraping Clé en Main pour Ressources NSI
Auteur: Dossier Technique NSI
Description: Ce script lit une liste d'URLs cibles à partir d'un fichier CSV,
             analyse les pages HTML pour extraire les liens vers les ressources
             pédagogiques (.pdf, .ipynb, .py, .zip) et télécharge automatiquement
             les fichiers en respectant l'arborescence.
"""

import os
import csv
import sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Configuration des extensions cibles
EXTENSIONS_CIBLES = ('.pdf', '.ipynb', '.py', '.zip', '.docx', '.xlsx')

# Headers pour simuler un navigateur réel et éviter les blocages
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_filename(filename):
    """Nettoie le nom de fichier pour éviter les erreurs système."""
    keepcharacters = ('.', '_', '-', ' ')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()

def download_file(url, folder_destination):
    """Télécharge un fichier distant et le sauvegarde localement."""
    try:
        os.makedirs(folder_destination, exist_ok=True)
        parsed_url = urlparse(url)
        base_name = os.path.basename(parsed_url.path)
        if not base_name:
            return False
        
        filename = clean_filename(base_name)
        file_path = os.path.join(folder_destination, filename)
        
        # Éviter de retélécharger si le fichier existe déjà
        if os.path.exists(file_path):
            print(f"  [Sauté] Déjà présent : {filename}")
            return True
        
        print(f"  [Téléchargement] {url} -> {filename}")
        response = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
        else:
            print(f"  [Erreur] Statut {response.status_code} pour {url}")
            return False
    except Exception as e:
        print(f"  [Exception] Échec du téléchargement pour {url} : {e}")
        return False

def scrape_site(site_name, base_url, type_structure):
    """Scrape une URL racine pour extraire et télécharger les fichiers cibles."""
    print(f"\n=== Analyse de : {site_name} ({base_url}) ===")
    try:
        response = requests.get(base_url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            print(f"[Erreur] Impossible d'accéder au site. Statut : {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        print(f"  {len(links)} liens trouvés sur la page principale. Filtrage en cours...")
        
        # Création du dossier spécifique pour ce site
        site_folder = os.path.join("ressources_nsi_extraites", clean_filename(site_name))
        
        compteur = 0
        for link in links:
            href = link.get('href')
            if not href:
                continue
            
            # Reconstruction de l'URL absolue
            absolute_url = urljoin(base_url, href)
            parsed_absolute = urlparse(absolute_url)
            
            # Vérification de l'extension
            if parsed_absolute.path.lower().endswith(EXTENSIONS_CIBLES):
                # Détermination du sous-dossier selon l'extension
                ext = parsed_absolute.path.split('.')[-1].lower()
                subfolder = os.path.join(site_folder, ext)
                
                success = download_file(absolute_url, subfolder)
                if success:
                    compteur += 1
                
                # Politesse réseau : petite pause entre deux téléchargements
                time.sleep(0.5)
                
        print(f"=== Fin de l'analyse. Fichiers téléchargés avec succès : {compteur} ===")
        
    except Exception as e:
        print(f"[Exception Globale] Erreur lors du scraping de {site_name} : {e}")

def main():
    csv_file = "urls_a_scraper.csv"
    if not os.path.exists(csv_file):
        print(f"Erreur : Le fichier de configuration '{csv_file}' est introuvable.")
        sys.exit(1)
        
    print("====================================================================")
    print("DÉMARRAGE DU SCRAPER NSI - AUTOMATISATION DES RESSOURCES PEDAGOGIQUES")
    print("====================================================================")
    
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # Passer l'en-tête
        
        for row in reader:
            if len(row) < 3:
                continue
            site_name, url, type_structure = row[0], row[1], row[2]
            scrape_site(site_name, url, type_structure)
            
    print("\n====================================================================")
    print("PROCESSUS TERMINÉ. Toutes les ressources ont été répertoriées.")
    print("Consultez le dossier 'ressources_nsi_extraites/'")
    print("====================================================================")

if __name__ == "__main__":
    main()
