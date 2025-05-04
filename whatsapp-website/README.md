# WhatsApp Website

This project is a simple web application built using Django that simulates a WhatsApp-like interface with group chat functionality.
In this i have added a whatsapp feature through which you can find the common members from the group you are at present and group from which you are comparing.
Suppose you are in your "Batch1 Official Group" --> you click on show members --> there are around 50-100 members some of the numbers are saved or some are not -->
You want to find who all your colleagues are also present in "Office SPORTS DAY group" --> for that now you can filter out through giving name "Office SPORTS DAY group" it will give you the people or same batch colleagues part of sports day group also

Just click on the show members--> give the name of the group inside the filter

## Project Structure

```
whatsapp-website
   static
      css
         styles.css
      data
         groups.json
├── whatsapp
|   
│   ├── templates
│   │   └── whatsapp
│   │       ├── base.html
│   │       ├── group1.html
│   │       ├── group2.html
│   │       └── group3.html
│   ├── views.py
│   ├── urls.py
│   └── __init__.py
         settings.py
         wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Features

- Three group chat templates: Group 1, Group 2, and Group 3.
- A base template that provides a common layout for all group pages.
- filter out feature for common group( discussed above)

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
python manage.py runserver/base/
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## License

This project is licensed under the MIT License.