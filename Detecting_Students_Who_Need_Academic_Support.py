def calculate_average(grades):
    """Calculates the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def count_failures(grades):
    """Counts how many grades are below the passing grade (5)."""
    passing = 5
    counting = 0
    for g in grades:
        if g < passing:
            counting += 1
    return counting


def assess_student(name, grades):
    """
    Evaluates the student's performance using passing = 5.
    Returns a simple text line with the main information.
    """
    passing = 5
    average = calculate_average(grades)
    failures = count_failures(grades)

    if failures >= 2 or average < passing:
        risk = "Needs Support"
    elif failures == 1 or (passing <= average < passing + 1):
        risk = "At Risk"
    else:
        risk = "Performing Well"

    return f"{name}: promedio={average}, suspensos={failures}, riesgo={risk}"
