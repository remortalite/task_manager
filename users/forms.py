from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username",
                  "password1", "password2")

    # do not check username for uniqueness
    def clean_username(self):
        return self.cleaned_data.get("username")
