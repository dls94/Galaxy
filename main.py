from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = .1  # percentage in screen width
    vertical_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"INIT W: {str(self.width)} H: {str(self.height)}")
        self.init_vertical_lines()

    def on_parent(self, widget, parent):
        # print(f"ON PARENT W: {str(self.width)} H: {str(self.height)}")
        pass

    def on_size(self, *args):
        # print(f"ON SIZE W: {str(self.width)} H: {str(self.height)}")
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2)
        for i in range(0, self.V_NB_LINES):
            x1 = int(central_line_x + offset * spacing)
            y1 = 0
            x2 = x1
            y2 = self.height
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1


class GalaxyApp(App):
    pass


GalaxyApp().run()
