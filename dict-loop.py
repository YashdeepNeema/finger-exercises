# In this program I'm trying to learn how to loop through a dictionary:

user_0 = {
    'username': 'efermi',
    'first_name': 'erico',
    'last_name': 'fermi',
}

for key, value in user_0.items():
    print(f'\n{key} : {value}');
print('\n')


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'sheldon': 'fortran',

}

for name, language in favorite_languages.items():
    print(f'{name.title()}\'s favorite language is {language.title()}.' );
print('\n')
