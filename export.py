import subprocess
import sys
import os

def export_vm(template_vm, export_path):
    try:
        # Commande pour exporter la VM en format OVF
        subprocess.run(['VBoxManage', 'export', template_vm, '--output', export_path], check=True)
        print(f"VM {template_vm} exportée avec succès sous {export_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exportation de la VM : {e}")
        sys.exit(1)

def import_vm(ovf_file, clone_name):
    try:
        # Commande pour importer la VM depuis un fichier OVF
        subprocess.run(['VBoxManage', 'import', ovf_file, '--vsys', '0', '--vmname', clone_name], check=True)
        print(f"Clone de la VM créé avec succès : {clone_name}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'importation de la VM : {e}")
        sys.exit(1)

def clone_vm(template_vm, clone_name, export_dir):
    # Créer un chemin pour le fichier OVF exporté
    export_path = os.path.join(export_dir, f"{clone_name}.ova")
    
    # Exporter la VM template
    export_vm(template_vm, export_path)
    
    # Importer la VM exportée comme clone
    import_vm(export_path, clone_name)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clone_vm_export_import.py <nom_de_la_VM_template> <nom_de_la_VM_clone>")
        sys.exit(1)

    template_vm = sys.argv[1]
    clone_name = sys.argv[2]
    export_dir = "C:/Users/wimart_t/VirtualBox VMs/exports"  # Répertoire d'exportation (à ajuster selon vos préférences)

    # Vérifiez si le répertoire d'export existe, sinon créez-le
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    clone_vm(template_vm, clone_name, export_dir)
