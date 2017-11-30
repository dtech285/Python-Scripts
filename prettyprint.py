def pp_json(json_thing, sort=True, indents=4):
    import json
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


if __name__ == "__main__":
	pp_json(your_json_string_or_dict)
