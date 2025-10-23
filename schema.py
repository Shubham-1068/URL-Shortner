def short_url(data):
    return {
        'short_url': data['sURL'],
        'long_url': data['lURL']
    }

def all_url(data):
    data = list(data)

    for i in data:
        i['_id'] = str(i['_id'])

    return data