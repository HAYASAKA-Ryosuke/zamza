#!coding:utf-8


class IC:
    top_margin = 20
    bottom_margin = 20
    left_margin = 40
    right_margin = 40
    pin_margin = 10
    fontsize = 10
    pin_length = 10

    def __init__(self):
        self.ic_name = {}
        self.width_margin = self.left_margin + self.right_margin
        self.height_margin = self.top_margin + self.bottom_margin
        self.top_pin_pos = []
        self.right_pin_pos = []
        self.left_pin_pos = []
        self.bottom_pin_pos = []
        self.top_ic_text = []
        self.bottom_ic_text = []
        self.left_ic_text = []
        self.right_ic_text = []

    def name(self, name):
        """icに名前をつけるとそのICの幅，高さ，それぞれのピンの位置, それぞれのピンの名前"""
        self.ic_name[name] = {"width": self.width, "height": self.height, "top_pin": list(self.top_ic_text), "left_pin": list(self.left_ic_text), "right_pin": list(self.right_ic_text), "bottom_pin": list(self.bottom_ic_text), "top_pin_pos": list(self.top_pin_pos), "left_pin_pos": list(self.left_pin_pos), "right_pin_pos": list(self.right_pin_pos), "bottom_pin_pos": list(self.bottom_pin_pos)}
        self.top_pin_pos = []
        self.right_pin_pos = []
        self.left_pin_pos = []
        self.bottom_pin_pos = []
        self.top_ic_text = []
        self.bottom_ic_text = []
        self.left_ic_text = []
        self.right_ic_text = []

    def __contour(self, x, y, width, height, color='black'):
        self.draw_line.line(((x, y), (x, y + height), (x + width, y + height), (x + width, y), (x, y)), fill=color, width=2)

    def pin(self, top=0, left=0, bottom=0, right=0):
        self.width = max(top, bottom) * self.pin_margin + max(top, bottom) * self.fontsize + self.width_margin
        self.height = max(left, right) * self.pin_margin + max(left, right) * self.fontsize + self.height_margin

    def draw(self, x, y, pin_color='red', text_color='black'):
        fontsize = self.fontsize
        self.__contour(x=x, y=y, width=self.width, height=self.height)
        for i, text in enumerate(self.top_ic_text):
            pos = (x + (i * self.pin_margin) + (i * fontsize) + self.width_margin // 2, y)
            self.draw_line.text(pos, str(text), font=self.font, fill=text_color)
            self.draw_line.line(((pos[0], pos[1]), (pos[0], pos[1] - self.pin_length)), fill=pin_color)
            self.top_pin_pos.append(pos)
        for i, text in enumerate(self.left_ic_text):
            pos = (x - self.pin_length, y + (i * self.pin_margin) + (i * fontsize) + self.height_margin // 2)
            self.draw_line.text(pos, str(text), font=self.font, fill=text_color)
            self.draw_line.line(((pos[0], pos[1]), (pos[0] + self.pin_length, pos[1])), fill=pin_color)
            self.left_pin_pos.append(pos)
        for i, text in enumerate(self.bottom_ic_text):
            pos = (x + (i * self.pin_margin) + (i * fontsize) + self.width_margin // 2, y + self.height + self.pin_length)
            self.draw_line.text(pos, str(text), font=self.font, fill=text_color)
            self.draw_line.line(((pos[0], pos[1]), (pos[0], pos[1] - self.pin_length)), fill=pin_color)
            self.bottom_pin_pos.append(pos)
        for i, text in enumerate(self.right_ic_text):
            pos = (x + self.width + self.pin_length, y + (i * self.pin_margin) + (i * fontsize) + self.height_margin // 2 + self.pin_length)
            self.draw_line.text(pos, str(text), font=self.font, fill=text_color)
            self.draw_line.line(((pos[0] - self.pin_length, pos[1]), (pos[0], pos[1])), fill=pin_color)
            self.right_pin_pos.append(pos)

    def get_pin_pos(self, ic_name, pin_name):
        if pin_name in self.ic_name[ic_name]["top_pin"]:
            for i, name in enumerate(self.ic_name[ic_name]["top_pin"]):
                if pin_name == name:
                    return ("top", i, self.ic_name[ic_name]["top_pin_pos"][i])
        if pin_name in self.ic_name[ic_name]["left_pin"]:
            for i, name in enumerate(self.ic_name[ic_name]["left_pin"]):
                if pin_name == name:
                    return ("left", i, self.ic_name[ic_name]["left_pin_pos"][i])
        if pin_name in self.ic_name[ic_name]["bottom_pin"]:
            for i, name in enumerate(self.ic_name[ic_name]["bottom_pin"]):
                if pin_name == name:
                    return ("bottom", i, self.ic_name[ic_name]["bottom_pin_pos"][i])
        if pin_name in self.ic_name[ic_name]["right_pin"]:
            for i, name in enumerate(self.ic_name[ic_name]["right_pin"]):
                if pin_name == name:
                    return ("right", i, self.ic_name[ic_name]["right_pin_pos"][i])

    def text(self, top, left, bottom, right):
        self.top_ic_text = top
        self.left_ic_text = left
        self.bottom_ic_text = bottom
        self.right_ic_text = right
