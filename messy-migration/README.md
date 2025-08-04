# CHANGES.md

## Overview
This document outlines the changes made to complete the Messy Migration challenge. The goal was to connect a React frontend to a Flask backend that serves user data from a SQLite database.

---

## ✅ Backend Fixes (Flask + SQLite)

- Refactored `app.py` to properly initialize and query the SQLite database
- Ensured `/api/users` endpoint returns JSON with correct structure
- Added gender field to user records for frontend display
- Verified database connection and query logic with test data

---

## ✅ Frontend Fixes (React)

- Created `UserList` component to fetch and display user data
- Connected to Flask backend using `fetch()` from `/api/users`
- Rendered user name, gender, and email in a clean list format
- Added basic styling for readability and layout
- Ensured mobile responsiveness and semantic HTML structure

---

## 🧠 Debugging & Refactoring

- Fixed CORS issues between frontend and backend
- Verified API response format and handled edge cases
- Cleaned up unused code and console logs
- Modularized components for clarity and maintainability

---

## ✅ Final Output

- User List 
- Alice (female) - alice@example.com 
- Bob (male) - bob@example.com 
- Charlie (male) - charlie@example.com 
- Diana (female) - diana@example.com


---

---

## 🔒 August 4, 2025 — Security & Maintainability Refactor

### ✅ Backend Enhancements

- Implemented JWT authentication using `PyJWT`
- Secured all routes except `/login` and `/home` with token validation
- Moved `SECRET_KEY` to `.env` and loaded securely using `python-dotenv`
- Added proper HTTP status codes and error handling for login, user creation, and updates
- Prevented duplicate email creation with conflict checks (`409`)
- Refactored SQL queries to avoid syntax errors and improve clarity

### ✅ Frontend Improvements

- Stored JWT token in `localStorage` after login
- Automatically attached token to all API requests via `Authorization` header
- Refactored `UserForm` to:
  - Clear form after successful create/update
  - Auto-fill form when editing a user
  - Remove all inline styles and Tailwind classes
  - Use scoped CSS (`user-form` and `form-group`) for maintainability

### 🧠 Refactor Highlights

- Improved separation of concerns between backend logic and route handling
- Added `useEffect` to sync form state with selected user
- Created reusable CSS for consistent form styling
- Added debug logging and error messages for better developer experience

### 🤖 AI Assistance

Used Microsoft Copilot to:
- Refactor JWT logic and secure route decorators
- Suggest clean CSS structure and scoped class names
- Identify SQL syntax issues and validation gaps
- Draft this update section for `CHANGES.md`

---



## Notes

- All code is clean, modular, and documented
- App runs with `python app.py` and `npm start`
- No external libraries used beyond Flask and React basics

