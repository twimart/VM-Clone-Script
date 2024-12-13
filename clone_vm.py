import subprocess
import sys

def clone_vm(template_vm, clone_name):
    try:
        # Commande pour cloner la VM
        subprocess.run(['VBoxManage', 'clonevm', template_vm, '--name', clone_name, '--register'], check=True)
        
        # Configuration supplémentaire (si nécessaire)
        subprocess.run(['VBoxManage', 'modifyvm', clone_name, '--memory', '1024', '--nic1', 'nat'], check=True)

        print(f"Clone créé avec succès : {clone_name}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du clonage de la VM : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clone_vm.py <nom_de_la_VM_template> <nom_de_la_VM_clone>")
        sys.exit(1)

    template_vm = sys.argv[1]
    clone_name = sys.argv[2]

    clone_vm(template_vm, clone_name)
