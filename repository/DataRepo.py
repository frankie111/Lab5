class DataRepo:
    def __init__(self, file):
        self.file = file

    def add(self, obj):
        obj_list = self.load()
        obj_list.append(obj)
        self.save(obj_list)

    def save(self, obj_list):
        self.write_to_file(self.convert_to_string(obj_list))

    def load(self):
        return self.convert_from_string(self.read_file())

    def read_file(self):
        with open(self.file, 'r') as f:
            content = f.read()
            f.close()
        return content

    def write_to_file(self, content):
        with open(self.file, 'w') as f:
            f.write(content)
            f.close()

    def convert_to_string(self, obj_list):
        return ""

    def convert_from_string(self, string):
        return []
