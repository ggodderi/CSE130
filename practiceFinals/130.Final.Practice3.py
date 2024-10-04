# Python

def read_runner_data(filename):
    assert filename != None
    assert type(filename) == type('')
    runner_data = []
    with open(filename, 'rt') as file_handle:
        assert file_handle != None
        for line in file_handle:
            assert type(line) == type('')
            runner_data.append(line.strip().split(','))
    
    assert len(runner_data) > 0
    for runner in runner_data:
        assert type(runner) == type([])
        assert len(runner) == 2
    return runner_data


def main():
    runner_data = read_runner_data('130.Final.Practice3.data.txt')
    # print(runner_data)
    assert len(runner_data) > 0

    fast_runners = []
    for runner in runner_data:
        # print(runner[1])
        assert type(runner) == type([])
        assert len(runner) == 2
        assert type(runner[1]) == type('')
        if int(runner[1]) <= 300:
            fast_runners.append(runner)

    print(fast_runners)
main()
