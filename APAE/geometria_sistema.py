
class Responsive_windows:

    def __init__(self, win):

        self.largura = win.winfo_screenwidth()
        self.altura = win.winfo_screenheight()

    def windows_w(self, percent):
        size = self.largura * percent / 100
        return size

    def windows_h(self, percent):
        size = self.altura * percent / 100
        return size

    def font_windows(self, tam):
        size = int((tam / self.largura) * self.largura)
        return size

class Responsive_container:

    def __init__(self, obj):

        self.largura = obj['width']
        self.altura = obj['height']

    def container_w(self, percent):

        size = self.largura * percent / 100
        return size

    def container_h(self, percent):

        size = self.altura * percent / 100
        return size
