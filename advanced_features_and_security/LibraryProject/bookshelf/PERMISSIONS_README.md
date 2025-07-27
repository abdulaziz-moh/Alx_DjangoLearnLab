# Permissions and Groups Setup for bookshelf App

## Custom Permissions

- The `Book` model defines the following custom permissions in its `Meta` class:
  - `can_view`: Can view book
  - `can_create`: Can create book
  - `can_edit`: Can edit book
  - `can_delete`: Can delete book

## Groups

- Create groups in the Django admin:
  - **Editors**: Assign `can_edit` and `can_create` permissions.
  - **Viewers**: Assign `can_view` permission.
  - **Admins**: Assign all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Enforcing Permissions in Views

- Views for listing, creating, editing, and deleting books are protected using the `@permission_required` decorator.
- Example: `@permission_required('bookshelf.can_edit', raise_exception=True)`

## Testing

- Assign users to groups via the Django admin.
- Log in as different users to verify access control for each view.

---

This setup ensures that only users with the correct group permissions can access the relevant views for the `Book` model.
