# WhatsApp Website

This project is a simple web application built using Django that simulates a WhatsApp-like interface with group chat functionality.

## Project Structure

```
whatsapp-website
├── whatsapp
│   ├── templates
│   │   └── whatsapp
│   │       ├── base.html
│   │       ├── group1.html
│   │       ├── group2.html
│   │       └── group3.html
│   ├── views.py
│   ├── urls.py
│   └── __init__.py
├── manage.py
├── requirements.txt
└── README.md
```

## Features

- Three group chat templates: Group 1, Group 2, and Group 3.
- A base template that provides a common layout for all group pages.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd whatsapp-website
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the development server, use the following command:
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## License

This project is licensed under the MIT License.