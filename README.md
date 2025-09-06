# my-todo-app
A web app for creating your to-do list, to help achieve your tasks as times flys away.

**Author:**
- *Ayanlowo Joshua*


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication (signup, login, password reset)
- Create, edit, delete, and view to-do items
- Mark tasks as completed
- Due date and completion tracking

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Yeshua235/my-todo-app.git
   cd my-todo-app
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the app at `http://127.0.0.1:8000/`
- Register a new account or log in
- Add, edit, and manage your to-do items

## Project Structure
- `accounts/` - User authentication and management
- `pages/` - Static and informational pages
- `todo/` - Core to-do functionality
- `templates/` - HTML templates
- `todo_webapp/` - Project settings and configuration

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

---
