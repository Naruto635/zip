# Goal Tracker

**Goal Tracker** is a web-based application built with Django that allows users to manage their personal goals and associated tasks. The application provides features such as user authentication, profile management, goal and task tracking, interactive charts for progress visualization, and seamless navigation. Users can create, update, and monitor their goals and tasks, earning points as they complete tasks, and export their tasks in iCalendar format.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Apply Migrations](#apply-migrations)
  - [Create Superuser](#create-superuser)
  - [Populate Profiles](#populate-profiles)
- [Running the Project](#running-the-project)
- [Usage](#usage)
  - [Registration & Login](#registration--login)
  - [Profile Page](#profile-page)
  - [Managing Goals](#managing-goals)
  - [Managing Tasks](#managing-tasks)
  - [Exporting Tasks](#exporting-tasks)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **User Authentication**: Secure user registration, login, and logout functionalities.
- **Profile Management**: Each user has a profile displaying their username, email, points, and progress charts.
- **Goal Tracking**: Users can create, view, and manage their personal goals with details such as title, description, deadline, priority, and recurrence.
- **Task Management**: Within each goal, users can add, view, and mark tasks as completed or incomplete.
- **Points System**: Users earn points upon completing tasks, motivating continued progress.
- **Interactive Charts**: Visual representations of task completion and goal progress using Chart.js.
- **Responsive Navigation**: Consistent and responsive navigation bar across all pages.
- **Export to iCalendar**: Users can export their tasks in the iCalendar (.ics) format for integration with calendar applications.

---

## Technologies Used

- **Backend**:
  - [Django](https://www.djangoproject.com/) - Python-based web framework.
  - [Python](https://www.python.org/) - Programming language.
- **Frontend**:
  - [Bootstrap 4](https://getbootstrap.com/) - CSS framework for responsive design.
  - [Chart.js](https://www.chartjs.org/) - JavaScript library for interactive charts.
- **Others**:
  - [jQuery](https://jquery.com/) - JavaScript library.
  - [icalendar](https://pypi.org/project/icalendar/) - Python library for iCalendar file generation.

---

## Installation

Follow these steps to set up the Goal Tracker project on your local machine.

### Prerequisites

- **Python 3.6 or higher**: Ensure Python is installed. You can download it from [here](https://www.python.org/downloads/).
- **pip**: Python package installer. It typically comes with Python.
- **Git**: For cloning the repository. Download from [here](https://git-scm.com/downloads).
- **Virtual Environment Tool**: `venv` is used in this guide, which comes with Python 3. Alternatively, tools like `pipenv` or `poetry` can be used.

### Clone the Repository

```bash
git clone https://github.com/Naruto635/goalTracker.git
cd goal_tracker_project
``
```
