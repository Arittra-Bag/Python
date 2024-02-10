import time

class CountdownTimer:
    def __init__(self, duration_seconds):
        self.duration_seconds = duration_seconds
        self.start_time = None
        self.paused = False
        self.paused_duration = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        if self.start_time and not self.paused:
            self.paused = True
            self.paused_duration = self.get_elapsed_time()

    def resume(self):
        if self.paused:
            self.paused = False
            self.start_time = time.time() - self.paused_duration

    def reset(self):
        self.start_time = None
        self.paused = False
        self.paused_duration = 0

    def get_elapsed_time(self):
        if self.start_time:
            if self.paused:
                return self.paused_duration
            else:
                return time.time() - self.start_time
        else:
            return 0

    def display_time(self):
        remaining_time = self.duration_seconds - self.get_elapsed_time()
        minutes, seconds = divmod(int(remaining_time), 60)
        print(f"Time remaining: {minutes:02}:{seconds:02}")

def main():
    print("Welcome to the Countdown Timer")
    duration = int(input("Enter the countdown duration in seconds: "))
    timer = CountdownTimer(duration)

    while True:
        print("\nOptions:")
        print("1. Start")
        print("2. Pause")
        print("3. Resume")
        print("4. Reset")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            timer.start()
            print("Timer started.")
        elif choice == '2':
            timer.pause()
            print("Timer paused.")
        elif choice == '3':
            timer.resume()
            print("Timer resumed.")
        elif choice == '4':
            timer.reset()
            print("Timer reset.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

        if not timer.paused:
            timer.display_time()

if __name__ == "__main__":
    main()
