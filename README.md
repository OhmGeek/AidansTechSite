# Aidan's Tech Inventory

## Aims:
- Add tech items, details and quantity
- Tag them, and search by tag
- Eventually, perhaps adding a hiring system through the site
- Integrate with the new Aidan's JCR website (this is a standalone django app)

## Features:
- Add tech items, details and quantity
- Add price for each (currently for one price only, but we need to add logic for managing day/week pricing)
- Simple basket for all to use

## TODO:
- [ ] User bookings
- [ ] More details about each item (stored as JSON for various fields)
- [ ] AJAX add to cart button
- [ ] Custom quantity
- [ ] Day/Week pricing
- [ ] Email order to the tech chair directly
## Credits
The cart app is pretty much an exact copy of [django-cart](https://github.com/bmentges/django-cart),
only it has been adjusted so that it works with the current version of Django (so that models import correctly).

We use this to create a simple cart thingy.
