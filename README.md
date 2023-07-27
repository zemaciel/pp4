# The Fourth Fork

![iamresponsive.png](docs/images/iamresponsive.png)

Full-Stack Project – HTML5 | CSS3 | Bootstrap 5 | Django | Python | PostgreSQL | Cloudinary

This web application, named "The Fourth Fork," is the fourth Portfolio Project for the Diploma in Full Stack Software Development with eCommerce at Code Institute. The name is derived from its significance as the fourth project and the dual meaning of "Fork," which relates to both web development and cutlery.

The project aims to allow users to create an account, log in, book a table, view, edit and delete existing bookings.

Check the live web site [here](https://pp04.herokuapp.com/)  

Repository available on [GitHub.](https://github.com/zemaciel/pp4/)

# User Experience

## Planning

The planning and development of this project adopt principles of Design Thinking and Agile. Cards containing user stories, a short description of a feature that would address a user's need, were placed on a board.

Using MoSCoW prioritisation, the stories were categorised as Must Have (critical requirements), Should Have (important but not essential), Could Have (desirable, but they are not required at this stage), and Won't Have (nice-to-have features, but they are put aside in favour of more urgent needs).

User Stories categorised as Won't Have remained in the backlog column for the next interaction.

I've used GitHub for this process. The board is available at this link [https://github.com/users/zemaciel/projects/2/views/1], and the Issues can be seen here [https://github.com/zemaciel/pp4/issues]

# Wireframes

# Design

## Colours

For the website, I choose a colour scheme to represent the restaurant's laid-back, cosy and welcoming atmosphere. A palette of rustic earth tones, such as terracotta, olive green, moss and sand, to evoke a sense of warmth and comfort.

## Typography

The font families chosen for this project are Josefin Sans and Lato, both imported from Google Fonts.

## Logo

I created a straightforward logo for both the navigation bar and the favicon. The design showcases a fork symbol positioned inside the letter "o" in the same colour scheme as the site.

## Imagery

# Database Schema

The database schema is displayed below. The relationship between customers and their bookings is established through the "user_id" columns, which link the two tables. This schema allows the system to store and manage customer information, as well as track their bookings and associated details.

![drawsqul.png](docs/images/drawsqul.png)
<details>
<summary>
Tables Details </summary>

**User Table:**

- **user**: This column represents a unique identifier for each customer in the table. It is likely used as the primary key, ensuring each customer has a distinct ID.
- **name**: This column stores the user's first name.
- **last_name**: This column stores the user's last name.
- email: This column stores the user's email address of the customer, useful for communication and identification purposes.
- **username**: This column stores the username chosen by the user for login.

**Booking Table:**

- **id**: This column is the primary key for the "Booking" table. Each booking entry has a unique identifier.
- **user**: This column represents a foreign key that links each booking to a specific customer in the "User" table. It establishes a relationship between bookings and customers, indicating which customer made the booking.
- **create_at**: This column stores the date and time when the booking entry was created.
- **booking_date**: This column stores the date of the booking, indicating when the customer plans to visit.
- **booking_time**: This column stores the time of the booking.
- **guests**: This column stores the number of people in the customer's party or group for the booking.
- **table**: This column stores information about the preferred or assigned table area for the booking, indoors or outdoors.
</details>


# Features

## **Frontend**

Main features on the pages that website visitors see and interact with.

### Navbar

### Hero Image

### Restaurant Menu

During my research for this project, I came across the website of Savor restaurant and was impressed by their use of tabs in presenting their menu. This approach is both visually appealing and efficient in terms of space utilisation, making it an ideal concept for showcasing the menu on the homepage.

### Call-to-action

At the bottom of the page, I added a call-to-action banner inviting the user to register, sign up, or book a table if the user is already logged in.

### Footer

### Signup and Login

### Forms

### Booking Cards

## Backend

This project include an administration area used by website administrators, owners or maybe in this case restaurant staff, to manage the bookings, and in the future can be use to mange website's content and other functionalities.
<details>
<summary>
Future Features</summary>

There is a lot of room for improvement on this project, and here are a few ideas that could be implemented in the future: 

- Allow the user to register using an Social Media account
- Allow the user to book a table without needing to register
- Sending booking confirmations via SMS and/or email
- Give the ability for a staff member, thru an a administrator account, to update the menu and other informations, such as opening hours.
- Password Reset: a user will be able to reset their password in case forgotten
</details>

# Deployment