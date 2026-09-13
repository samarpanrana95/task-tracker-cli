from datetime import datetime

class Task:
    def __init__(self, id_number, description):
        self.id = id_number
        self.status = 'todo'
        self.description = description
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.updatedAt = self.createdAt

    def to_dict (self):
        return {
            'id' : self.id,
            'status': self.status,
            'description': self.description,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }

