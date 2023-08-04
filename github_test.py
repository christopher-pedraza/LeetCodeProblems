import os

problem_name = input("Problem name: ")

os.system('git add .')
os.system(f'git commit -m "Add \'{problem_name}\' solution"')
os.system('git push origin main')