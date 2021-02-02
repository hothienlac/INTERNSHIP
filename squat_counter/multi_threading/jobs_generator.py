


def job_generator(function_to_work, tasks):
    for task in tasks:
        yield [function_to_work, task]
