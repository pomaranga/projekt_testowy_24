def setup():
    size(400,400)
def draw():
    background(152,190,100)
	global s = createShape()
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
    rect (300, 100, 65, 65)
    fill(100, 200, 190)
    shape(s, 25, 25);
	text("text", width/2-30, height/2-30)
    stroke(255, 0, 0)
    fill(255, 0, 0)
    rect (20, 10, 80, 50)

