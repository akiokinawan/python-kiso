def build_person(first_name, last_name, age=10):
    """人についての情報を辞書で返す"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
musicians = build_person('jimi', 'hendrix')
print(musician)
print(musicians)
