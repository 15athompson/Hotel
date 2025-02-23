# Generated by Django 5.1.6 on 2025-02-22 17:37

import django.core.validators
import django.db.models.deletion
import hotel_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0002_alter_reservation_guest_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest",
            name="address_line1",
            field=models.CharField(
                max_length=80,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z0-9\\-\\',\\. ]+$",
                        message="Address can only contain letters, numbers, hyphens, apostrophes, commas, periods and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="address_line2",
            field=models.CharField(
                blank=True,
                max_length=80,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z0-9\\-\\',\\. ]+$",
                        message="Address can only contain letters, numbers, hyphens, apostrophes, commas, periods and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="city",
            field=models.CharField(
                max_length=80,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z\\-\\' ]+$",
                        message="City can only contain letters, hyphens, apostrophes and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="county",
            field=models.CharField(
                max_length=80,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z\\-\\' ]+$",
                        message="County can only contain letters, hyphens, apostrophes and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="email",
            field=models.EmailField(
                max_length=320,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                        message="Please enter a valid email address",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="first_name",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z\\-\\' ]+$",
                        message="First name can only contain letters, hyphens, apostrophes and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="last_name",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z\\-\\' ]+$",
                        message="Last name can only contain letters, hyphens, apostrophes and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="phone_number",
            field=models.CharField(
                max_length=11,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\+?44?\\d{10}$|^0\\d{10}$",
                        message="Phone number must be a valid UK number (e.g., '07123456789' or '+447123456789')",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="postcode",
            field=models.CharField(
                max_length=8,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}$",
                        message="Please enter a valid UK postcode (e.g., 'SW1A 1AA' or 'M1 1AA')",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="title",
            field=models.CharField(
                max_length=10, validators=[hotel_app.models.validate_title]
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="amount_paid",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Amount already paid by the guest",
                max_digits=6,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="guest",
            field=models.ForeignKey(
                help_text="Guest making the reservation",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reservations",
                to="hotel_app.guest",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="length_of_stay",
            field=models.PositiveSmallIntegerField(help_text="Number of nights booked"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="notes",
            field=models.TextField(
                blank=True,
                help_text="Additional notes or special requests for the reservation",
                max_length=500,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z0-9\\-\\',\\.\\!\\?\\s]+$",
                        message="Notes can only contain letters, numbers, basic punctuation and spaces",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="number_of_guests",
            field=models.PositiveSmallIntegerField(
                help_text="Number of guests staying in the room"
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Total price for the entire stay",
                max_digits=6,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="reservation_date_time",
            field=models.DateTimeField(
                help_text="Date and time when the reservation was made"
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="reservation_id",
            field=models.AutoField(
                help_text="Unique identifier for the reservation",
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="room_number",
            field=models.ForeignKey(
                help_text="Room assigned to this reservation",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reservations",
                to="hotel_app.room",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="start_of_stay",
            field=models.DateField(help_text="Check-in date"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="status_code",
            field=models.CharField(
                choices=[
                    ("RE", "Reserved"),
                    ("IN", "Checked In"),
                    ("OT", "Checked Out"),
                ],
                help_text="Current status of the reservation",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_number",
            field=models.IntegerField(
                help_text="Unique identifier for the room (e.g., 101, 102, etc.)",
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                help_text="The type/category of this room, determining its features and price",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rooms",
                to="hotel_app.roomtype",
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="bath",
            field=models.BooleanField(help_text="Indicates if the room has a bathtub"),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="deluxe",
            field=models.BooleanField(
                help_text="Indicates if this is a deluxe category room"
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="maximum_guests",
            field=models.PositiveSmallIntegerField(
                help_text="Maximum number of guests allowed in this room type"
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Nightly rate for this room type",
                max_digits=6,
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="room_type_code",
            field=models.CharField(
                help_text="Unique 1-3 letter code for the room type (e.g., 'STD' for Standard)",
                max_length=3,
                primary_key=True,
                serialize=False,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(1),
                    django.core.validators.RegexValidator(
                        "^[A-Z]{1,3}$",
                        message="The room type code must be between 1 and 3 uppercase letters",
                    ),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="room_type_name",
            field=models.CharField(
                help_text="Descriptive name for the room type", max_length=25
            ),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="separate_shower",
            field=models.BooleanField(
                help_text="Indicates if the room has a separate shower unit"
            ),
        ),
    ]
