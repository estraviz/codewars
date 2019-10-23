# Password validator

## Description

Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

* There needs to be at least 1 uppercase letter.
* There needs to be at least 1 lowercase letter.
* There needs to be at least 1 number.
* The password needs to be at least 8 characters long.

You are permitted to use any methods to validate the password.

### Examples

```python
password("Abcd1234") ===> True
password("Abcd123") ===> False
password("abcd1234") ===> False
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890") ===> True
password("ABCD1234") ===> False
password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,") ===> True
password("!@#$%^&*()-_+={}[]|\:;?/>.<,") ===> False
```

#### Extra info

* You will only be passed strings.
* The string can contain any standard keyboard character.
* Accepted strings can be any length, as long as they are 8 characters or more.
