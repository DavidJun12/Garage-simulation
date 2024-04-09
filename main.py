import tkinter as tk
from turtle import RawTurtle, Canvas
import vehicles
import random


def create_vehicle_frame(parent, vehicle, x, y, width, height, bg_color):
    frame = tk.Frame(parent, width=width, height=height, relief=tk.RAISED, borderwidth=0)
    frame.configure(bg=bg_color)
    frame.place(x=x, y=y)

    label = tk.Label(frame, text=f"{type(vehicle).__name__} Details")
    label.place(x=170, y=10, anchor="nw")
    
    # Display vehicle details
    tk.Label(frame, text=f"Make: {vehicle.get_make()}").place(x=10, y=25, anchor="nw")
    tk.Label(frame, text=f"Model: {vehicle.get_model()}").place(x=10, y=50, anchor="nw")
    tk.Label(frame, text=f"Mileage: {vehicle.get_mileage()}").place(x=10, y=75, anchor="nw")
    tk.Label(frame, text=f"Price: {vehicle.get_price()}").place(relx=10, rely=100, anchor="nw")
    if isinstance(vehicle, vehicles.Car):
        tk.Label(frame, text=f"Number of Doors: {vehicle.get_doors()}").place(x=10, y=100, anchor="nw")

    elif isinstance(vehicle, vehicles.Truck):
        tk.Label(frame, text=f"Drive Type: {vehicle.get_drive_type()}").place(x=10, y=100, anchor="nw")
    elif isinstance(vehicle, vehicles.SUV):
        tk.Label(frame, text=f"Passenger Capacity: {vehicle.get_pass_cap()}").place(x=10, y=100, anchor="nw")

    # Add canvas container for vehicle diagram
    canvasContainer = tk.Canvas(frame, width=370, height=330, borderwidth=0, relief=tk.SOLID)
    canvasContainer.place(x=5,y=150)

    # Add canvas for drawing the vehicle

    sizes = [(0.4, 0.4),(0.55, 0.55), (1.0, 1.0), (0.7, 0.7), (0.85, 0.85)]   # define set of predefined sizes
    #sizes = [(1.0, 1.0)]   # define set of predefined sizes

    random_size = random.choice(sizes)  # select random size from predefined set
    canvasDraw = tk.Canvas(canvasContainer,  borderwidth=0)
    canvasDraw.place(relwidth=random_size[0], relheight=random_size[1], anchor="nw")  # Use relative width and height to match canvasContainer
    
    
    # Schedule the drawing function to run after a short delay to ensure canvas is properly initialized and displayed
    canvasDraw.after(60, draw_vehicle, canvasDraw, vehicle)



# draw vehicles
def draw_vehicle(canvasDraw, vehicle):

    if isinstance(vehicle, vehicles.Car):
        rel_vertices = [(0.04, 0.42), (0.18, 0.4), (0.32, 0.3 ), (0.6,0.3 ), (0.8,0.4), (0.95,0.42), (0.96, 0.6), (0.7,0.62),(0.2, 0.62),(0.03, 0.6), (0.05,0.5)]
        windowRel_vertices = [(0.21, 0.41), (0.33, 0.31), (0.45, 0.31), (0.45, 0.41)]
        windowRel_vertices_2 = [(0.47, 0.31), (0.6, 0.31),(0.76, 0.41), (0.47, 0.41)]


        vertices = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in rel_vertices]
        windowVertices = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in windowRel_vertices]
        windowVertices_2 = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in windowRel_vertices_2]


        canvasDraw.create_polygon(vertices, fill="blue")
        canvasDraw.create_polygon(windowVertices, fill="grey")
        canvasDraw.create_polygon(windowVertices_2, fill="grey")


        canvasDraw.create_oval(0.18*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.38*canvasDraw.winfo_width() ,0.7*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.22*canvasDraw.winfo_width(), 0.54*canvasDraw.winfo_height(), 0.34*canvasDraw.winfo_width() ,0.66*canvasDraw.winfo_height(), fill="white")
        canvasDraw.create_oval(0.66*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.86*canvasDraw.winfo_width() ,0.7*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.7*canvasDraw.winfo_width(), 0.54*canvasDraw.winfo_height(), 0.82*canvasDraw.winfo_width() ,0.66*canvasDraw.winfo_height(), fill="white")


    elif isinstance(vehicle, vehicles.Truck):
        rel_vertices = [(0.05, 0.1), (0.6, 0.1), (0.6, 0.6), (0.05, 0.6)]
        rel_vertices2 = [(0.61, 0.2), (0.8, 0.2), (0.95, 0.35), (0.96, 0.6),(0.61, 0.6)]
        vertices = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in rel_vertices]
        vertices2 = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in rel_vertices2]
        windowRel_vertices_2 = [(0.63, 0.22), (0.79, 0.22),(0.9, 0.35), (0.63, 0.35)]
        windowVertices_2 = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in windowRel_vertices_2]

        canvasDraw.create_polygon(vertices, fill="green")
        canvasDraw.create_polygon(vertices2, fill="green")
        canvasDraw.create_polygon(windowVertices_2, fill="grey")


        canvasDraw.create_oval(0.15*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.37*canvasDraw.winfo_width() ,0.72*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.20*canvasDraw.winfo_width(), 0.55*canvasDraw.winfo_height(), 0.32*canvasDraw.winfo_width() ,0.67*canvasDraw.winfo_height(), fill="white")

        canvasDraw.create_oval(0.68*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.9*canvasDraw.winfo_width() ,0.72*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.73*canvasDraw.winfo_width(), 0.55*canvasDraw.winfo_height(), 0.85*canvasDraw.winfo_width() ,0.67*canvasDraw.winfo_height(), fill="white")
        

    elif isinstance(vehicle, vehicles.SUV):
        rel_vertices = [(0.18, 0.2), (0.65, 0.2), (0.7, 0.35), (0.95, 0.37), (0.95,0.6), (0.18, 0.6)]
        windowRelVertices_1 = [(0.22, 0.23), (0.4, 0.23), (0.4, 0.36), (0.22,0.36)]
        windowRel_vertices_2 = [(0.43, 0.23), (0.64, 0.23),(0.68, 0.36), (0.43, 0.36)]

        vertices = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in rel_vertices]
        canvasDraw.create_polygon(vertices, fill="red")

        verticesWindow_1 = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in windowRelVertices_1]
        windowVertices_2 = [(canvasDraw.winfo_width() * x, canvasDraw.winfo_height() * y) for x, y in windowRel_vertices_2]

        canvasDraw.create_polygon(verticesWindow_1, fill="grey")
        canvasDraw.create_polygon(windowVertices_2, fill="grey")


        canvasDraw.create_oval(0.24*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.44*canvasDraw.winfo_width() ,0.7*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.28*canvasDraw.winfo_width(), 0.54*canvasDraw.winfo_height(), 0.40*canvasDraw.winfo_width() ,0.66*canvasDraw.winfo_height(), fill="white")

        canvasDraw.create_oval(0.68*canvasDraw.winfo_width(), 0.5*canvasDraw.winfo_height(), 0.88*canvasDraw.winfo_width() ,0.7*canvasDraw.winfo_height(), fill="black")
        canvasDraw.create_oval(0.72*canvasDraw.winfo_width(), 0.54*canvasDraw.winfo_height(), 0.84*canvasDraw.winfo_width() ,0.66*canvasDraw.winfo_height(), fill="white")



def draw_sunflower(canvasFlower, x, y):

    # Create a RawTurtle object to draw on the canvas
    turtle = RawTurtle(canvasFlower)
    turtle.hideturtle()
    

    # Disable animation and screen updates
    turtle._tracer(0)
    
    # Move turtle to the specified position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


    # Draw sunflower petals
    
    turtle.color(round(random.uniform(0, 1),2), round(random.uniform(0, 1),2), round(random.uniform(0, 1),2))
    for _ in range(8):
        draw_petal(turtle, 50)
        turtle.begin_fill()  # Start filling the petal
        for _ in range(2):
            turtle.circle(20, 100)  # Draw the petal shape
            turtle.lt(90)
        turtle.end_fill()  # End filling the petal
        turtle.circle(0, 22)  # Move to draw the center

    # Draw sunflower center
    turtle.penup()
    turtle.goto(x-2, y-5)  # Move turtle to the center of the canvas
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Update the Tkinter canvas to display the final drawing
    canvasFlower.update()
 

# Function to draw petal shape
def draw_petal(turtle, radius):
    turtle.penup()
    turtle.rt(1)
    turtle.pendown()
    turtle.circle(radius, 1)
    turtle.lt(90)
    turtle.circle(radius, 3)
    turtle.penup()
    turtle.rt(180)


def restart(root):
    # Function to rerun the code and redraw vehicles with a new random size
    root.destroy()  # Destroy the current Tkinter window
    main()  # Rerun the main function to redraw vehicles

    # Create a new Tkinter window with the updated vehicles
    root.mainloop()

def main():
    root = tk.Tk()
    root.title("Car Inventory")
    root.geometry("1200x670")  # Set window size
    
    canvasFlower = Canvas(root, width =1170, height=110)
    canvasFlower.place(relx=0.01, rely=0.8, anchor="nw")



    #schedule drawing of sunflowers
    for x in range(-520, 560, 60):

        if (x <= 0):

            canvasFlower.after(10, draw_sunflower, canvasFlower, x, 0)
            canvasFlower.after(10, draw_sunflower, canvasFlower, -x, 0)

        #draw_sunflower(canvasFlower,x,0) 

    # Create vehicles
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    # Place frames for each vehicle with larger sizes and different background colors
    create_vehicle_frame(root, car, x=10, y=0, width=390, height=550, bg_color="white")
    create_vehicle_frame(root, truck, x=405, y=0, width=390, height=550, bg_color="white")
    create_vehicle_frame(root, suv, x=800, y=0, width=390, height=550, bg_color="white")

    
     # Create restart button
    restart_button = tk.Button(root, text="Restart", background="green",width=8, height=2, command=lambda: restart(root))
    restart_button.place(relx=0.46, rely=0.95, anchor="nw")
    
    root.mainloop()

if __name__ == "__main__":
    main()
