# Given a list of n numbers, determine if it contains any duplicate numbers.
# If given n list of numbers check if there are duplicate numbers


def chck_dup(arr, size):
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] == [j]:
                print(arr[i], end="")

    arr = [1, 2, 3, 4, 5, 2, 1]
    arr_size = len(arr)
    chck_dup(arr, arr_size)


# find  the longest substring of unique letters in a given string of n letters.


def unique_substring(string):
    no_of_char = 256

    word = len(string)
    cur_len = 1
    max_len = 1
    prev_index = 0
    i = 0

    visited = [-1] * no_of_chars
    # Mark first character as visited to store
    # first character in visited array
    visited[ord(string[0])] = 0

    for i in xrange(1, n):
        prev_index = visited[ord(string[i])]

        if prev_index == -1 or (i - cur_len > prev_idex):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        visited[ord(string[i])] = 1

        if cur_len > max_len:
            max_len = cur_len

        curl_len = i - prev_index

        visited[ord(string[i])] = i

        if cur_len > max_len:
            max_len = cur_len

        return max_len

        string = "ABDEFGABEEE"
        print("The input string is " + string)
        length = unique_substring(string)
        print(str(length))
