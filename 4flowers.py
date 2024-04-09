import tkinter as tk
from turtle import RawTurtle, Canvas

def draw_sunflower(canvas, x, y):
    # Create a RawTurtle object to draw on the canvas
    turtle = RawTurtle(canvas)
    turtle.hideturtle()

    # Disable animation and screen updates
    turtle._tracer(0)

    # Move turtle to the specified position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw sunflower petals
    for _ in range(8):
        turtle.color("yellow")
        draw_petal(turtle, 50)

        turtle.begin_fill()  # Start filling the petal
        for _ in range(2):
            turtle.circle(20, 100)  # Draw the petal shape
            turtle.lt(90)
        turtle.end_fill()  # End filling the petal
        turtle.circle(0, 22)  # Move to draw the center

    # Draw sunflower center
    turtle.penup()
    turtle.goto(x - 2, y - 5)  # Move turtle to the center of the canvas
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Update the Tkinter canvas to display the final drawing
    canvas.update()

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

# Create a Tkinter window
root = tk.Tk()
root.title("Sunflower")
root.geometry("500x500")  # Set window size

# Create a Tkinter canvas to hold the turtle drawing
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Draw four sunflowers on the canvas
draw_sunflower(canvas, -150, 0)
draw_sunflower(canvas, -90, 0)
draw_sunflower(canvas, -30, 0)
draw_sunflower(canvas, 30, 0)

# Run the Tkinter event loop
root.mainloop()
