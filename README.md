# QuadPype Studio Add-on

This repository contains a collection of plugins and modules designed for use with QuadPype, an open-source pipeline management tool. These plugins are developed to streamline various actions in the pipeline, such as creating, loading, and publishing steps. The repository also includes a module named **quad_pyblish_module**, which is intended for managing various plugins specifically tailored for QuadPype.

## Installation

This plugin should be added in the System Settings (Control Panel of QuadPype), in the Additional Addons.

## DEV

1. Renommer le dossier `quadpype_studio_addon` en `quadpype_studio_addon-v1.X.X` (ATTENTION: le numéro de version dans le nom du dossier doit absolument matcher le numéro de la version contenu dans le fichier `.\quad_studio_addon\version.py`, oui pour le moment rien n'est fait pour automatiser cela).
2. Mettre le dossier dans un dossier parent nommé avec la version majeur et mineur, eemple pour le paquet en version `1.0.5` ça va être `1.0` ou `v1.0` (le v est optionnel).
3. Mettre ce dossier `1.0` dans un dossier parent `studio_addon`.
4. Dans vos User Settings mettre le path absolue vers le dossier `studio_addon`.
5. Relancer QuadPype
