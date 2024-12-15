def my_game(pazzl_str: str, answer: list, cnt:int) -> int:
    temp_cnt = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_cnt <= cnt:
        user_str = input(f"{pazzl_str}: \n" ).lower()
        if user_str in answer:
            return temp_cnt
        temp_cnt +=1
    return 0