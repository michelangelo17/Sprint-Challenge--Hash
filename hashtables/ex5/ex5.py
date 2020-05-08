def finder(files, queries):
    result = []
    file_dict = {}
    for file in files:
        start = file.rfind('/') + 1
        end = file.rfind('.')
        q_name = None
        if end == -1:
            q_name = file[start:]
        else:
            q_name = file[start:end]
        if q_name in file_dict:
            file_dict[q_name].append(file)
        else:
            file_dict[q_name] = [file]
    for q in queries:
        if q in file_dict:
            result.extend(file_dict[q])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo.txt',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
