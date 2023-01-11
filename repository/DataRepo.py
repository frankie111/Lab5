class DataRepo:
    def __init__(self, file):
        self.file = file

    def add(self, obj):
        obj_list = self.load()
        last_id = obj_list[-1].id if obj_list != [] else 0
        obj.id = last_id + 1
        obj_list.append(obj)
        self.save(obj_list)

    def remove(self, obj):
        obj_list = self.load()
        obj_list.remove(obj)
        self.save(obj_list)

    def update(self, obj, updated_obj):
        obj_list = self.load()
        ind = obj_list.index(obj)
        obj_list[ind] = updated_obj
        self.save(obj_list)

    def find_by_id(self, id_):
        obj_list = self.load()
        filtered = list(filter(lambda obj: obj.id == id_, obj_list))
        return filtered[0] if len(filtered) != 0 else None

    def find_by_ids(self, ids):
        res = []
        for id_ in ids:
            obj = self.find_by_id(id_)
            if obj is not None:
                res.append(obj)

        return res

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
