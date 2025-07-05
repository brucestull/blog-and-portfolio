This error is coming from Django’s **ReadOnlyPasswordHashWidget**, which—when rendering the “Password” field in the Admin change form—calls your hasher’s `safe_summary()` method under the hood.  The default PBKDF2 hasher implements it like this:

```python
# django/contrib/auth/hashers.py
def safe_summary(self, encoded):
    algorithm, iterations, salt, hash = encoded.split('$', 3)
    …
```

Because it does

```python
algorithm, iterations, salt, hash = encoded.split('$', 3)
```

it **expects exactly four** `$`-separated parts in the stored password string. ([docs.huihoo.com][1])

---

### What’s gone wrong?

In your fixture you did:

```json
"password": "pbkdf2_sha256$…"
```

but that value only contains **two** parts (the algorithm and an ellipsis), so `split('$', 3)` returns only two elements—hence the “expected 4, got 2” error.

By Django convention, a stored hash must be in the form:

```
<algorithm>$<iterations>$<salt>$<hash>
```

For PBKDF2+SHA256, something like:

```
pbkdf2_sha256$260000$N3W8xqWbY9yT$Oe7tC9Xg3RTB1f5l2uZk1hM8b0s
```

([django.readthedocs.io][2])

---

### How to fix

1. **Generate a proper hash** and put that in your fixture. For example, in a Django shell:

   ```bash
   python manage.py shell
   ```

   ```python
   from django.contrib.auth.hashers import make_password
   print(make_password("YourPlainTextPassword"))
   # e.g. pbkdf2_sha256$260000$HtR2jYzXAsqs$X0LK9N... (full 4-part string)
   ```

   Then update your `initial_data.json`:

   ```diff
     "fields": {
   -     "password": "pbkdf2_sha256$…",
   +     "password": "pbkdf2_sha256$260000$HtR2jYzXAsqs$X0LK9N...<rest of hash>",
         …
     }
   ```

2. **Or** skip loading the raw password in fixtures and instead:

   * Create your superuser with

     ```bash
     python manage.py createsuperuser --username admin --email admin@example.com
     ```

     which will prompt you for a (validly hashed) password, *or*

   * After loading fixtures, run

     ```bash
     python manage.py changepassword admin
     ```

     to set a proper hash.

---

#### Why this matters

Django uses the full 4-part format so it knows:

* **which algorithm** to use (`pbkdf2_sha256`)
* **how many iterations** (e.g. `260000`)
* the **salt**
* and the actual **hash**

All of that metadata is required both for verifying logins *and* for safely displaying (and masking) password info in the Admin. Ensuring your fixture’s `password` value follows this convention will eliminate the unpacking error.

[1]: [Source code for django.contrib.auth.hashers - Huihoo](https://docs.huihoo.com/django/1.8/_modules/django/contrib/auth/hashers.html)

[2]: [Password management in Django](https://django.readthedocs.io/en/latest/topics/auth/passwords.html)
