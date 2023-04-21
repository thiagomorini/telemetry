import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Cube
from floor import Floor
from text import Text
from telemetry import Telemetry
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 60

class Game():
    def __init__(self, client, player):
        pygame.init()

        self.is_running = True

        self.x, self.y, self.z = 0, 0, 0
        self.pressed_keys = []

        self.cube = Cube()
        self.floor = Floor()

        self.player = player
        self.telemetry = Telemetry()
        self.client = client

    def setup(self):
        self.display = (SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        pygame.display.set_caption("!!!!!!!!!!!!!!!!")
        self.clock = pygame.time.Clock()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        self.texts = [
            Text("How to move:", 10, 560),
            Text("Arrow keys to move", 10, 530),
            Text("W and S keys for Up and Down", 10, 500),
            Text("Space bar to restart", 10, 470),
            Text("Esc to finish", 10, 440)
        ]

        self.coordinates_text = []

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.floor.draw()

        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        self.cube.draw()
        glPopMatrix()

        self.coordinates_text.append(Text(f"X: {self.x:.2f}", 720, 560))
        self.coordinates_text.append(Text(f"Y: {self.y:.2f}", 720, 530))
        self.coordinates_text.append(Text(f"Z: {self.z:.2f}", 720, 500))
        self.coordinates_text.append(Text(f"Pressed keys: {self.keys}", 10, 10))

        for text in self.texts:
            text.draw()

        for text in self.coordinates_text:
            text.draw()
        self.coordinates_text = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.is_running = False
            pygame.quit()
            quit()

        if keys[pygame.K_LEFT]:
            self.x -= 0.1
            self.pressed_keys.append("LEFT")
        if keys[pygame.K_RIGHT]:
            self.x += 0.1
            self.pressed_keys.append("RIGHT")
        if keys[pygame.K_UP]:
            self.z -= 0.1
            self.pressed_keys.append("UP")
        if keys[pygame.K_DOWN]:
            self.z += 0.1
            self.pressed_keys.append("DOWN")
        if keys[pygame.K_w]:
            self.y += 0.1
            self.pressed_keys.append("W")
        if keys[pygame.K_s]:
            self.y -= 0.1
            self.pressed_keys.append("S")
        if keys[pygame.K_SPACE]:
            self.x, self.y, self.z = 0, 0, 0
            glLoadIdentity()
            gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -5)
            self.pressed_keys.append("SPACE")

        self.keys = "+".join(str(key) for key in self.pressed_keys)
        self.pressed_keys = []

        if self.y < 0 and (glGetDoublev(GL_MODELVIEW_MATRIX)[3][1] + self.y) < 0.5:
            self.y = -glGetDoublev(GL_MODELVIEW_MATRIX)[3][1] + 0.0

    def run(self):
        def send_telemetry(client, telemetry_data):
            client.send_data(telemetry_data)
            with self.thread_lock:
                self.active_threads -= 1

        self.setup()

        self.thread_lock = threading.Lock()
        self.active_threads = 0
        self.max_threads = 8 # Max. threads

        telemetry_queue = []

        while self.is_running:
            self.clock.tick(FRAME_RATE)

            self.handle_events()
            self.draw()

            if self.telemetry.check_distance(self.x, self.y, self.z):
                telemetry_data = self.telemetry.get_telemetry_data(self.player.id, self.x, self.y, self.z, self.keys)

                if self.active_threads >= self.max_threads:
                    telemetry_queue.append(telemetry_data)
                else:
                    t = threading.Thread(target=send_telemetry, args=(self.client, telemetry_data))
                    t.start()
                    with self.thread_lock:
                        self.active_threads += 1

            while self.active_threads < self.max_threads and telemetry_queue:
                telemetry_data = telemetry_queue.pop(0)
                t = threading.Thread(target=send_telemetry, args=(self.client, telemetry_data))
                t.start()
                with self.thread_lock:
                    self.active_threads += 1

            pygame.display.flip()
