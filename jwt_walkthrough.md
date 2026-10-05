# JWT Authentication Walkthrough

This app issues a JWT (JSON Web Token) when a student is created. The client
sends that token with later requests, and the API uses it to identify the
student making the request.

## 1. Configure the signing secret

Add a private secret to the project's `.env` file:

```dotenv
JWT_SECRET_KEY=replace-this-with-a-long-random-secret-value
```

The app reads this setting in `config.py`. It must be at least 32 characters.
Keep it private: anyone who gets the secret could create tokens the API trusts.
If it is missing or too short, the API returns `503` instead of issuing or
accepting tokens.

## 2. Create a student and receive a token

Send the student's details to `POST /students`:

```http
POST /students
Content-Type: application/json

{
  "student_number": "S100",
  "name": "Example Student",
  "email": "student@example.com"
}
```

The service saves the student first. Then the endpoint signs a JWT containing:

- `sub`: the new student's database ID (the token subject)
- `iat`: when the token was issued
- `exp`: when it expires, 30 minutes after issue

The token is signed with the configured secret using the `HS256` algorithm.
The response includes the student details, `access_token`, and
`token_type: "bearer"`. Keep the access token and do not share it.

## 3. Send the token with a request

For an endpoint that requires a signed-in student, send the token in the
standard `Authorization` header:

```http
GET /students/me
Authorization: Bearer <access_token>
```

For example, if the response from student creation contained
`"access_token": "eyJ..."`, the header would be:

```http
Authorization: Bearer eyJ...
```

The `Bearer` prefix tells the API how the token is being sent.

## 4. How the current-user dependency works

In `dependencies.py`, `get_current_user` is a FastAPI dependency used by
`GET /students/me`:

1. `HTTPBearer` reads the token from the `Authorization` header.
2. `jwt.decode` checks its signature with the server's secret, restricts
   accepted tokens to `HS256`, and rejects expired tokens.
3. The dependency reads `sub`, converts it to a student ID, and looks up that
   student through `StudentRepository`.
4. If everything checks out, it returns the `StudentModel`. FastAPI injects
   that object into the endpoint as `current_user`.

The endpoint returns the student's public response fields. The token itself is
not encrypted; its contents can be read by whoever holds it. Do not put
passwords or other secrets inside it.

## 5. Errors to expect

- **401 Unauthorized** — token missing, invalid, expired, malformed, or its
  student no longer exists. Send a valid token or create a new one.
- **503 Service Unavailable** — `JWT_SECRET_KEY` is missing or shorter than
  32 characters. Configure the secret and restart the app.
- **409 Conflict** — the student number or email is already in use.

## Current scope

Student creation currently acts like registration and returns a token; there is
no separate login endpoint or password verification. The token proves that the
server issued it for a student ID, but does not prove a password was checked.
Add a real login flow before using this as account authentication in production.
