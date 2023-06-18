Django Object Relational Mapping:
> Django handles Databases communication and changes by using Object Relational Mapping system
>
> Class models are transformed by migrations into database tables
>
> Each class known as a model is a database table.
>
> Each class attribute is a column
>
>> Transforming a model into a database
>>
>> Classes -> MakeMigrations -> Migrate -> Database
>>
>> Migrations will have step by step transformation that a database must do to apply the changes made in the code
>>
> We can use makemigrations command to create migration on the current code.
>
> The process of using a class, defining a model, creating a migration, and applying the migration, and the changes to the database is the job of the ORM.

## Creating a new model
>
> Models are created in models.py
>
> A new app called 'notes' is made to demonstrate.
>
> [notes/models.py](./notes/models.py)
> Once a model is created as depicted in the models.py folder
>
> We need to migrate using the command `python manage.py makemigrations`
>
> Every first migration of an app will be named like this.
> [notes/migrations/0001_initial.py](./notes/migrations/0001_initial.py)
>
> Now we need to apply the migrations using `python manage.py migrate`
> After hitting up this command a table is created.
>
> These changes wont show up on the Django Web Interface
>
> To do so, [admin.py](./notes/admin.py)
> Here we can add which models can be displayed and thus modified by the django web interface.
>

## How to handle
>
> Launching shell `python manage.py shell`
>
> Creating a note object :
>
```
    >>> from notes.models import Note
    >>> my_note = Note.objects.get(pk='1')  # get method will search for object where private key is equal to one. 
    >>> my_note.title  # We can access using the object by their attributes.
    >>> Note.objects.all()  # To Query all in the table. This returns a 'QuerySet'
    # Create a new note
    >>> new_note = Note.objects.create(title='My third note', text='This is a test note from shell for the second time',author='Kaustubh Ajgaonkar', comments='Nothing to here to see')
    # Filtering attributes that start with 'My'
    >>> Note.objects.filter(title__startswith='My') # This will return a query set with the Note Object Number
    # Exclude: Opposite of filter
    >>> Note.objects.exclude(text__icontains='Django')
    # Query sets can also be filterd
    >>> Note.objects.filter(text__icontains='Django').exclude(title__icontains='Django')  # This will filter text that contains Django but exclude title that excludes Django
```
