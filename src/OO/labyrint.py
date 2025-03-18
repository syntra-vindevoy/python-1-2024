import tkinter as tk
import random
import heapq
import time


class Robot:
    def __init__(self, labyrinth, start, exit):
        self.labyrinth = labyrinth
        self.start = start
        self.exit = exit
        self.position = start

    def move(self, direction):
        x, y = self.position
        if direction == "up":
            return x - 1, y
        elif direction == "down":
            return x + 1, y
        elif direction == "left":
            return x, y - 1
        elif direction == "right":
            return x, y + 1
        return x, y

    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < len(self.labyrinth) and 0 <= y < len(self.labyrinth[0]):
            return self.labyrinth[x][y] == ' '  # Path is represented by space
        return False

    def a_star_search(self):
        # A* search implementation
        open_list = []
        closed_list = set()
        came_from = {}

        # f = g + h
        g_score = {self.start: 0}
        h_score = {self.start: self.heuristic(self.start)}

        heapq.heappush(open_list, (g_score[self.start] + h_score[self.start], self.start))

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == self.exit:
                return self.reconstruct_path(came_from)

            closed_list.add(current)

            # Explore neighbors (up, down, left, right)
            for direction in ["up", "down", "left", "right"]:
                neighbor = self.move(direction, current)
                if neighbor in closed_list or not self.is_valid_move(neighbor):
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + h_score[neighbor]
                    heapq.heappush(open_list, (f_score, neighbor))

        return None  # No path found

    def heuristic(self, position):
        # Manhattan distance as heuristic
        return abs(position[0] - self.exit[0]) + abs(position[1] - self.exit[1])

    def reconstruct_path(self, came_from):
        current = self.exit
        path = []
        while current != self.start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


class LabyrinthGUI(tk.Tk):
    def __init__(self, labyrinth, robot, size=50, cell_size=20):
        super().__init__()

        self.labyrinth = labyrinth
        self.robot = robot
        self.size = size
        self.cell_size = cell_size
        self.title("Robot Pathfinding")

        # Set up the canvas
        self.canvas = tk.Canvas(self, width=size * cell_size, height=size * cell_size)
        self.canvas.pack()

        # Draw the initial labyrinth
        self.draw_labyrinth()

    def draw_labyrinth(self):
        for i in range(self.size):
            for j in range(self.size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = (j + 1) * self.cell_size
                y2 = (i + 1) * self.cell_size

                if self.labyrinth[i][j] == '*':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black")
                elif (i, j) == self.robot.position:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    def update_robot_position(self):
        self.canvas.delete("all")
        self.draw_labyrinth()

    def run_path(self):
        path = self.robot.a_star_search()

        if path:
            for step in path:
                self.robot.position = step
                self.update_robot_position()
                self.update_idletasks()
                time.sleep(0.1)  # Slow down to see the robot's progress step by step
        else:
            print("No path found")


def generate_labyrinth(size):
    labyrinth = [['*' for _ in range(size)] for _ in range(size)]

    # Create a random path for simplicity (a simple solution for testing)
    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:  # 30% chance to be open space
                labyrinth[i][j] = ' '

    # Ensure start and exit positions are open
    labyrinth[0][0] = ' '  # Start
    labyrinth[size - 1][size - 1] = ' '  # Exit

    # Manually create a path from start to exit (guaranteed valid path)
    create_valid_path(labyrinth, (0, 0), (size - 1, size - 1))

    return labyrinth

def create_valid_path(labyrinth, start, end):
    # Create a simple path between start and end manually by going horizontally then vertically
    x1, y1 = start
    x2, y2 = end

    # Create a horizontal path first
    if x1 != x2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            labyrinth[i][y1] = ' '

    # Then create a vertical path
    if y1 != y2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            labyrinth[x2][j] = ' '

    # Ensure the start and end are paths
    labyrinth[start[0]][start[1]] = ' '
    labyrinth[end[0]][end[1]] = ' '

def main():
    size = 50
    labyrinth = generate_labyrinth(size)
    start = (0, 0)
    exit = (size - 1, size - 1)

    robot = Robot(labyrinth, start, exit)

    # Create the GUI and pass the robot and labyrinth
    app = LabyrinthGUI(labyrinth, robot, size)
    app.after(1000, app.run_path)  # Run pathfinding after a short delay to allow the window to initialize
    app.mainloop()


if __name__ == "__main__":
    main()
