from OpenGL.GL import *

class Floor:
    def draw(self):
        glBegin(GL_LINES)
        glColor3f(0, 0, 1)
        for i in range(-40, 41, 2):
            # horizontal lines
            glVertex3f(-40, -1, i)
            glVertex3f(40, -1, i)
            # vertical lines
            glVertex3f(i, -1, -40)
            glVertex3f(i, -1, 40)
        glEnd()
