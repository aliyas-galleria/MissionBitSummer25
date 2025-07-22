from PIL import Image, ImageDraw
import random


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        shape = self.attributes.get("shape")
        x, y = self.attributes["position"]
        r = self.attributes["radius"]
        color = self.attributes["color"]

        if shape == "rectangle":
            draw_context.rectangle((x, y, x + r, y + r), fill=color)
        elif shape == "circle":
            draw_context.ellipse((x, y, x + r, y + r), fill=color)
        elif shape == "line":
            draw_context.line((x, y, x + r, y + r), fill=color)
        elif shape == "triangle":
            points = [(x, y - r), (x - r, y + r), (x + r, y + r)]
            draw_context.polygon(points, fill=color)


class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("output.png")


def main():
    canvas = Canvas(500, 500, (0, 0, 0))
    shapes = ["rectangle", "circle", "line", "triangle"]
    for _ in range(50):
        shape_choice = random.choice(shapes)
        attrs = {
            "shape": shape_choice,
            "position": (random.randint(0, 450), random.randint(0, 450)),
            "radius": random.randint(10, 60),
            "color": (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        }
        element = ArtElement(attrs)
        canvas.add_element(element)

    canvas.render()


def render(self):
    draw = ImageDraw.Draw(self.image)
    for element in self.elements:
        element.draw(draw)
    self.image.show()
    self.image.save("output.png")


main()
