import streamlit as st


def get_standard_equation(x1_gse: float | int, y1_gse: float | int, x2_gse: float | int, y2_gse: float | int) -> str:
    """
    It takes the coordinates of two points on a line, finds the gradient and y-intercept of the line, and returns the
    equation of the line in the form y = mx + c, where m is the gradient and c is the y-intercept

    :param x1_gse: the x-coordinate of the first point
    :type x1_gse: float | int
    :param y1_gse: the y-coordinate of the first point
    :type y1_gse: float | int
    :param x2_gse: the x-coordinate of the second point
    :type x2_gse: float | int
    :param y2_gse: the y-coordinate of the second point
    :type y2_gse: float | int
    :return: The equation of the line in the form y = mx + c
    :rtype: str
    """
    # find the gradient of the line
    gradient = (y2_gse - y1_gse) / (x2_gse - x1_gse)
    # display this to the user
    st.markdown(f"Gradient: `{int(gradient)}`" if gradient.is_integer() else f"`Gradient: {gradient}`")
    # find the y-intercept of the line
    y_intercept = y1_gse - gradient * x1_gse
    # display this to the user
    st.markdown(f"Y-intercept: `{int(y_intercept)}`" if y_intercept.is_integer() else f"Y-intercept: `{y_intercept}`")
    # return the equation of the line, with integer values if possible
    # if the y-intercept is 0, don't show it, or if it is negative, don't show the + sign show in int form when both the gradient and the y intercept are whole numbers
    if y_intercept == 0:
        return f"y = {int(gradient)}x" if gradient.is_integer() else f"y = {gradient}x"
    elif y_intercept < 0:
        return f"y = {int(gradient)}x - {int(-y_intercept)}" if gradient.is_integer() and y_intercept.is_integer() else f"y = {gradient}x - {-y_intercept}"
    # if the y-intercept is positive, show the + sign
    else:
        return f"y = {int(gradient)}x + {int(y_intercept)}" if gradient.is_integer() and y_intercept.is_integer() else f"y = {gradient}x + {y_intercept}"


def get_distance(x1_gd: float | int, y1_gd: float | int, x2_gd: float | int, y2_gd: float | int) -> str:
    """
    It takes the coordinates of two points and returns the distance between them

    :param x1_gd: the x-coordinate of the first point
    :type x1_gd: float | int
    :param y1_gd: the y-coordinate of the first point
    :type y1_gd: float | int
    :param x2_gd: the x-coordinate of the second point
    :type x2_gd: float | int
    :param y2_gd: the y-coordinate of the second point
    :type y2_gd: float | int
    :return: The distance between the two points.
    :rtype: float | int
    """
    distance = ((x2_gd - x1_gd) ** 2 + (y2_gd - y1_gd) ** 2) ** 0.5  # find the distance between the two points
    return f"{int(distance)}" if distance.is_integer() else f"{distance:.2f}"


def get_perpendicular_bisector(x1_gpb: float | int, y1_gpb: float | int, x2_gpb: float | int, y2_gpb: float | int) -> str:
    """
    It finds the midpoint of the line, finds the gradient of the perpendicular bisector, finds the y-intercept of the
    perpendicular bisector, and returns the equation of the perpendicular bisector, with integer values if possible

    :param x1_gpb: the x-coordinate of the first point
    :type x1_gpb: float | int
    :param y1_gpb: y-coordinate of the first point
    :type y1_gpb: float | int
    :param x2_gpb: the x-coordinate of the first point
    :type x2_gpb: float | int
    :param y2_gpb: the y-coordinate of the first point
    :type y2_gpb: float | int
    :return: The equation of the perpendicular bisector of the line between the two points.
    :rtype: str
    """

    midpoint_x = (x1_gpb + x2_gpb) / 2  # find the midpoint of the line
    midpoint_y = (y1_gpb + y2_gpb) / 2
    gradient = (x2_gpb - x1_gpb) / (y1_gpb - y2_gpb)  # find the gradient of the perpendicular bisector
    y_intercept = midpoint_y - gradient * midpoint_x  # find the y-intercept of the perpendicular bisector
    # return the equation of the perpendicular bisector, with integer values if possible
    if y_intercept == 0:
        return f"y = {int(gradient)}x" if gradient.is_integer() else f"y = {gradient}x"
    elif y_intercept < 0:
        return f"y = {int(gradient)}x - {int(-y_intercept)}" if gradient.is_integer() and y_intercept.is_integer() else f"y = {gradient}x - {-y_intercept}"
    else:
        return f"y = {int(gradient)}x + {int(y_intercept)}" if gradient.is_integer() and y_intercept.is_integer() else f"y = {gradient}x + {y_intercept}"


if __name__ == "__main__":
    st.title("Line Equation Calculator")
    # instructions for the app
    st.write(
        "Enter the coordinates of two points on a line, and the app will find the equation of the line,"
        " the distance between the two points, and the equation of the perpendicular bisector of the line.")
    # get the coordinates of the two points from the user
    st.markdown("""#### Coordinate Point 1""")
    x1 = st.number_input("x:", step=1)
    y1 = st.number_input("y:", step=1)
    st.markdown("""#### Coordinate Point 2""")
    x2 = st.number_input("x: ", step=1)
    y2 = st.number_input("y: ", step=1)

    # display the equation of the line
    if st.button("Calculate"):
        st.write("Equation of the line: ")
        st.markdown(f"""`{get_standard_equation(x1, y1, x2, y2)}`""")
        st.write("Distance between the two points: ")
        st.markdown(f"""`{get_distance(x1, y1, x2, y2)}`""")
        st.write("Equation of the perpendicular bisector: ")
        st.markdown(f"""`{get_perpendicular_bisector(x1, y1, x2, y2)}`""")
