#Amanda Thill
#1/22/2025
#This program is designed to be a Horror movie
#app for people to purchase all types of Horror movies.

#Import the tkinter module to create GUI applications
#The tkinter library provides various widgets for creating graphical user interfaces.
import tkinter as tk
#Import the messagebox module from tkinter to display message boxes.
#This creates pop-up message boxes showing information, warnings, or errors.
from tkinter import messagebox
from PIL import Image, ImageTk  #Import Pillow for image handling

class HorrorMovieStoreApp:
    """
    This class represents the main application for the Horror Movie Store.
    It handles the login, main window, movie list, cart, and checkout operations.
    """
    def __init__(self, root):
        """
        Initializes the application, setting up the root window and the list of available movies.
        
        Parameters:
        root (Tkinter.Tk): The root window that holds the entire application.
        """
        self.root = root #Root window for the aplication
        self.root.title("Horror Movie Store") #Set title of the application window
        self.root.withdraw()  #Hide the root window initially
        self.movies = [  #List of movies available in the store
            {"title": "The Cabin in the Woods", "genre": "Sci-Fi", "price": 10.95, "image": "images/CabinInTheWoods.gif",
             "description": "Five friends go to a remote cabin where they get more than they bargained for.",
             "cast": "Kristen Connolly, Chris Hemsworth, Anna Hutchison", "release_year": 2012},
            {"title": "Beetlejuice", "genre": "Comedy", "price": 8.99, "image": "images/Beetlejuice.gif",
             "description": "A couple of recently deceased ghosts hire a malicious spirit to scare away the new inhabitants of their former home.",
             "cast": "Michael Keaton, Alec Baldwin, Geena Davis", "release_year": 1988},
            {"title": "Midsommar", "genre": "Slasher", "price": 12.95, "image": "images/Midsommar.gif",
             "description": "A couple travels to Sweden to attend a rural hometown's fabled mid-summer festival, only to find themselves caught in the grip of a pagan cult.",
             "cast": "Florence Pugh, Jack Reynor, Vilhelm Blomgren", "release_year": 2019},
            {"title": "Nosferatu", "genre": "New", "price": 20.99, "image": "images/Nosferatu.gif",
             "description": "A young man is sent to Transylvania to assist a vampire with the purchase of a new home, but the vampire has other plans for his new friend.",
             "cast": "Lily-Rose Depp, Bill Skarsgård, Nicholas Hoult", "release_year": 2024},
            {"title": "The Craft", "genre": "Teen", "price": 15.95, "image": "images/thecraft.gif",
             "description": "A newcomer to a high school joins a trio of outcast teenage girls who practice witchcraft, and they all soon learn the consequences of their powers.",
             "cast": "Robin Tunney, Fairuza Balk, Neve Campbell", "release_year": 1996}
        ]
        self.cart = []  #Initialize an empty cart
        self.create_login_window()  #Create the login window on app startup

    def create_login_window(self):
        """
        Creates the login window where the user will enter their username and password.
        """
        self.login_window = tk.Toplevel(self.root)  #Create a new window for login
        self.login_window.title("Come in if you dare")  #Set the title of the login window
        self.login_window.geometry("500x600")  #Set the size of the login window
        self.login_window.config(bg="black")  #Set the background color to black

        #Add Login Image 
        image_path = "images/HorrorMovieMadness.gif"
        try:
            login_image = Image.open(image_path)  #Use PIL to open the image
            login_image = login_image.resize((200, 200))  #Resize the image
            self.login_image = ImageTk.PhotoImage(login_image)  #Convert image to Tkinter format
            self.login_image_label = tk.Label(self.login_window, image=self.login_image, bg="black")
            self.login_image_label.pack(pady=10)  #Display the login image
        except Exception as e:
            print(f"Error loading login image: {e}")
            tk.Label(self.login_window, text="Login Image (Alt Text)", fg="white", bg="black").pack(pady=10)

        #Username and password input fields
        tk.Label(self.login_window, text="Horror Movie Store Login", font=("Helvetica", 16), fg="red", bg="black").pack(pady=20)
        tk.Label(self.login_window, text="Username:", fg="white", bg="black", font=("Helvetica", 12)).pack(pady=10)
        self.username_entry = tk.Entry(self.login_window, font=("Helvetica", 12))
        self.username_entry.pack(pady=10)

        tk.Label(self.login_window, text="Password:", fg="white", bg="black", font=("Helvetica", 12)).pack(pady=10)
        self.password_entry = tk.Entry(self.login_window, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=10)

        #Login button to submit credentials
        login_button = tk.Button(self.login_window, text="Login", command=self.check_login, bg="green", fg="black")
        login_button.pack(pady=20)  

        #Exit button to close the application
        exit_button = tk.Button(self.login_window, text="Exit", command=self.exit_app, bg="red", fg="white")
        exit_button.pack(pady=10)  #Exit button to quit the app

    def check_login(self):
        """
        Verifies the login credentials and either allows access or shows an error.
        """
        username = self.username_entry.get()  #Get entered username
        password = self.password_entry.get()  #Get entered password

        correct_username = "user"  #Correct username
        correct_password = "password123"  #Correct password

        #If the credentials are correct, open the main movie store window
        if username == correct_username and password == correct_password:
            self.login_window.destroy()  #Close the login window
            self.create_main_window()  #Open the main movie store window
            self.root.deiconify()  #Show the root window after successful login
        else:
            #Show error message if credentails are incorrect
            messagebox.showerror("Login Error", "Incorrect username or password. Please try again.")

    def create_main_window(self):
        """
        Creates the main window that displays the movie list and other functionalities.
        """
        self.root.config(bg="black")  #Set background color for main window

        #Clear any previous widgets to prevent duplication
        for widget in self.root.winfo_children():
            widget.destroy()

        #Display the store title at the top of the window
        title_label = tk.Label(self.root, text="Horror Movie Madness Store", font=("Creepster", 24), fg="red", bg="black")
        title_label.pack(pady=20)

        #Listbox to display available movies
        self.movie_listbox = tk.Listbox(self.root, width=50, height=10)
        self.movie_listbox.pack(pady=10)

        for movie in self.movies:  #Add each movie to the listbox
            self.movie_listbox.insert(tk.END, movie['title'])

        #Add Buttons for "View Movie Details", "View Cart", and "Checkout"
        view_button = tk.Button(self.root, text="View Movie Details", command=self.view_movie_details, bg="darkred", fg="white")
        view_button.pack(pady=10)

        cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart, bg="darkred", fg="white")
        cart_button.pack(pady=10)

        checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout, bg="green", fg="black")
        checkout_button.pack(pady=10)

        #Back to Login button 
        back_to_login_button = tk.Button(self.root, text="Back to Login", command=self.back_to_login, bg="red", fg="white")
        back_to_login_button.pack(pady=10)

    def back_to_login(self):
        """
        Hide the main window and show the login window again
        """
        self.root.withdraw()  #Hide the main window
        self.create_login_window()  #Create and show the login window again

    def view_movie_details(self):
        """
        Displays the details of the selected movie including 
        title, genre, price, details about movie, and image.
        """
        try:
            selected_movie_index = self.movie_listbox.curselection()[0] #Get selected movie index
            selected_movie = self.movies[selected_movie_index] #Get selected movie details

            details_window = tk.Toplevel(self.root) #Create a new window for movie details
            details_window.title(f"{selected_movie['title']} Details")
            details_window.geometry("750x650")
            details_window.config(bg="black")

            #Display movie details in the details window
            tk.Label(details_window, text=f"Title: {selected_movie['title']}", font=("Helvetica", 14), fg="white", bg="black").pack(pady=10)
            tk.Label(details_window, text=f"Genre: {selected_movie['genre']}", font=("Helvetica", 12), fg="white", bg="black").pack(pady=5)
            tk.Label(details_window, text=f"Price: ${selected_movie['price']}", font=("Helvetica", 12), fg="white", bg="black").pack(pady=5)
            tk.Label(details_window, text=f"Release Year: {selected_movie['release_year']}", font=("Helvetica", 12), fg="white", bg="black").pack(pady=5)
            tk.Label(details_window, text=f"Cast: {selected_movie['cast']}", font=("Helvetica", 12), fg="white", bg="black").pack(pady=5)
            tk.Label(details_window, text=f"Description: {selected_movie['description']}", font=("Helvetica", 12), fg="white", bg="black", wraplength=750).pack(pady=5)

            try:
                movie_image_path = selected_movie["image"]
                movie_image = Image.open(movie_image_path)  #Use PIL to open the image
                movie_image = movie_image.resize((200, 300))  #Resize the image for display
                movie_image = ImageTk.PhotoImage(movie_image)  #Convert to Tkinter format
                image_label = tk.Label(details_window, image=movie_image, bg="black")
                image_label.photo = movie_image  #Keep a reference to avoid garbage collection
                image_label.pack(pady=10)
            except Exception as e:
                print(f"Error loading movie image: {e}")
                tk.Label(details_window, text="Image not available", fg="white", bg="black").pack(pady=10)

            rent_button = tk.Button(details_window, text="Rent", command=lambda: self.add_to_cart(selected_movie, details_window), bg="green", fg="black")
            rent_button.pack(pady=10)

            exit_button = tk.Button(details_window, text="Back", command=details_window.destroy, bg="red", fg="white")
            exit_button.pack(pady=10)

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a movie to view.")

    def add_to_cart(self, movie, details_window):
        """
        Adds the selected movie to the shopping cart and closes the details window.
        """
        self.cart.append(movie)  #Add the movie to the cart
        messagebox.showinfo("Added to Cart", f"{movie['title']} has been added to your cart!")
        details_window.destroy()  #Close the movie details window after adding to cart

    def remove_from_cart(self, movie, cart_window):
        """
        Removes the selected movie from the shopping cart and closes the cart window.
        """
        if movie in self.cart:
            self.cart.remove(movie) #Remove the movie from cart
            messagebox.showinfo("Removed from Cart", f"{movie['title']} has been removed from your cart!")
            cart_window.destroy()  #Close the cart window after removing the movie
        else:
            messagebox.showwarning("Error", "Movie not found in cart.")

    def update_cart_window(self, cart_window):
        """
        Updates the cart window to reflect changes in the cart (after removing a movie).
        """
        #Clear the current widgets in the cart window
        for widget in cart_window.winfo_children():
            widget.destroy()

        #If the cart is empty, show an empty cart message
        if not self.cart:
            tk.Label(cart_window, text="Your cart is empty!", font=("Helvetica", 14), fg="white", bg="black").pack(pady=20)
        else:
            tk.Label(cart_window, text="Movies in your Cart:", font=("Helvetica", 14), fg="white", bg="black").pack(pady=10)

            total_price = 0
            total_items = len(self.cart)
            for movie in self.cart:
                frame = tk.Frame(cart_window, bg="black") #Create a frame for each movie
                frame.pack(pady=5)
                tk.Label(frame, text=movie["title"], font=("Helvetica", 12), fg="white", bg="black").pack(side=tk.LEFT, padx=10)
                remove_button = tk.Button(frame, text="Remove", command=lambda m=movie: self.remove_from_cart(m, cart_window), bg="red", fg="black")
                remove_button.pack(side=tk.LEFT)

                total_price += movie["price"]  #Add the movie's price to the total

            #Display the total price and total number of items
            tk.Label(cart_window, text=f"Total Items: {total_items}", font=("Helvetica", 14), fg="white", bg="black").pack(pady=5)
            tk.Label(cart_window, text=f"Total Price: ${total_price:.2f}", font=("Helvetica", 14), fg="white", bg="black").pack(pady=10)

            checkout_button = tk.Button(cart_window, text="Checkout", command=self.checkout, bg="green", fg="black")
            checkout_button.pack(pady=10)

        #Back button for the cart window
        back_button = tk.Button(cart_window, text="Back", command=cart_window.destroy, bg="red", fg="white")
        back_button.pack(pady=10)

    def view_cart(self):
        """
        Displays the shopping cart with movies added.
        """
        self.cart_window = tk.Toplevel(self.root)  #Create and store reference to the cart window
        self.cart_window.title("Your Cart")
        self.cart_window.config(bg="black")

        #Call the update function to populate the cart window
        self.update_cart_window(self.cart_window)

    def checkout(self):
        """
        Simple checkout function to show the total and close the cart window.
        """
        if self.cart:
            total = sum(movie['price'] for movie in self.cart)
            messagebox.showinfo("Checkout", f"Your total is ${total:.2f}. Thank you for shopping!")
            self.cart.clear()  #Clear the cart after checkout

            #Close the cart window
            if hasattr(self, 'cart_window') and self.cart_window.winfo_exists():
                self.cart_window.destroy()

        else:
            messagebox.showwarning("Cart is Empty", "Your cart is empty. Add some movies first.")

    def exit_app(self):
        """
        Exit the application with confirmation.
        """
        confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm_exit:
            self.login_window.destroy()  #Close the login window
            self.root.quit()  #Exit the main loop and close the app

#Set up the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HorrorMovieStoreApp(root)
    root.mainloop()
