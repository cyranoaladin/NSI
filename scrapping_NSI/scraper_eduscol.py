# -*- coding: utf-8 -*-
"""
Script de Scraping Spécifique Éduscol NSI avec Extraction & Tri de ZIP
Auteur: Dossier Technique NSI
Description: Ce script extrait les ressources officielles NSI depuis Éduscol,
             télécharge les fichiers et gère l'extraction automatique
             ainsi que le tri intelligent des archives ZIP (sujets d'examens, codes).
"""

import os
import time
import zipfile
import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# URLs racines officielles de la spécialité NSI sur Eduscol STI
EDUSCOL_NSI_URLS = [
    "https://sti.eduscol.education.fr/formations/bac-voie-generale/specialite-nsi-numerique-et-sciences-informatiques",
    "https://sti.eduscol.education.fr/referentiels-par-competences-bac-scientifique/specialite-nsi-numerique-et-sciences-informatiques"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_name(name):
    """Nettoie une chaîne pour en faire un nom de fichier valide."""
    keepcharacters = ('.', '_', '-', ' ')
    cleaned = "".join(c for c in name if c.isalnum() or c in keepcharacters).strip()
    return cleaned if cleaned else "ressource_sans_nom"

def extract_and_sort_zip(zip_path, base_dest_dir):
    """Extrait une archive ZIP et trie son contenu de manière intelligente par extension."""
    temp_extraction_dir = os.path.join(base_dest_dir, "_temp_zip_extraction")
    os.makedirs(temp_extraction_dir, exist_ok=True)
    
    try:
        print(f"  [ZIP] Décompression de l'archive : {os.path.basename(zip_path)}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_extraction_dir)
            
        compteur_fichiers = 0
        # Parcours récursif des fichiers décompressés pour le tri
        for root, _, files in os.walk(temp_extraction_dir):
            for file in files:
                chemin_source = os.path.join(root, file)
                
                # Ignorer les fichiers cachés ou système système (ex: .DS_Store, __MACOSX)
                if file.startswith('.') or '__MACOSX' in chemin_source:
                    continue
                    
                ext = os.path.splitext(file)[1].lower().strip('.')
                if not ext:
                    ext = "sans_extension"
                
                # Catégorisation sémantique selon l'extension
                if ext in ['py', 'pyw']:
                    categorie = "01_Codes_Python"
                elif ext in ['pdf']:
                    categorie = "02_Sujets_et_Cours_PDF"
                elif ext in ['docx', 'doc', 'odt']:
                    categorie = "03_Documents_Texte"
                elif ext in ['png', 'jpg', 'jpeg', 'gif', 'svg']:
                    categorie = "04_Images_et_Graphiques"
                elif ext in ['html', 'css', 'js']:
                    categorie = "05_Ressources_Web"
                elif ext in ['csv', 'json', 'xml', 'txt']:
                    categorie = "06_Donnees_et_Configuration"
                else:
                    categorie = f"07_Autres_{ext.upper()}"
                
                dossier_cible = os.path.join(base_dest_dir, "Archives_Extraites_Triees", categorie)
                os.makedirs(dossier_cible, exist_ok=True)
                
                chemin_destination = os.path.join(dossier_cible, file)
                
                # Gestion des doublons de noms de fichiers lors du tri à plat
                if os.path.exists(chemin_destination):
                    nom_base, extension = os.path.splitext(file)
                    chemin_destination = os.path.join(dossier_cible, f"{nom_base}_doublon_{int(time.time())}{extension}")
                
                shutil.move(chemin_source, chemin_destination)
                compteur_fichiers += 1
                
        print(f"  [ZIP] Extraction réussie : {compteur_fichiers} fichiers triés et classés.")
        
    except zipfile.BadZipFile:
        print(f"  [Erreur ZIP] L'archive {os.path.basename(zip_path)} semble corrompue.")
    except Exception as e:
        print(f"  [Erreur ZIP] Échec lors du traitement de l'archive : {e}")
    finally:
        # Nettoyage rigoureux du dossier temporaire
        if os.path.exists(temp_extraction_dir):
            shutil.rmtree(temp_extraction_dir)

def scrape_eduscol_nsi():
    print("====================================================================")
    print("DÉMARRAGE DU SCRAPER ÉDUSCOL NSI - RESSOURCES INSTITUTIONNELLES")
    print("====================================================================")
    
    dossier_principal = os.path.join("ressources_nsi_extraites", "Eduscol_Officiel")
    dossier_zip_bruts = os.path.join(dossier_principal, "Archives_ZIP_Brutes")
    
    os.makedirs(dossier_principal, exist_ok=True)
    os.makedirs(dossier_zip_bruts, exist_ok=True)
    
    for page_url in EDUSCOL_NSI_URLS:
        print(f"\n[Analyse Page] Exploration de : {page_url}")
        try:
            response = requests.get(page_url, headers=HEADERS, timeout=20)
            if response.status_code != 200:
                print(f"  [Erreur] Impossible d'accéder à la page (Code : {response.status_code})")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            liens = soup.find_all('a')
            
            print(f"  {len(liens)} liens détectés. Recherche de documents officiels...")
            fichiers_telecharges = 0
            
            for lien in liens:
                href = lien.get('href')
                texte_lien = lien.text.strip()
                if not href:
                    continue
                
                # Cibler les extensions courantes OU les routes de téléchargement Drupal d'Éduscol
                href_lower = href.lower()
                is_file = href_lower.endswith(('.pdf', '.zip', '.docx', '.xlsx'))
                is_drupal_download = '/download' in href_lower or 'fichier' in href_lower or 'file' in href_lower
                
                if is_file or is_drupal_download:
                    url_absolue = urljoin(page_url, href)
                    
                    # Déterminer l'extension probable
                    parsed_path = urlparse(url_absolue).path.lower()
                    if '.zip' in parsed_path or '.zip' in href_lower:
                        ext = '.zip'
                    elif '.docx' in parsed_path or '.docx' in href_lower:
                        ext = '.docx'
                    elif '.xlsx' in parsed_path or '.xlsx' in href_lower:
                        ext = '.xlsx'
                    else:
                        ext = '.pdf' # Extension reine sur Éduscol pour les guides/sujets
                    
                    # Construire un nom propre et explicite basé sur le texte cliquable
                    nom_propre = clean_name(texte_lien) if texte_lien else clean_name(os.path.basename(parsed_path))
                    if not nom_propre or nom_propre == "download":
                        nom_propre = f"ressource_officielle_{int(time.time() * 1000) % 100000}"
                        
                    nom_fichier_final = f"{nom_propre[:60]}{ext}"
                    
                    # Choisir le dossier de destination en fonction du type
                    if ext == '.zip':
                        chemin_local = os.path.join(dossier_zip_bruts, nom_fichier_final)
                    else:
                        chemin_local = os.path.join(dossier_principal, nom_fichier_final)
                    
                    # Téléchargement si non existant
                    if os.path.exists(chemin_local):
                        # Si c'est un ZIP déjà présent mais pas encore décompressé, on s'assure qu'il soit traité
                        if ext == '.zip':
                            extract_and_sort_zip(chemin_local, dossier_principal)
                        continue
                        
                    print(f"  [Téléchargement] -> {nom_fichier_final}")
                    try:
                        res_file = requests.get(url_absolue, headers=HEADERS, timeout=25, stream=True)
                        if res_file.status_code == 200:
                            with open(chemin_local, 'wb') as f:
                                for chunk in res_file.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            
                            fichiers_telecharges += 1
                            
                            # Si c'est une archive ZIP, déclencher immédiatement l'extraction et le tri
                            if ext == '.zip':
                                extract_and_sort_zip(chemin_local, dossier_principal)
                                
                            # Politesse réseau stricte pour les infrastructures ministérielles
                            time.sleep(1.2)
                        else:
                            print(f"    [Échec] Statut HTTP {res_file.status_code}")
                    except Exception as e:
                        print(f"    [Erreur requete] Impossible de récupérer le fichier : {e}")
                        
            print(f"[Fin de Page] Terminée. {fichiers_telecharges} nouveaux fichiers traités.")
            
        except Exception as e:
            print(f"[Exception Globale] Erreur sur la page {page_url} : {e}")
            
    print("\n====================================================================")
    print("PROCESSUS ÉDUSCOL TERMINÉ. Les archives ont été décompressées et triées.")
    print(f"Consultez le dossier : '{dossier_principal}'")
    print("====================================================================")

if __name__ == "__main__":
    scrape_eduscol_nsi()
