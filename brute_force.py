def brute_force_time(length, charset):

    attack_speeds = {
        "CPU": 10**6,
        "GPU": 10**9,
        "CLUSTER": 10**12
    }

    combinations = charset ** length

    results = {}

    for attack, speed in attack_speeds.items():

        seconds = combinations / speed

        results[attack] = seconds

    return results