def setup():
    size(400,400)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.stroke()
    s.vertex(0, 0)
    s.vertex(0, 50)
    s.vertex(50, 50)
    s.vertex(50, 0)
    s.endShape(CLOSE)
    fill(255, 0, 0)
def draw():
    rect (200, 100, 80, 58)
    fill(100, 200, 190)
    shape(s, 25, 25);
	background(152,190,100)
