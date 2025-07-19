import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL} degrees Celcius"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Convert the ISO string to a datetime object
    date_object = datetime.fromisoformat(iso_string)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = weekdays[date_object.weekday()]
    day = date_object.strftime("%d")  # leading zero day
    year = str(date_object.year)
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month = months[date_object.month - 1]
    return f"{weekday} {day} {month} {year}"
 


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    #convert nasty string to float
    #convert fahrenheit to celcius 
    #return temp as celsius rounded to 1 decimal
    temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_celcius = (temp_in_fahrenheit - 32)*(5/9)
    return round(temp_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
        """
    # mean = sum(data)/len(data).
    #do something about the tricky string test
    #we need an empy list and maybe a for loop?
    #we need to use float.
    ## create empty list
    temp = []
    ##loop 
    for f in (weather_data):
    ## add convert item to list 
        temp.append(float(f))
    list_length = len(weather_data)
    total = sum(temp)
    mean = float(total)/list_length
    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    #open and read csv data.
    # for loop to store data 
    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row:
                date = row[0]
                min_value = float(row[1])
                max_value = float(row[2])
                data.append([date, min_value, max_value])
    return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    #convert strings to floats
    #return min vlaue as float
    #return a tuple of min value and index
    # return empty tuple if list is empty. 
    if not weather_data: 
        return () #return empty tuple if list is empty. 

    min_value = float(weather_data[0]) #return values including strings as float
    min_index = 0
    for index, value in enumerate(weather_data):
        x = float(value)  # Convert string or number to float
        if x < min_value:
            min_value = x
            min_index = index
        elif x == min_value:
    #loop through list to find minimum value
            min_index = index
    return (min_value, min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    #convert strings to floats
    #return max vlaue as float
    #return a tuple of max value and index
    # return empty tuple if list is empty. 
    if not weather_data: 
        return () #return empty tuple if list is empty. 

    max_value = float(weather_data[0]) #return values including strings as float
    max_index = 0
    for index, value in enumerate(weather_data):
        n = float(value)  # Convert string or number to float
        if n > max_value:
            max_value = n
            max_index = index
        elif n == max_value:
    #loop through list to find maximum value
            max_index = index
    return (max_value, max_index)


def generate_summary(weather_data):
    dates = [day[0] for day in weather_data] 
    min_temps = [day[1] for day in weather_data]
    max_temps = [day[2] for day in weather_data]

    num_days = len(weather_data)

    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    min_date = dates[min_index]
    max_date = dates[max_index]

    min_temp_c = convert_f_to_c(min_temp)
    max_temp_c = convert_f_to_c(max_temp)

    avg_low = round(sum([convert_f_to_c(t) for t in min_temps]) / num_days, 1)
    avg_high = round(sum([convert_f_to_c(t) for t in max_temps]) / num_days, 1)

    min_date_str = convert_date(min_date)
    max_date_str = convert_date(max_date)

    summary = f"{num_days} Day Overview\n"
    summary += f"  The lowest temperature will be {min_temp_c:.1f}{DEGREE_SYMBOL}, and will occur on {min_date_str}.\n"
    summary += f"  The highest temperature will be {max_temp_c:.1f}{DEGREE_SYMBOL}, and will occur on {max_date_str}.\n"
    summary += f"  The average low this week is {avg_low:.1f}{DEGREE_SYMBOL}.\n"
    summary += f"  The average high this week is {avg_high:.1f}{DEGREE_SYMBOL}.\n"

    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # loop through lists
    #call day format function
    #call celsius funtion
    #return final summary
    #call celsius funtion
    daily_summary = "" #initialising an empty string for the summary
    for row in weather_data:
        daily_summary += f"---- {convert_date(row[0])} ----\n"
        daily_summary += f"  Minimum Temperature: {convert_f_to_c(row[1])}\N{DEGREE SIGN}C\n"
        daily_summary += f"  Maximum Temperature: {convert_f_to_c(row[2])}\N{DEGREE SIGN}C\n\n"
    return(daily_summary)

