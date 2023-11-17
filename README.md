# Cookify
#### Video Demo:  https://youtu.be/iu6WFDQ3ErA
#### Description:
Cookify is a web application that takes an image that contains a number of ingredients and then gives out the quantity of those ingredients required and the proper instructions for preparing a meal with those ingredients.

I’ve used APIs to OCR scan the image and get all the ingredients from it. Another API is implemented which uses the ingredients lists and gives out a list of ingredients (with the quantity) and the ordered instructions to prepare it.

When the user upload an image file at the homepage, it creates a post request to another page. It initially saves the image file on the host's computer, but removes it after an online URL for that image is created. Then using that URL, it is passed to an API for OCR scanner.

The retured text from OCR scanner is then passed to another API which takes that list of ingredients and then gives out the JSON formatted quantity of ingredients and the ordered instructions.

Throughout this project, I've used mutiple concepts taught during the CS50 course which includes Flask, APIs, Jinga, CSS, HTML, Python, etc..

#### Detailed working :
Let's delve into a more elaborate and descriptive explanation of this Flask application:

### Overview:

The Flask application, named Cookify, serves as a user-friendly platform for culinary enthusiasts. Users can upload a receipt or a list of ingredients, and the application, in turn, processes the uploaded information. The backend functionality involves text extraction via Optical Character Recognition (OCR) and leveraging external APIs to retrieve relevant recipes. Here's a detailed breakdown:

### 1. Flask Setup:

The application utilizes the Flask web framework. With `Flask(__name__)`, an instance of the Flask class is created. The `app.config` settings include enabling auto-reloading of templates for development ease.

### 2. Session Configuration:

Flask-Session is employed for session management. The configuration settings dictate that sessions are not permanent and are stored in the filesystem.

### 3. Routes:

#### a. `/` (index):
   - Renders the `index.html` template.
   - The template extends `layout.html` and presents a user-friendly interface with a form for file uploads.

#### b. `/process` (process):
   - Handles both GET and POST requests.
   - On a POST request:
     - Saves the uploaded file locally.
     - Uploads the image to Imgur for storage, obtaining the image URL.
     - Utilizes OCR Extract Text API to extract text from the image.
     - Sends the extracted text to the Recipe Finder API to get ingredients and cooking instructions.
     - Renders the `process.html` template with the retrieved data.

### 4. API Key Handling:

The application integrates API keys for secure access to external services, such as Imgur, OCR Extract Text, and Recipe Finder APIs. It's crucial to keep these keys confidential.

### 5. File Handling:

Uploaded files are stored locally temporarily for processing and then removed to maintain a clean environment.

### `templates/index.html`:

- Extends the `layout.html` template.
- Displays a welcoming interface with a Cookify logo.
- Provides a form for users to upload files containing receipts or lists of ingredients.

### `templates/layout.html`:

- Defines the overall structure of HTML pages.
- Incorporates the Bootstrap framework for responsive design.
- Displays the Cookify logo at the top.
- Contains a footer with attribution to the developer's GitHub page.

### `static/styles.css`:

- Defines CSS styles for enhanced presentation.
- Specifies background colors, image centering, and form styling for a visually appealing user experience.

### `templates/process.html`:

- Extends the `layout.html` template.
- Presents the extracted ingredients and cooking instructions retrieved from the Recipe Finder API.
- Leverages CSS styles for formatting, contributing to an organized and visually appealing output.

### Additional Notes:

- Flask-Session aids in managing user sessions effectively.
- External APIs (Imgur, OCR Extract Text, and Recipe Finder) play a pivotal role in image processing and recipe extraction.
- The inclusion of API keys underscores the importance of confidentiality.
- Styling is accomplished through a combination of Bootstrap and custom CSS.

In essence, Cookify blends the power of Flask, external APIs, and thoughtful design to create a seamless and enjoyable experience for users interested in exploring new recipes based on their uploaded ingredients or receipts.
