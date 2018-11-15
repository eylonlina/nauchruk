_users = {

    'dima': {
        'name': 'Dima Tsimokha',
        'job title': 'Developer',
        'workplace': 'HSE SPb University'
    },

    'sasha': {
        'name': 'Sasha Starikova',
        'job title': 'Designer',
        'workplace': 'HSE SPb University'
    },

    'polina': {
        'name': 'Polina Eylon',
        'job title': 'Meneger',
        'workplace': 'HSE SPb University'
    }

}

def get_user(username):
    return _users.get(username)
