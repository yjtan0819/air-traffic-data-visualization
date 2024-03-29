from api import fetcher
from data import a_v_data, aggregate
from project.config import settings

START_DT = settings.START_DT
END_DT = settings.END_DT

AIRPORTS_BY_REGION = [
    # Europe
    ["LFPG", "EGLL", "EHAM", "EDDF", "LEMD", "LIRF", "LSZH", "UUEE"],
    # Eastern Asia
    ["VHHH", "RJBB", "RJTT", "RKSI", "RCTP", "RPLL"],
    # Asia (other)
    ["YSSY", "YMML", "OMDB", "VABB", "VIDP", "WSSS"],
    # Americas
    ["CYYZ", "KSFO", "KLAX", "KATL", "KJFK", "SBGR"],
]


def main_wrapper():
    # intrinsic methods
    print(
        f"Start of our python project: main function called {main_wrapper.__name__}")

    # Stuff here - wrapper!
    # Project structuring for modularity, maintainability, and separation of concerns.

    # Set up a .gitignore and a .pull_template
    # 3. API example. Creating fetcher. from __init__. Create fetcher for states_accessor and tracks_accessor.
    # Create config with pydantic baseSettings. Use env variables and use PyCharm.env files!

    # API fetcher examples
    fetcher.states_accessor()
    # fetcher.tracks_accessor() -> Not supporting it anymore

    # 4. Finish API fetcher. Also add some data folders in gitignore. Like data_to_ignore (with sample example) Also
    # utils example

    # 5. Need to introduce fixed dataset (link). Adding data_ignore to env

    # 6. Now have forming_dataset! Have env variable tied into config in project, Need to use unix time info. Our
    # fetcher needs to change a bit. EXAMPLE1: Forming dataset
    flight_list_formed = aggregate.forming_dataset(start_time=START_DT, end_time=END_DT)

    # EXAMPLE2: Fixed dataset
    flight_list_fixed = aggregate.fixed_dataset()

    # 7. Make sure the time period is more than 2 year. Export csv look at data!

    # 8. Add a_v_data script. Write analyzer. AIRPORTS_BY_REGION should be a global var.

    # Analyzer, visualizer
    cleaned_data = a_v_data.analyze(dataset=flight_list_fixed, airports_subset=AIRPORTS_BY_REGION)

    # 9. Visualizer is a_v_data script.
    a_v_data.visualize(data=cleaned_data, airports_subset=AIRPORTS_BY_REGION)

    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()

    # 10. Future ideas.
    # 1. Implement usage of timezones within your unix time converters
    # 2. Use matplotlib or seaborn instead of altair.
    # 3. Use only the "formed" data. Clean it up the best you can and visualize the data.
    # For example, maybe determine that a departing flight is only considered so if the
    # "departure_airport_candidates_count" is lower than a certain threshold (think env variables).
    # 4. Use another API you find on the web
