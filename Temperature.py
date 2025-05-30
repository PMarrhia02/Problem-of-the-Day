def analyze_temperatures(temperatures: list[list[float]]) -> tuple[int, int, list[float]]:
    """
    Examines 7 days of data of hourly temperatures.
    
    tasks:
        - Locate the hottest day 
        - Look for the coldest day
        - Return the average temperature for every day.
        
    arguments:
        - temperatures (list\[list\[float\]\]): A list of 7 lists of 24 float 
        values each, representing hourly temperatures for each day.
        - avg (list[float]): A list of 7 floats which gives the average temperature each day.
        - hottest_day (int): Index of the hottest day, 0-based.
        - coldest_day (int): The coldest day index (count starting from 0).

    returns:
        Tuple[int, int, List[float]]:
        - Return the 0-based index of the hottest day as an integer.
        - An integer which refers to the index of the coldest day (zero-based).
        - A list containing 7 number values which are floating and depicting 
        the average temperature on some days.
        
    """
    
    """daily averages"""
    avg = []
    
    for day in temperatures: 
        daily_avg = sum(day) / 24
        avg.append(daily_avg)

    #Find indices of hottest day and coldest day
    hottest_day = avg. index(max(avg))
    coldest_day = avg. index(min(avg))
    
    return hottest_day, coldest_day, avg

if __name__ == "__main__":
    temperatures = [
        [22.0]*24,
        [25.0]*24,
        [18.0]*24,
        [21.0]*24,
        [24.0]*24,
        [23.0]*24,
        [20.0]*24
    ]
    result = analyze_temperatures(temperatures)
    print(result)