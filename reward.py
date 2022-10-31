def reward_function(params):
    center_variance = params["distance_from_center"] / params["track_width"]

    # racing line 84 points

    left_lane = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 63, 64, 65, 66, 67,
                 68, 69, 70,
                 75, 76, 77, 78, 79, 80, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 119, 120, 121, 122, 123, 124,
                 125, 126]
    center_lane = [10, 11, 12, 13, 37, 38, 58, 59, 60, 71, 72, 73, 74, 81, 82, 83, 93, 94, 106, 107, 116, 117,
                   118]  # Fill in the waypoints

    right_lane = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                  32, 33, 34, 35, 36, 84, 85, 86, 87, 88, 89,
                  90, 91, 92, 108, 109, 110, 111, 112, 113, 114, 115]  # Fill in the waypoint4

    # Speed

    fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
            76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 109, 110, 111, 112, 113, 114, 115, 116,
            117, 121, 122, 123, 124, 125, 126]  # 3

    moderate = [34, 35, 36, 39, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 94, 95, 96, 97, 98, 99, 118, 119, 120]  # 2

    slow = [37, 38, 46, 47, 48, 49, 93, 100, 101, 102, 103, 104, 105, 106, 107, 108]  # 1
    sharp_turns = [48, 107]
    rounded_turns = [37, 57, 119]

    reward = 30

    if params["all_wheels_on_track"]:

        reward += 5

    else:

        reward -= 5

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:

        reward += 10

    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:

        reward += 10

    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:

        reward += 10

    else:

        reward -= 10

    if params["closest_waypoints"][1] in fast:

        if params["speed"] > 3.3:

            reward += 20

        else:

            reward -= 20

    elif params["closest_waypoints"][1] in moderate:

        if params["speed"] > 1 and params["speed"] <= 3.3:

            reward += 10

        else:

            reward -= 10

    elif params["closest_waypoints"][1] in slow:

        if params["speed"] <= 1:

            reward += 10

        else:

            reward -= 10

    # if params["closest_waypoints"][1] in sharp_turns:
    #     if params['steering_angle'] > 20 and params['steering_angle'] < 50:
    #         reward += 25
    #     else:
    #         reward -= 25
    #
    # if params["closest_waypoints"][1] in rounded_turns:
    #     if params['steering_angle'] > 10 and params['steering_angle'] < 20:
    #         reward += 25
    #     else:
    #         reward -= 25

    print("Next point", params["closest_waypoints"][1])
    print("Speed", params["speed"])
    print("Is left", params["is_left_of_center"])

    return float(reward)
