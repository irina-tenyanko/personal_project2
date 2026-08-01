class Place:
    def __init__(self,name,country,description,image_url,visited):
        self.name = name
        self.country = country
        self.description = description
        self.image_url = image_url
        self.visited = visited

    def get_status(self):
        if self.visited:
            return "Вже відвідано"
        return "Хочу відвідати"
    