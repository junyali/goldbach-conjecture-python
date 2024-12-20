
## // Imports \\ ##
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk, messagebox, PhotoImage
import timeit

class GUI:
    # Sieve of eratosthenes is used to find every prime number up to and including n
    def sieve_of_eratosthenes(self, n):
        potential_prime = [True for _ in range(n + 1)]
        primes = []

        # Check all numbers if prime
        i = 2
        while i * i <= self.spinbox_value:
            if potential_prime[i]:
                for j in range(i * i, n + 1, i):
                    potential_prime[j] = False
            i += 1

        # Collects all prime numbers into a separate elist
        for i in range(2, n + 1):
            if potential_prime[i]:
                primes.append(i)

        return primes

    def goldbach_strong_conjecture(self, n, primes):
        sums = []
        # sum_x and sum_y are two prime numbers of which the sum is n
        sum_x, sum_y = 0, 0
        result = 0

        for prime_i in range(len(primes)):
            if result == n:
                sums.append("{x} + {y}".format(x=sum_x, y=sum_y))
            sum_x = primes[prime_i]
            for prime_j in range(len(primes)):
                sum_y = primes[prime_j]
                result = sum_x + sum_y
                # Checks each combination of primes to see if the sum is equal to n
                if result == n:
                    sums.append("{x} + {y}".format(x=sum_x, y=sum_y))
            #self.progress_label.config(text="Checking prime sums [{x} / {y}]".format(x=prime_i * len(primes), y=len(primes) ** 2))

        return sums

    def start_find(self):
        timer_start = timeit.default_timer()

        n = self.spinbox_value
        self.progressbar.start()
        self.progress_label.config(text="Collecting primes up to {}".format(n))

        primes = self.sieve_of_eratosthenes(n)

        self.progress_label.config(text="Finding prime sums of {}".format(n))
        sums = self.goldbach_strong_conjecture(n, primes)

        self.progressbar.stop()
        self.progressbar["value"] = 0

        timer_end = timeit.default_timer()
        time_difference = timer_end - timer_start

        self.progress_label.config(text="Search took {time} seconds".format(time=time_difference))
        self.results_combo.config(values=sums)

    def changed_spinbox_value(self):
        self.spinbox_value = self.prime_spinbox.get()

    def clicked_enter_button(self):
        try:
            self.spinbox_value = int(self.spinbox_value)
        except ValueError:
            tkinter.messagebox.showerror(title="Input Error", message="Non-natural numbers are not accepted", icon=tkinter.messagebox.ERROR)
        else:
            if self.spinbox_value <= 2:
                tkinter.messagebox.showerror(title="Input Error", message="Numbers equal to or less than 2 are not accepted", icon=tkinter.messagebox.ERROR)
            elif self.spinbox_value % 2 != 0:
                tkinter.messagebox.showerror(title="Input Error", message="Non-even numbers are not accepted", icon=tkinter.messagebox.ERROR)
            else:
                self.results_combo.config(values=[], textvariable=tk.StringVar(self.root, "Click for results"))
                self.start_find()


    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Goldbach Conjecture")
        self.root.geometry("260x230")

        image = PhotoImage(file="./program-icon.png")
        self.root.iconphoto(False, image)

        self.prompt_label = tk.Label(self.root, text="Try any even natural number greater than two!", anchor="center", justify="center")
        self.prime_spinbox = tk.Spinbox(self.root, from_=1, to=99999999999999999999, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=tk.IntVar(), font=("Arial", 12), bg="lightgrey", fg="black", state="normal", cursor="hand2", bd=3, justify="center", width=10, wrap=True, command=self.changed_spinbox_value)
        self.enter_button = tk.Button(self.root, text="Let's go!", bd=3, cursor="hand2", overrelief="ridge", width=10, command=self.clicked_enter_button)
        self.progressbar = ttk.Progressbar(self.root, orient="horizontal", mode="indeterminate", length=250)
        self.progress_label = tk.Label(self.root, text="", anchor="center", justify="center", wraplength=250)
        self.results_combo = ttk.Combobox(self.root, state="readonly", values=[], textvariable=tk.StringVar(self.root, "Click for results"))

        self.spinbox_value = self.prime_spinbox.get()
        self.progressbar["value"] = 0

        self.prompt_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N)
        self.prime_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N)
        self.enter_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N)
        self.progressbar.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N)
        self.progress_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N)
        self.results_combo.grid(row=5, column=0, padx=5, pady=5, sticky=tk.N)



if __name__ == '__main__':
    program = GUI()
    program.root.mainloop()
