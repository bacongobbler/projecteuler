def multiples_generator(multiple, max_value=1000):
    for i in range(1, max_value):
        if i % multiple == 0:
            yield i

if __name__ == "__main__":
    first_set = set([i for i in multiples_generator(3)])
    second_set = set([i for i in multiples_generator(5)])
    in_second_set_but_not_in_first_set = second_set - first_set
    merged_list = list(first_set) + list(in_second_set_but_not_in_first_set)
    print sum(merged_list)
