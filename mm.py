# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import pkgutil, csv


def get_modules():
    modules_list = []
    for pkg in pkgutil.iter_modules():
        modules_list.append(pkg[1])
    return modules_list
    
def open_file(filename):
    with open(filename, 'r', encoding = 'UTF-8', errors = 'replace') as file:
        text = file.read()
    return text

def get_imports(text):    
    import_list = []
    for line in text.split('\n'):
        if line.find('import') == 0 or line.find('from') == 0:
            module_name = line.split()[1:]
            if module_name != []:
                for module in module_name:
                    if module.find('import') == 0 or module.find('as') == 0:
                        break
                    else:
                        if module.find('.') != -1:
                            module = module.split('.')[0]
                        module = module.replace(',', '')
                        import_list.append(module)
    import_list = set(import_list)                        
    return import_list
   
def not_installed_modules(import_list):
    unique_list = []
    standard_modules = ['sys']
    modules_list = get_modules()
    for module in import_list:
        if module in modules_list or module in standard_modules:
            pass
        else:
            unique_list.append(module)      
    return unique_list

def replace_modules_for_pip(unique_list):
    import_modules, pip_modules, headerz = [], [], []
    with open('modules.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headerz = next(reader)
        for row in reader:    
            import_modules.append(row[0])
            pip_modules.append(row[1].replace(' ', ''))
    for unique in unique_list:
        if unique in import_modules:
            unique_index = unique_list.index(unique)
            import_index = import_modules.index(unique)
            unique_list[unique_index] = pip_modules[import_index]
    return unique_list  

def forming_requirements(unique_list):
    with open('requirements.txt', 'w') as file:
        requirements = '\n'.join(unique_list)
        file.write(requirements)
    return requirements
  
def main():
    parser = ArgumentParser()
    
    parser.add_argument("--requirements", "-r",
                        action="store_true", dest="req", default=False,
                        help="Create requirements.txt file from script.")
                        
    parser.add_argument("--file", "-f",
                        dest="filename", help="Python file to check import modules.")
          
    args = parser.parse_args()
    
    if args.filename:
        text = open_file(args.filename)
        import_list = get_imports(text)
        unique_list = not_installed_modules(import_list)
        replace_list = replace_modules_for_pip(unique_list)
        if replace_list != []:
            if args.req:
                forming_requirements(replace_list)
                print('File requirements was created.\nUse pip install -r requirements.txt')
            else:
                replace_list = ' '.join(replace_list)
                print('Formed list modules, use for install:\npip install ' + replace_list)
        else:
            print('No missing modules')
if __name__ == "__main__":
    main()
