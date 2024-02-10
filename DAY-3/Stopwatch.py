import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.paused_time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.paused_time = time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped.")

    def resume(self):
        if not self.running:
            self.start_time = time.time() - self.paused_time
            self.running = True
            print("Stopwatch resumed.")

    def reset(self):
        self.start_time = None
        self.paused_time = 0
        self.running = False
        print("Stopwatch reset.")

    def display_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
        else:
            elapsed_time = self.paused_time

        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

if __name__ == "__main__":
    stopwatch = Stopwatch()

    while True:
        print("\nOptions:")
        print("1. Start")
        print("2. Stop")
        print("3. Resume")
        print("4. Reset")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            stopwatch.start()
        elif choice == '2':
            stopwatch.stop()
        elif choice == '3':
            stopwatch.resume()
        elif choice == '4':
            stopwatch.reset()
        elif choice == '5':
            break

        stopwatch.display_time()
