# https://codeforces.com/problemset/problem/1846/G




def main():
    ttt = int(input())
    for _ in range(ttt):
        n, m = map(int, input().split())
        symptoms = input().strip()
        initial_state = int(symptoms, 2)
        medicines = []

        for i in range(m):
            days_to_take = int(input())
            removes = ((1 << n) - 1) ^ int(input().strip(), 2)
            side_effects = int(input().strip(), 2)
            medicines.append(((removes, side_effects), days_to_take))

        inf = float('inf')
        symptoms_states = [inf] * (1 << n)
        symptoms_states[initial_state] = 0
        queue = [(0, initial_state)]

        while queue:
            current_days, current_state = min(queue)
            queue.remove((current_days, current_state))

            for i in range(m):
                to_state = current_state & medicines[i][0][0]
                to_state |= medicines[i][0][1]

                if symptoms_states[to_state] > current_days + medicines[i][1]:
                    queue = [(d, s) for d, s in queue if s != to_state]  # Remove duplicates
                    symptoms_states[to_state] = current_days + medicines[i][1]
                    queue.append((symptoms_states[to_state], to_state))

        if symptoms_states[0] == inf:
            symptoms_states[0] = -1
        print(symptoms_states[0])

if __name__ == "__main__":
    main()
