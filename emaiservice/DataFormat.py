import json

class DataFormat:
        
    def data_format(self, username, email, barbeiro, servico, date, time):
        dic_info = {
            'user': username,
            'email': email,
            'barber': barbeiro,
            'servico': servico,
            'date': date,
            'time': time
        }
        
        return json.dumps(dic_info)