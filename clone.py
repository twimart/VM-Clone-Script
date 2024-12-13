import sys

def run_direct_cloning_script(template_vm, clone_name):
    # Importer le premier script de clonage direct ici
    from clone_vm import clone_vm
    clone_vm(template_vm, clone_name)  # Passer le template et le nom du clone


def run_export_import_cloning_script(template_vm, clone_name):
    # Importer le deuxième script de clonage export-import ici
    from export import export_vm, import_vm, clone_vm  # Supposons que le script d'export-import s'appelle "clone_vm_export_import.py"
    clone_vm(template_vm, clone_name, export_dir="C:/Users/wimart_t/VirtualBox VMs/exports")

if __name__ == "__main__":
    # Demander à l'utilisateur de choisir la méthode de clonage
    print("Choisissez la méthode de clonage :")
    print("1 : Clonage direct")
    print("2 : Clonage par export/import")
    
    choice = input("Entrez 1 ou 2 : ")
    
    if choice not in ["1", "2"]:
        print("Choix invalide, veuillez entrer 1 ou 2.")
        sys.exit(1)

    # Lancer le clonage en fonction du choix de l'utilisateur
    if choice == "1":
        template_vm = input("Entrez le nom de la VM template (par exemple, 'Ubuntu_LTS_1') : ")
        clone_name = input("Entrez le nom du clone : ")
        run_direct_cloning_script(template_vm, clone_name)
    elif choice == "2":
        template_vm = input("Entrez le nom de la VM template (par exemple, 'Ubuntu_LTS_1') : ")
        clone_name = input("Entrez le nom du clone : ")
        run_export_import_cloning_script(template_vm, clone_name)  # Passer le template et le clone
