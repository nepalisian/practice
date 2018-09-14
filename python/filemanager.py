class FileManager(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.fd = open(self.filename, "w")
        return self.fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.fd.close()
