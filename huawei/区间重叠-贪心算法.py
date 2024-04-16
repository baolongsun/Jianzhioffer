input_list = [[1,4],[3,6],[2,5]]
input_list = sorted(input_list,key=lambda x:x[0])
num_len = len(input_list)
for i in range(num_len):
    print(i)


def main():
    # 获取区间个数
    count = int(input().strip())

    # 排序
    intervals = [list(map(int, input().strip().split(','))) for _ in range(count)]
    intervals.sort()

    interval_stack = [intervals[0]]

    # 遍历并合并区间
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        top_interval = interval_stack[-1] if interval_stack else None

        while True:
            # 如果栈为空，直接加入当前区间
            if not top_interval:
                interval_stack.append(current_interval)
                break

            top_start, top_end = top_interval
            current_start, current_end = current_interval

            # 当前区间在栈顶区间的左侧且没有重叠
            if current_end <= top_start:
                break

            # 当前区间在栈顶区间的左侧但与其有重叠
            elif current_start <= top_start and current_end <= top_end:
                break

            # 当前区间完全覆盖栈顶区间
            elif current_start <= top_start and current_end > top_end:
                interval_stack.pop()

            # 当前区间在栈顶区间内部，但终点超出
            elif current_start > top_start and current_end > top_end:
                interval_stack.append([top_end, current_end])
                break

            # 当前区间在栈顶区间的右侧且没有重叠
            else:
                interval_stack.append(current_interval)
                break

            # 更新栈顶区间
            top_interval = interval_stack[-1] if interval_stack else None

    print(len(interval_stack))


if __name__ == "__main__":
    main()

