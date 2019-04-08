def make_user_profile(first_name: str, last_name: str, **additional_info) -> {}:
    profile = {}
    profile["first_name"] = first_name
    profile["last_name"] = last_name
    for key, value in additional_info.items():
        profile[key] = value
    return profile


musician = make_user_profile("Kurt", "Kobein", passion="music", plague="drugs")
print(musician)
