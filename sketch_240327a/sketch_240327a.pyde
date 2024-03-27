def setup():
    size(400,400)
def draw():
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.stroke(255, 0, 0)
    s.vertex(0, 0)
    s.vertex(0, 50)
    s.vertex(50, 50)
    s.vertex(50, 0)
    s.endShape(CLOSE)
    fill(255, 0, 0)
    rect (200, 100, 80, 58)
    fill(100, 200, 190)
    shape(s, 25, 25);
	text("text", width/2-30, height/2)
    background(152,190,100)
