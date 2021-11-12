
import time
import turtle
# setting up the drawing pen
drawer = turtle.Turtle()
drawer.pensize(4)
drawer.speed(0)
drawer.pencolor("gold")
drawer.hideturtle()


# setting up the  turtle screen
screen = turtle.Screen()
screen.title("Designing Watch")
screen.bgcolor("black")
screen.tracer(0)   # turns the turtle animations off to increase the drawing speed


def make_watch(drawing_pen, radius):  # to draw the watch face
    drawing_pen.penup()
    drawing_pen.goto(0, 150)
    drawing_pen.right(180)
    drawing_pen.pendown()
    drawing_pen.color("blue")
    drawing_pen.circle(radius)


radius_of_watch = 150


def mark_points_for_hours(marker, angle):

    make_watch(drawer, radius_of_watch)
    marker.penup()
    marker.goto(0, 0)
    marker.right(90)
    marker.pencolor("gold")
    marker.pensize(2)

    i = 12
    while i >= 1:
        marker.forward(130)
        marker.pendown()
        marker.write(i)
        marker.forward(20)
        marker.penup()
        marker.goto(0, 0)
        marker.left(angle)
        i -= 1


angleForHourMarker = 30            # angle for hour points marker is 360/12 = 30


def mark_points_for_minutes(marker, angle):
    mark_points_for_hours(drawer, angleForHourMarker)
    marker.pensize(1)
    marker.pencolor("white")
    marker.penup()
    marker.goto(0, 0)
    marker.setheading(90)

    i = 0
    while i < 60:
        marker.forward(140)
        marker.pendown()
        marker.forward(10)
        marker.penup()
        marker.goto(0, 0)
        marker.right(angle)
        i += 1


angleForMinuteMarker = 6               # angle for minute points marker is 360/60 = 6
mark_points_for_minutes(drawer, angleForMinuteMarker)


def hour_pointer(hour, minute,  pointer, pointer_color):    # creating function for hour hand
    pointer.pensize(5)
    pointer.penup()
    pointer.goto(0, 0)
    pointer.color(pointer_color)
    pointer.setheading(90)
    angle = (hour/12)*360 + (minute/2)  # causes the hour pointer to move proportionally to minute
    pointer.right(angle)
    pointer.pendown()
    pointer.forward(60)


def minute_pointer(minute, second, pointer, pointer_color):    # creating function for minute hand
    pointer.pensize(3)
    pointer.penup()
    pointer.goto(0, 0)
    pointer.color(pointer_color)
    pointer.setheading(90)
    angle = (((minute / 60) * 360) + ((second/3600)*360))   # causes the minute pointer to move proportionally to second
    pointer.right(angle)
    pointer.pendown()
    pointer.forward(80)


def second_pointer(second, pointer, pointer_color):   # creating function for second hand
    pointer.pensize(1)
    pointer.penup()
    pointer.goto(0, 0)
    pointer.color(pointer_color)
    pointer.setheading(90)
    angle = (second / 60) * 360
    pointer.right(angle)
    pointer.pendown()
    pointer.forward(110)


hourPointerColor = "red"
minutePointerColor = "yellow"
secondPointerColor = "orange"
hourPointer = turtle.Turtle()
minutePointer = turtle.Turtle()
secondPointer = turtle.Turtle()


def update_time():
    while True:
        hour = int(time.strftime("%I"))     # returns integer representation of hour from time object
        minute = int(time.strftime("%M"))   # returns integer representation of minute from time object
        second = int(time.strftime("%S"))   # returns integer representation of second from time object
        hour_pointer(hour, minute,  hourPointer, hourPointerColor)
        minute_pointer(minute, second, minutePointer, minutePointerColor)
        second_pointer(second, secondPointer, secondPointerColor)

        screen.update()              # updates the Turtle Screen
        time.sleep(1)
        secondPointer.clear()        # deletes second pointer from the screen
        minutePointer.clear()        # deletes second pointer from the screen
        hourPointer.clear()          # deletes second pointer from the screen


update_time()


screen.mainloop()
